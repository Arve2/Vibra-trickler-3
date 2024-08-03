# Vibra-trickler-3
Since I can't stop dreaming about the perfect auto-trickler




## Install CircuitPython
On PC...
1. Download latest version of CircuitPython UF2 firmware file for [Pico W](https://circuitpython.org/board/raspberry_pi_pico_w/) or [Pico](https://circuitpython.org/board/raspberry_pi_pico/), preferably English-US language. _I used v9.1.0_
1. On Pico: 
   - Press and hold `BOOTSEL` button 
   - Connect to PC with USB cable
   - Release `BOOTSEL` button.
1. _The Pico boot sector will now appear as a storage device, `RPI-RP2` in file explorer._
1. On PC: Copy-paste the UF2 file to the `RPI-RP2` storage device.
1. _The Pico will reboot, loading the new CircuitPython._
1. Check your file explorer. After installing CircuitPython, the Pico should appear as `PICODRIVE`. Note the driveletter (Usually `D:` or `E:`).

## Install and configure Thonny editor
On PC...
1. Download, install and start [Thonny](https://thonny.org/). _I used v4.1.4_
1. Go to `Tools` > `Options` > `Interpreter` > 
   - Interpreter dropdown: `MicroPython (Raspberry Pi Pico)`
   - Port or WebREPL: `CircuitPython CDC control @ COMx` _Auto-detection sometimes fail with CircuitPython._
   - Click `OK`
1. Thonny should now show, at the bottom right `MicroPython (Raspberry Pi Pico) - Board CDC @ COMX`.

## Download Adafruit ToF sensor modules to /lib folder
_Besides CircuitPython, Adafruit provides an [addon module for VL6180X](https://github.com/adafruit/Adafruit_CircuitPython_VL6180X/). I used [r1.4.12](https://github.com/adafruit/Adafruit_CircuitPython_VL6180X/releases/tag/1.4.12)_

On PC...
1. Download [adafruit_vl6180x.py](https://github.com/adafruit/Adafruit_CircuitPython_VL6180X/blob/main/adafruit_vl6180x.py) and copy it to `<Pico driveletter>:\lib\adafruit_vl6180x.py` 
   - a) manually, or 
   - b) with `CMD.exe`: `curl.exe https://raw.githubusercontent.com/adafruit/Adafruit_CircuitPython_VL6180X/main/adafruit_vl6180x.py --output D:\lib\adafruit_vl6180x.py --create-dirs` _Adjust driveletter accordingly!_

## Copy this project code to Pico root folder
_Now, let's add the secret sauce of this project!_

On PC...
1. Download [.\code.py](https://github.com/arve2/Vibra-trickler-3/blob/main/code.py) and copy it to `<Pico driveletter>:\code.py` 
   - a) manually, or 
   - b) with `CMD.exe`: `curl.exe https://raw.githubusercontent.com/arve2/Vibra-trickler-3/main/code.py --output D:\code.py` _Adjust driveletter accordingly!_


## Powder hopper and trickler
@ToDo: 
- Upload STL/3mf files to repo.
- Images of pipe attachment and holes.
- Build instructions?

See https://a360.co/3Wv0UIo 

Bill of materials:
- 3D printed parts
- 6 x 8mm aluminium pipe like [this](https://www.byggmax.se/r%C3%B6r-aluminium-silver-%C3%B88x11m-p208114) or [this](https://www.stahl-shop24.de/Alu-Rundrohr-8x1mm-1000mm)
- Small screw
- 3...5V DC vibrator motor (see circuit diagram)