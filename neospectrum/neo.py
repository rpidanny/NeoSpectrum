'''
  Neo class to handle all Matrix display communication using Neo library.
'''
from websocket import create_connection

class Neo:

  def __init__(self, host):
    self.host = host
    # print("ws://{}:{}".format(ip, port))
    self.ws = create_connection("ws://{}".format(host))

  def update(self, frame):
    self.ws.send(frame)

  def encode(self, data):
    # TODO: implement encoding spectrum to Neo compatible datastructure
    return data
