'''
  FFT class to encapsulate all FFT related tasks.
'''
import numpy as np

class FFT():
  START = 0

  wave_x = 0
  wave_y = 0
  spec_x = 0
  spec_y = 0

  def __init__(self, rate, bins):
    self.rate = rate
    self.bins = bins

  def process(self, data):
    self.wave_x = range(self.START, self.START + self.bins)
    self.wave_y = data[self.START:self.START + self.bins]
    self.spec_x = np.fft.fftfreq(self.bins, d=1.0 / self.rate)
    tempy = np.fft.fft(self.wave_y)
    self.spec_y = [np.sqrt(c.real ** 2 + c.imag ** 2) for c in tempy]
    self.spec_y = self.decibel(np.absolute(self.spec_y))
    return self.wave_x, self.wave_y, self.spec_x, self.spec_y

  def decibel(self, lin):
    # return 20 * np.log10(self.norm(lin))
    return 10 * np.log10(lin)

  def norm(self, sig):
    sig_max = np.float(np.max(sig))
    return 10 * sig / sig_max
