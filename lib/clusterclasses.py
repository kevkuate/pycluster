import sys
import time
import simplejson
import jsonpickle
import uuid

sys.path.insert(0, '.')

import clustertools

#main views
class master(object):
    def __init__(self):
        self.jobs    = jobheap()
        self.slaves  = {}

    def register_slave(self, slaveinfo):
        key = slaveinfo.key()
        
        if key in self.slaves:
            print "updating"
            self.slaves.pop(key)
        
        else:
            print "adding"
            
        self.slaves[ key ] = slaveinfo
    
    def get_next_command(self, slaveinfo):
        key = slaveinfo.key()
        
        if key in self.slaves:
            for jobinfo in self.jobs.queue:
                if jobinfo.canrun( slaveinfo ):
                    jobs.run(jobinfo, slaveinfo)
                    return jobinfo
                
        return None

    def update_node_status(self):
        pass
    
    def record_node_result(self):
        pass

    # ==== UI API ====
    def get_all_running_commands(self):
        return self.jobs.running
    
    def get_commands_queue(self):
        return self.jobs.queue
    
    def get_slaves(self):
        return self.slaves
    
class slave_hardware_info(object):
    def __init__(self):
        self.info = clustertools.get_computer_info()

    def key(self):
        print self.info
        return ( self.info['node'], self.info['ip'] )
    

class slave_hardware_status(object):
    def __init__(self):
        self.status = clustertools.get_computer_status()
    
    def key(self):
        print self.info
        return ( self.info['node'], self.info['ip'] )
    
class slave(object):
    def __init__(self):
        self.requester      = clustertools.requests
        self.computerinfo   = slave_hardware_info()
        self.computerstatus = slave_hardware_status()
        self.isregistered   = False
        self.masterinfo     = None
        self.masteraddr     = None
        self.isbusy         = False
        self.current_run    = None
        self.timercount     = 0
        self.curruid        = uuid.uuid1().hex
        self.computerinfo.info['uid'] = self.curruid
    
    
    def go(self):
        if self.timercount == 10 or self.timercount == 0:
            self.timercount = 0
            self.slave_register_node_info_in_master()
        
        if self.isbusy:
            self.slave_send_run_status_to_master()
            
        else:
            self.slave_get_command()

        self.slave_send_node_status_to_master()

        self.timercount += 1


    def find_master(self):
        broadcaster     = clustertools.broadcast_receiver()
        self.masterinfo = broadcaster.listenbroadcastserverinfo()
        
        if self.masterinfo is not None:
            self.masterinfo = self.masterinfo.strip().split(',')
            self.masterinfo[2] = '127.0.0.1'
            self.masteraddr = "http://%s:%s" % (self.masterinfo[2], self.masterinfo[3])
            print "MASTER ADDRESS: '%s'" % self.masteraddr


    def slave_get_command(self): # every minute when free
        payload  = jsonpickle.encode( self.computerinfo )
        postaddr = self.masteraddr + '/getcommand'
        #print "POST ADDRESS: '%s'" % postaddr
        hasadded = False
        
        while not hasadded:
            res = self.requester.post( postaddr, data=payload )
            #print "GETTING COMMAND: '%d' val '%s'" % ( res.status_code, res.text )
            
            if res.status_code == 200:
                print "SUCCESS GETTING COMMAND TEXT:",res.text
                hasadded = True
                cmddata  = jsonpickle.decode( res.text )
                print "SUCCESS GETTING COMMAND DATA:",cmddata
                self.current_run = cmddata
                
                if cmddata is not None:
                    self.isbusy = True
                
                #TODO: RUN COMMAND
                #print "CURRENT RUN:", self.current_run
                
            else:
                print "FAILED GETTING COMMAND"
                time.sleep(1)

        
        pass
        #from MASTER, get:
            #command
            #owner
            #origin
    
    
        #if not 404:
        #        if _func == start:
        #        create start time
        #        create uuid
        #        change status RUNNING
        #
        #
        #        start thread
        #        save pid
        #        create logfile
        #        create errfile
        #        create outfile
        #
        #
        #        lock server
        #
        #
        #if _func == kill:
        #        get _uuid
        #        change status CANCELLED
        #
        #
        #== ? ==
        #func upload_file
        #func download_file
        #func list_files
        pass
    
    
    def slave_register_node_info_in_master(self): # every min if not registered
        payload = jsonpickle.encode( self.computerinfo )
        putaddr = self.masteraddr + '/registernode'
        print "PUT ADDRESS: '%s'" % putaddr
        self.isregistered = False
        
        while not self.isregistered:
            res = self.requester.put(putaddr, data=payload)
            print "REGISTERING RESULT: '%d' val '%s'" % ( res.status_code, res.text )
            
            if res.status_code == 200 and res.text == 'OK':
                self.isregistered = True
                print "SUCCESS REGISTERING"
            else:
                print "FAILED REGISTERING"
                time.sleep(1)
    
    
    def slave_send_node_status_to_master(self): # every minute (heart beat)
        #server_info
        #proc%
        #mem%
        #load
        #lock state
        #status RUNNING / FAILED / SUCCESS / CANCELLED / FREE
    
        #if status not FREE:
        #    command
        #    owner
        #    origin
        #    start time
        #    ela time
        #    logfile name
        #    errfile name
        #    outfile name
        #    uuid
        
        payload = jsonpickle.encode( self.computerstatus )
        putaddr = self.masteraddr + '/updatenodestatus'
        print "PUT ADDRESS: '%s'" % putaddr
        hasadded = False
        
        while not hasadded:
            res = self.requester.put(putaddr, data=payload)
            print "SENDING STATUS: '%d' val '%s'" % ( res.status_code, res.text )
            
            if res.status_code == 200 and res.text == 'OK':
                print "SUCCESS SENDING STATUS"
                hasadded = True
                
            else:
                print "FAILED SENDING STATUS"
                time.sleep(1)
    
    
    def slave_send_run_status_to_master(self):
        payload = jsonpickle.encode( self.current_run )
        putaddr = self.masteraddr + '/updaterunstatus'
        print "PUT ADDRESS: '%s'" % putaddr
        hasadded = False
        
        while not hasadded:
            res = self.requester.put(putaddr, data=payload)
            print "SENDING RUN STATUS: '%d' val '%s'" % ( res.status_code, res.text )
            
            if res.status_code == 200 and res.text == 'OK':
                print "SUCCESS SENDING RUN STATUS"
                hasadded = True
                
            else:
                print "FAILED SENDING RUN STATUS"
                time.sleep(1)


    def slave_send_command_result_to_master(self): # on completion
        self.curruid        = uuid.uuid1().hex
        self.computerinfo.info['uid'] = self.curruid
        #send
        #    command
        #    owner
        #    origin
        #    start time
        #    ela time
        #    uuid
        #    run result
        #    pid
        #    logfile name
        #    errfile name
        #    outfile name
        #    status RUNNING / FAILED / SUCCESS / CANCELLED
        #unlock server
        #set status FREE
        pass



class ui(object):
    def __init__(self):
        pass





#auxiliary classes
class job(object):
    def __init__(self):
        pass
    
    def canrun( slaveinfo ):
        pass

    def attach_slave(self, slaveinfo ):
        #attach uid
        pass
    
    def get_uid(self):
        pass
    
class jobheap(object):
    def __init__(self):
        self.queue   = []
        self.running = {}
    
    def get_queue(self):
        return self.queue
    
    def delete_job(self, jobinfo):
        uid = jobinfo.get_uid()
        if uid in self.running:
            self.running.pop( uid )
    
    def add_job(self, jobinfo):
        self.queue.append( jobinfo )
    
    def run(self, jobinfo, slaveinfo):
        jobinfo.attach_slave( slaveinfo )
        self.running.append( jobinfo )
        self.queue.pop( jobinfo )


