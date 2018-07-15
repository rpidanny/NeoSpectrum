# Neo Spectrum

![alt text](https://github.com/rpidanny/assets/raw/master/NeoSpectrum/NeoSpectrum.gif "Neo Spectrum Demo")

Audio Spectrum visualization on [Dot Matrix Display](https://raw.githubusercontent.com/rpidanny/assets/master/Neo/MAX7219-Matrix.jpeg).

## Getting Started

### Prerequisites

* MAX72XX based [Dot Matrix Display](https://raw.githubusercontent.com/rpidanny/assets/master/Neo/MAX7219-Matrix.jpeg).
* ESP8266 Dev Board with [Neo](https://github.com/rpidanny/Neo)'s [MatrixEditor](https://github.com/rpidanny/Neo/tree/master/examples/MatrixEditor) example sketch installed.

### Installation

```shell
pip install -r requirements.txt
```

## Usage

### With Plot

```shell
python neospectrum.py --display 192.168.2.13
```

### Without Plot (Daemon Mode)

```shell
python neospectrum.py --display 192.168.2.13 -D
```

## Wishlist

* [x] Daemon mode
* [x] Real Time Audio Processing
* [x] Visualization on local system
  * [x] Input audio wave
  * [x] Audio spectrum
* [x] Visualization on Matrix Display
  * [x] Audio spectrum
* [x] Get Neo's IP as argument

## License

This project is licensed under the MIT License - see the [license file](LICENSE) file for details