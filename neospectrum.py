from neospectrum.mic import Mic
from neospectrum.fft import FFT
from neospectrum.plot import Plot

sample = 16000
bins = 512

def main():
  mic = Mic(sample, bins)
  fft = FFT(sample, bins)
  plt = Plot(sample, bins)
  try:
    while True:
      data = mic.getchunk()
      x, y, s_x, s_y = fft.process(data)
      plt.update(x, y, s_x, s_y)
  except KeyboardInterrupt:
    mic.disconnect()
  print("End")

if __name__ == "__main__":
  main()
