import argparse
import matplotlib.animation as animation
from neospectrum.mic import Mic
from neospectrum.plot import Plot
from neospectrum.neo import Neo

# Sampling rate = 2 x Max frequency (Nyquist rate)
SAMPLE = 16000

# Resolution of FFT
BINS = 512

# Frames per second
FPS = 60

def options():
  parser = argparse.ArgumentParser(
      description="Audio Spectrum Visualization with Neo")
  parser.add_argument(
      "-d", "--display", help="IP Address of Neo Display", required=True)
  parser.add_argument(
      "-D", "--daemon", help="Daemon mode without Plot", action="store_true")
  args = parser.parse_args()
  return args

# Runs fps times a second
def animate(i, line, mic, neo):
  wave_x, wave_y, spec_x, spec_y = mic.getchunk()

  # update spectrum on Neo display
  neo.update(spec_y)

  line[0].set_data(wave_x, wave_y)
  line[1].set_data(spec_x, spec_y)
  return line

def main():
  args = options()

  mic = Mic(SAMPLE, BINS)

  # Neo listens on port 81
  neo = Neo("{}:81".format(args.display))

  if args.daemon:
    print "Press ctrl + c to quit"
    try:
      while True:
        wave_x, wave_y, spec_x, spec_y = mic.getchunk()
        neo.update(spec_y)
    except KeyboardInterrupt:
      mic.disconnect()
  else:
    plt = Plot(SAMPLE, BINS)
    # setup animation loop
    ani = animation.FuncAnimation(plt.fig, animate, fargs=(
        plt.line, mic, neo), blit=True, interval=1000.0 / FPS, repeat=False)
    plt.show()
    mic.disconnect()
  print "Good Bye!"

if __name__ == "__main__":
  main()
