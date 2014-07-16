import zmq
import random
import time
import md5

def push():
    context = zmq.Context()
    # Socket to send messages on
    sender = context.socket(zmq.PUSH)
    sender.bind("tcp://*:5557")
    print "Press Enter when the workers are ready: "
    _ = raw_input()
    print "Sending tasks to workers..."
    # The first message is "0" and signals start of batch
    sender.send('0')
    # Initialize random number generator
    random.seed()
    # Send 100 tasks
    #total_msec = 0

    tstart = time.time()
    for task_nbr in range(10000000):
        # Random workload from 1 to 100 msecs
        #workload = random.randint(1, 100)
        workload=md5.new(str(task_nbr)).hexdigest()
        #total_msec += workload
        sender.send(str(workload))

    tend = time.time()
    tdiff = tend - tstart
    total_msec = tdiff * 1000
    print "Total elapsed time: %d msec" % total_msec

if __name__ =="__main__":
    push()

