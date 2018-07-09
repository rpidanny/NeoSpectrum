'''
  Microphone class to handle all audio related tasks.
'''
import pyaudio
import numpy as np
from neospectrum.fft import FFT

class Mic:
  FORMAT = pyaudio.paFloat32
  CHANNELS = 1

  def __init__(self, rate, bins, chunk=512):
    self.rate = rate
    self.chunk = chunk
    self.bins = bins
    self.pa = pyaudio.PyAudio()
    self.stream = self.pa.open(format=self.FORMAT,
                               channels=self.CHANNELS,
                               rate=self.rate,
                               input=True,
                               output=False,
                               frames_per_buffer=self.chunk)
    self.fft = FFT(rate, bins)

  def getchunk(self):
    ret = self.stream.read(self.chunk)
    ret = np.fromstring(ret, np.float32)
    return self.fft.process(ret)

  def disconnect(self):
    self.pa.terminate()
