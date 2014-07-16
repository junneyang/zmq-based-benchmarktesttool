import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5566")

while True:
     socket.send("HELLO")
     socket.send("WORLD")