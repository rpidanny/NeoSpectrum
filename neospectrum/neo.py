'''
  Neo class to handle all Matrix display communication using Neo library.
'''
import thread
from websocket import create_connection

class Neo:
  ws = None
  def __init__(self, host):
    self.host = host
    # print("ws://{}:{}".format(ip, port))
    thread.start_new_thread(self.connect, ())

  def connect(self):
    self.ws = create_connection("ws://{}".format(self.host))

  def update(self, frame):
    if self.ws != None:
      self.ws.send(frame)

  def encode(self, data):
    # TODO: implement encoding spectrum to Neo compatible datastructure
    return data
