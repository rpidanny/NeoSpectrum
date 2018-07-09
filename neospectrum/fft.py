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

    def fft(self, data):
        self.wave_x = range(self.START, self.START + self.bins)
        self.wave_y = data[self.START:self.START + self.bins]
        self.spec_x = np.fft.fftfreq(self.bins, d=1.0 / self.rate)
        tempy = np.fft.fft(self.wave_y)
        self.spec_y = [np.sqrt(c.real ** 2 + c.imag ** 2) for c in tempy]
        return self.wave_x, self.wave_y, self.spec_x, self.spec_y
