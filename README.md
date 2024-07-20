# Vibra-trickler-3
Since I can't stop dreaming about the perfect auto-trickler




## Install CircuitPython
1. On PC: Download latest version of CircuitPython UF2 firmware file for [Pico W](https://circuitpython.org/board/raspberry_pi_pico_w/) or [Pico](https://circuitpython.org/board/raspberry_pi_pico/), preferably English-US language. _I used v9.1.0_
1. On Pico: 
   - Press and hold `BOOTSEL` button 
   - Connect to PC with USB cable
   - Release `BOOTSEL` button.
1. _The Pico boot sector will now appear as a storage device, `RPI-RP2` in file explorer._
1. On PC: Copy-paste the UF2 file to the `RPI-RP2` storage device.
1. _The Pico will reboot, loading the new CircuitPython._

## Install and configure Thonny editor
On PC...
1. Download, install and start [Thonny](https://thonny.org/). _I used v4.1.4_
1. Go to `Tools` > `Options` > `Interpreter` > 
   - Interpreter dropdown: `MicroPython (Raspberry Pi Pico)`
   - Port or WebREPL: `CircuitPython CDC control @ COMx` _Auto-detection sometimes fail with CircuitPython._
   - Click `OK`
1. Thonny should now show, at the bottom right `MicroPython (Raspberry Pi Pico) - Board CDC @ COMX`.

## Download Adafruit ToF sensor modules to /lib folder
_Creds to Adafruit for_
- _[VL6180X](https://github.com/adafruit/Adafruit_CircuitPython_VL6180X/) I used [r1.4.12](https://github.com/adafruit/Adafruit_CircuitPython_VL6180X/releases/tag/1.4.12)_
- _[Bus Device (I2C)](https://github.com/adafruit/Adafruit_CircuitPython_BusDevice) I used [r5.2.9](https://github.com/adafruit/Adafruit_CircuitPython_BusDevice/releases/tag/5.2.9)_

On PC...
1. Check File Explorer. After installing CircuitPython, the Pico should appear as `PICODRIVE`. Note the driveletter, then use PowerShell to download the required files to it:
```PowerShell
$picoDrive = 'D:' #Adjust accordingly!
curl.exe https://raw.githubusercontent.com/adafruit/Adafruit_CircuitPython_VL6180X/main/adafruit_vl6180x.py --output "$picoDrive\lib\adafruit_vl6180x.py" --create-dirs
curl.exe https://raw.githubusercontent.com/adafruit/Adafruit_CircuitPython_BusDevice/main/adafruit_bus_device/i2c_device.py --output "$picoDrive\lib\adafruit_bus_device\i2c_device.py" --create-dirs

Copy-Item -Path '.\code.py' -Destination "$picoDrive\"
```