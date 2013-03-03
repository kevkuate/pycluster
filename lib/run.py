#!/usr/bin/python
import subprocess
from threading  import Thread
import sys, traceback

try:
    from Queue import Queue, Empty
except ImportError:
    from queue import Queue, Empty  # python 3.x

if __name__=="__main__":
    import os
    fullpath=os.getcwd()

    # add parent folder to path

    #print "CURRENT PATH " + fullpath
    fullpath=os.path.abspath(fullpath)
    #print "PREVIOUS PATH " + fullpath
    sys.path.insert(0,fullpath)
    #print "PATH " + str(sys.path)
    import constants

def enqueue_pipe(pipe, queue):
    for line in iter(pipe.readline, b''):
        queue.put(line)
    pipe.close()



def runString(id, cmdFinal, executable="/bin/bash", outout=sys.stdout, outerr=sys.stderr, outlog=sys.stdout):
    try:
        outlog.write(id + " :: OPENING PROCESS FOR CMD '" + cmdFinal + "'" + "\n")

        q_out = Queue()
        q_err = Queue()

        p = subprocess.Popen( cmdFinal, shell=True,
            executable = executable,
            stdout     = subprocess.PIPE,
            stderr     = subprocess.PIPE )

        #http://stackoverflow.com/questions/375427/non-blocking-read-on-a-subprocess-pipe-in-python

        t_err = Thread(target=enqueue_pipe, args=(p.stderr, q_err))
        t_err.daemon = True # thread dies with the program
        t_err.start()

        t_out = Thread(target=enqueue_pipe, args=(p.stdout, q_out))
        t_out.daemon = True # thread dies with the program
        t_out.start()



        pid           = p.pid

        try:

            outlog.write(id + " :: CHECKING POOL" + "\n")
            while p.poll() is None:
                #print "JOB :: " + id + " :: TRYING TO READ PIPE (" + str(p.poll()) + ")"
                try:
                    lineOut = q_out.get_nowait()
                    #lineOut = q_out.get(timeout=1)
                    outout.write(id + " :: " + lineOut)
                except Empty:
                    pass
                    #print('no stderr output yet')
                #else: # got line


                try:
                    lineErr = q_err.get_nowait()
                    #lineErr = q_err.get(timeout=1)
                    outerr.write(id + " :: " + lineErr)
                except Empty:
                    pass
                    #print('no stderr output yet')
                #else: # got line




            outlog.write(id + " :: GETTING RETURN CODE" + "\n")
            outlog.write(id + " :: WAITING" + "\n")
            #print "WAITING"
            exitCode = p.returncode
            p.wait()

            outlog.write(id + " :: JOINING THREADS" + "\n")
            t_err.join()
            t_out.join()

            outlog.write(id + " :: EMPTYING QUEUE" + "\n")
            while not q_out.empty():
                outout.write(id + " :: " + q_out.get_nowait() + "\n")
            while not q_err.empty():
                outerr.write(id + " :: " + q_err.get_nowait() + "\n")

            outlog.write(id + " :: QUEUE EMPTY" + "\n")

            #print "JOB :: " + id + " :: JOINING QUEUES"
            #q_err.task_done()
            #q_out.task_done()
            #q_err.join()
            #q_out.join()
            #print "JOB :: " + id + " :: FINISHED"

            if exitCode:
                outlog.write(id + " :: STR {" + cmdFinal + "} :: RETURNED: " + str(exitCode) + " THEREFORE FAILED " + "\n")
                outlog.write(id + " :: FAILED TO RUN " + cmdFinal + " :: RETURNED: " + str(exitCode) + " THEREFORE FAILED " + "\n")
                return(exitCode)
            #print "FINISHED"

            #print "FINISHED RUNNING CMD " + cmdFinal + " WRITING"
            #Job.outputFileWriter.write(id, p.stdout)
            #print "FINISHED RUNNING CMD " + cmdFinal + " WROTE"
            outlog.write(id + " :: REACHED END. FINISHING WITH STATUS " + str(exitCode) + "\n")

            return exitCode

        except Exception, e:
            outlog.write(id + " :: Exception (Job__launch_out): " + str(e) + "\n")
            outlog.write(id + " :: FAILED TO RUN " + cmdFinal + " EXCEPTION " + str(e) + "\n")
            outlog.write(id + " :: TRACEBACK :: "  + " ".join(traceback.format_stack()) + "\n")
            exitCode = 252
            return exitCode

    except Exception, e:
        outlog.write(id + " :: Exception (Job__launch): " + str(e) + "\n")
        outlog.write(id + " :: FAILED TO RUN " + cmdFinal + " EXCEPTION " + str(e) + "\n")
        outlog.write(id + " :: TRACEBACK :: "  + " ".join(traceback.format_stack()) + "\n")
        exitCode = 253
        return exitCode






#try:
#    (stdOut, stdErr) = p.communicate(input=None)
#
#    try:
#        line = q_out.get_nowait() # or q.get(timeout=.1)
#    except Empty:
#        print('no output yet')
#    else: # got line
#        print line
#
#    if stdOut:
#        #sys.stdout.write("LINE<1> "+str(stdOut))
#        messaging.stdout(id, str(stdOut), internal=True)
#
#    if stdErr:
#        #sys.stderr.write("LINE<2> "+str(stdErr))
#        messaging.stderr(id, str(stdErr), internal=True)
#
#    #print "WAITING"
#    messaging.exitCode = p.wait()
#    if messaging.exitCode:
#        print "JOB :: " + id + " :: STR {" + cmdFinal + "} :: RETURNED: " + str(messaging.exitCode) + " THEREFORE FAILED "
#        messaging.status = constants.FAILED
#        messaging.addError("FAILED TO RUN " + cmdFinal + " :: RETURNED: " + str(messaging.exitCode) + " THEREFORE FAILED ")
#        return messaging.exitCode
#    #print "FINISHED"
#
#    #print "FINISHED RUNNING CMD " + cmdFinal + " WRITING"
#    #Job.outputFileWriter.write(id, p.stdout)
#    #print "FINISHED RUNNING CMD " + cmdFinal + " WROTE"
#    print "JOB :: " + id + " :: REACHED END. FINISHING WITH STATUS " + constants.STATUSES[messaging.status] + " " + str(messaging.exitCode)
#    messaging.status   = constants.FINISH
#    messaging.exitCode = 0
#    return messaging.exitCode
