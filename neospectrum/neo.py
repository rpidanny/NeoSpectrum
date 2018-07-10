'''
  Neo class to handle all Matrix display communication using Neo library.
'''
import thread
import numpy as np
from websocket import create_connection

class Neo:
  ws = None
  def __init__(self, host, width=32):
    self.host = host
    self.width = width
    thread.start_new_thread(self.connect, ())

  def connect(self):
    print "connecting to ws://{}".format(self.host)
    self.ws = create_connection("ws://{}".format(self.host))

  def update(self, frame):
    encoded = self.encode(self.quantize(frame))
    if self.ws != None:
      self.ws.send(encoded)

  def encode(self, data):
    # TODO: implement encoding spectrum to Neo compatible datastructure
    # print data
    # print ["{0:0.2f}".format(i) for i in data]
    tmp = ["{0:0.2f}".format(i) for i in data]
    print ", ".join(str(x) for x in tmp)
    return data

  def quantize(self, lst):
    group_size = len(lst) / self.width
    res = []
    for i in xrange(0, len(lst), group_size):
      if (i + group_size) > len(lst):
        avg = np.average(lst[i:])
      else:
        avg = np.average(lst[i:i+group_size])
      res.append(avg if avg >= 0 else 0)
    return res
