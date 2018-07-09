'''
  Plot class to encapsulate all visualization tasks.
'''
import matplotlib.pyplot as plt

class Plot:
  START = 0

  def __init__(self, rate, bins):
    self.rate = rate
    self.bins = bins

    self.fig, (self.ax1, self.ax2) = plt.subplots(2, 1)
    self.line1, = self.ax1.plot([], [], lw=2)
    self.line2, = self.ax2.plot([], [], lw=2, color='r')
    self.line = [self.line1, self.line2]

    self.ax1.set_ylim(-1.5, 1.5)
    self.ax1.set_xlim(self.START, self.START + self.bins)
    self.ax1.grid()

    self.ax2.set_ylim(0, 100)
    self.ax2.set_xlim(0, self.rate / 2)
    self.ax2.grid()

  def show(self):
    plt.show()