'''
  Plot class to encapsulate all visualization tasks.
'''

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

class Plot:
    START = 0
    def __init__(self, rate, bins):
        self.rate = rate
        self.bins = bins

    def update(self, wave_x, wave_y, spec_x, spec_y):
        plt.clf()
        # wave
        plt.subplot(311)
        plt.plot(wave_x, wave_y)
        plt.axis([self.START, self.START + self.bins, -0.5, 0.5])
        plt.xlabel("time [sample]")
        plt.ylabel("amplitude")
        #Spectrum
        plt.subplot(312)
        plt.plot(spec_x, spec_y, marker= 'o', linestyle='-')
        plt.axis([0, self.rate / 2, 0, 50])
        plt.xlabel("frequency [Hz]")
        plt.ylabel("amplitude spectrum")
        #Pause
        plt.pause(.01)
