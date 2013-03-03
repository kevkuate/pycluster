#!/usr/bin/python
import sys,os
import re
import pprint
import time
import base64
import datetime
import time
import simplejson
import jsonpickle

sys.path.insert(0, 'lib')

import clustertools
import clusterclasses

#TODO: ADD PIPELINE DATA


setupfile    = 'uisetup.json'


if not os.path.exists(setupfile):
    print "count not find setup file %s" % setupfile
    sys.exit(1)

for k,v in jsonpickle.decode(open(setupfile, 'r').read())['server'].items():
    #print "SERVER K %s V %s" % (k, v)
    globals()[k] = v

for k,v in jsonpickle.decode(open(setupfile, 'r').read())['datas' ].items():
    #print "DATAS K %s V %s" % (k, v)
    globals()[k] = v

    
SLAVESLEEPTIME = 60

def main():
    slave     = clusterclasses.slave()
    slave.find_master()
    
    while True:
        slave.go()
        time.sleep(SLAVESLEEPTIME)
    


if __name__ == '__main__':
    main()
