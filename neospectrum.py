import matplotlib.animation as animation
from neospectrum.mic import Mic
from neospectrum.plot import Plot

sample = 32000
bins = 512
fps = 60

# Runs fps times a second
def animate(i, line, mic):
  wave_x, wave_y, spec_x, spec_y = mic.getchunk()

  # TODO: update spectrum on Neo

  line[0].set_data(wave_x, wave_y)
  line[1].set_data(spec_x, spec_y)
  return line

def main():
  mic = Mic(sample, bins)
  plt = Plot(sample, bins)
  ani = animation.FuncAnimation(plt.fig, animate, fargs=(
      plt.line, mic), blit=True, interval=1000.0 / fps, repeat=False)
  plt.show()
  mic.disconnect()
  print "Good Bye!"

if __name__ == "__main__":
  main()
