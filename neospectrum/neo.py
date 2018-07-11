'''
  Neo class to handle all Matrix display communication using Neo library.
'''
import thread
import numpy as np
from websocket import create_connection

class Neo:
  ws = None
  sc = 8.0 / 1 # 8 pixels on matrix display / max 20 ampliture of spectrum
  prev = ''
  def __init__(self, host, width=32):
    self.host = host
    self.width = width
    thread.start_new_thread(self.connect, ())

  def connect(self):
    print "connecting to ws://{}".format(self.host)
    self.ws = create_connection("ws://{}".format(self.host))

  def update(self, frame):
    if self.ws != None:
      encoded = self.encode(self.quantize(frame))
      # only update display if frame changes
      if encoded != self.prev:
        self.ws.send(encoded)
        self.prev = encoded

  def encode(self, data):
    arr = np.full(self.width, 0, dtype=int)
    enc = '#'
    for row in range(0, 8):
      # TODO: some optimizations here
      for cols, val in enumerate(data):
        if (8 - row) <= val:
          arr[cols] = 1
      for dis in xrange(0, self.width, 8):
        tmp = arr[dis:dis + 8]
        val = 0
        for idx, b in enumerate(tmp):
          val += (2 ** (7 - idx)) * b
        enc += str(val).zfill(3)
    return enc

  def quantize(self, lst):
    group_size = len(lst) / (2 * self.width)
    res = []
    for i in xrange(0, (len(lst) / 2), group_size):
      if (i + group_size) > len(lst):
        m = max(lst[i:])
      else:
        m = max(lst[i:i+group_size])
      res.append(self.scale(m) if m >= 0 else 0)
    return res

  def scale(self, ip):
    return int(ip * self.sc)

  # def to_matrix(self, arr):
  #   mat = np.full((8, len(arr)), 0, dtype=int)
  #   enc = ['#']
  #   for row in range(0, 8):
  #     for cols, val in enumerate(arr):
  #       if (8 - row) <= val:
  #         mat[row][cols] = 1
  #     for dis in xrange(0, len(arr), 8):
  #       tmp = mat[row][dis:dis + 8]
  #       val = 0
  #       for idx, b in enumerate(tmp):
  #         val += (2 ** (7 - idx)) * b
  #       enc.append(str(val).zfill(3))
  #   return enc
