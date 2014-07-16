#-*- coding: utf-8 -*-
#!/usr/bin/env python
import sys
import time
import zmq

import httplib
import json

from  multiprocessing import Process
import threading

def worker():
    context = zmq.Context()
    receiver = context.socket(zmq.PULL)
    receiver.connect("tcp://localhost:5557")
    #receiver.setsockopt(zmq.IDENTITY, sys.argv[1])

    sender = context.socket(zmq.PUSH)
    sender.connect("tcp://localhost:5558")
    controller = context.socket(zmq.SUB)
    controller.connect("tcp://localhost:5559")
    controller.setsockopt(zmq.SUBSCRIBE, "")
    poller = zmq.Poller()
    poller.register(receiver, zmq.POLLIN)
    poller.register(controller, zmq.POLLIN)

    conn = httplib.HTTPConnection("10.81.15.47:18080")
    headers = {"Content-type":"application/json","Connection":"Keep-Alive"}
    params = ({
                   "service": "UserService",
                	"method": "GetUserPreference",
                   "request": {
                	  "header": {
                   	   "subservice":"sub",
                   	   "secretkey": "pass",
                   	   "servicekey": "key1"
               	   },
                   "cuid": "fed3641138107dca4c101fd70fa96979",
                   "srcType": ["MAP_CATEGORY","TUANGOU_PRICE"],
                "include_tag":[u"医疗",u"建材市场"],
                "exclude_tag":[u"体检中心",u"文具店"]
        	   }
        })

    while True:
        socks = dict(poller.poll())
        if socks.get(receiver) == zmq.POLLIN:
            message = receiver.recv()
            '''sys.stdout.write(message+'\t')
            sys.stdout.flush()

            workload = int(message)  # Workload in msecs
            time.sleep(workload*0.01)'''

            try:
                conn.request("POST", "/lbs/da/openservice", json.JSONEncoder().encode(params), headers)
                response = conn.getresponse()
                data = response.read()
                #print data
                conn.close()
            except Exception as e:
                #print(e)
                pass


            sender.send(message)
        if socks.get(controller) == zmq.POLLIN:
            break

if __name__ =="__main__":
    for wrk_num in range(150):
        Process(target=worker, args=()).start()
        #threading.Thread(target=worker, args=()).start()

