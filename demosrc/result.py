#-*- coding: utf-8 -*-
#!/usr/bin/env python
import sys
import time
import zmq

def result():
    context = zmq.Context()
    receiver = context.socket(zmq.PULL)
    receiver.bind("tcp://*:5558")
    controller = context.socket(zmq.PUB)
    controller.bind("tcp://*:5559")
    receiver.recv()
    tstart = time.time()
    cnt=0
    for task_nbr in xrange(2000000):
        r=receiver.recv()
        '''if task_nbr % 10 == 0:
            sys.stdout.write(":")
        else:
            sys.stdout.write(".")'''
        '''sys.stdout.write(r+"\t")
        sys.stdout.flush()'''
        cnt+=1
        #print "complete send: %d\r" %(cnt),

    tend = time.time()
    tdiff = tend - tstart
    total_msec = tdiff * 1000
    print "Total elapsed time: %d msec" % total_msec
    print "Total cnt: %d" % cnt
    controller.send("KILL")
    time.sleep(1)

if __name__ =="__main__":
    result()

