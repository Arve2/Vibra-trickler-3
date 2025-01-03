# Vibra-trickler-3
My third and best take on creating a simple and reliable automatic powder trickler for handloading. 

**Since changing a lot (most!) of the code, this readme file is under reconstruction, so please check back next week. (I don't usually test my code, but when I do - I do it in Main branch.)**

40gr of rifle powder takes 15...20s. Most throws are spot on "0" - better than I can trickle powder by hand.

Overview and operations (video): \
<a href="https://youtu.be/m2H_ZvZXtMM"><img src="./media/overview.jpg" width="400" ></a>

| Logic view | Breadboard view |
|----|----|
|<a href="./media/circuit_diagram.jpg"><img src="./media/circuit_diagram.jpg" width="300" ></a>|<a href="./media/breadboard_above.jpg"><img src="./media/breadboard_above.jpg" width="300" ></a>|

## Intended audience
_Me_, I'm an electronics nerd and a handloader. If _you_ are "only" a handloader looking to automate your Lee scale: just follow the do't and dont's in the first part of this readme. If you are a nerd, wanting to replace components or tweak the design: There will be a part for you at the end.

# Part 1: Do It Yourself

## Bill of materials
- 1x Mini vibrator from a scrapped cellphone
- 1x [Raspberry Pi Pico](https://www.electrokit.com/en/raspberry-pi-pico-h) or [Pico W](https://www.electrokit.com/en/raspberry-pi-pico-wh). _Pico 2 or 2W should work but are not tested._
- 1x [Breadboard](https://www.electrokit.com/en/kopplingsdack-400-anslutningar) or [breadboard pattern PCB](https://www.electrokit.com/en/experimentkort-breadboard-400-hal).
  - If PCB: Consider 2x [20pin headers](https://www.electrokit.com/en/hylslist-2.54mm-1x20p) to make the Pico removable.
- 6 x 8mm aluminium pipe like [this](https://www.byggmax.se/r%C3%B6r-aluminium-silver-%C3%B88x11m-p208114) or [this](https://www.stahl-shop24.de/Alu-Rundrohr-8x1mm-1000mm)

https://a360.co/3Wv0UIo


## Assemble hardware
@2Do

## Install CircuitPython
_Before starting, the Pico needs some firmware to run Python code._

On PC...
1. Download latest version of CircuitPython UF2 firmware file for [Pico W](https://circuitpython.org/board/raspberry_pi_pico_w/) or [Pico](https://circuitpython.org/board/raspberry_pi_pico/). _I used v9.1.0_
1. On Pico: 
   - Press and hold `BOOTSEL` button 
   - Connect to PC with USB cable
   - Release `BOOTSEL` button.
1. _The Pico boot sector will now appear as a storage device, `RPI-RP2` in file explorer._
1. On PC: Copy-paste the UF2 file to the `RPI-RP2` storage device.
1. _The Pico will reboot, loading the new CircuitPython._
1. _The Pico file storage will now appear as a storage device, `CRICUITPI` or `PICODRIVE` in file explorer. Usually driveletter `D:` or `E:`_

## Copy vibra-trickler code to Pico root folder
_Now, let's add code.py - the secret sauce of this project!_

On PC...
1. Download [.\code.py](https://github.com/arve2/Vibra-trickler-3/blob/main/code.py) to `<Pico driveletter:>\code.py` _If the Pico drive already contains an example file named `code.py`:. Remove or overwrite it._

## Install and configure Thonny editor
On PC...
1. Download, install and start [Thonny](https://thonny.org/). _I used v4.1.4_
1. Go to `Tools` > `Options` > `Interpreter` > 
   - Interpreter dropdown: `MicroPython (Raspberry Pi Pico)`
   - Port or WebREPL: `CircuitPython CDC control @ COMx` _Auto-detection sometimes fail with CircuitPython._
   - Click `OK`
1. Thonny should now show, at the bottom right `MicroPython (Raspberry Pi Pico) - Board CDC @ COMX`.


## Powder hopper and trickler
@ToDo: 
- Upload STL/3mf files to repo.
- Images of pipe attachment and holes.
- Build instructions?

See https://a360.co/3Wv0UIo 

Bill of materials:
- 3D printed parts

- Small screw
- 3...5V DC vibrator motor (see circuit diagram)

# Design considerations
I am quite pleased with my original [Vibra-trickler 1](https://youtu.be/v3MtZg-lgy8?si=bmgzrVPSmXZy_p-L) but would like it to throw charges _faster_. This prooved hard because of physical latency/inertia of the scale beam. It was also quite cumbersome to reproduce (solder!) the extensive circuitry. Hence I tried an all-out digital and app-controlled design in [Vibra-trickler 2](https://github.com/Arve2/Vibra-trickler-2). However, the signal noise had to be mitigated, resulting in _computing_ latencies. So the time saved was only a few seconds compared to v1. 

The main ideas behind this v3 project is to use
- the vibra-trickling approach and a trusted analogue scale from v1, but 
- digital processing and PWM control from v2, and
- a scale with lighter beam (=lower latency), such as the [Lee Safety scale](https://leeprecision.com/powder-handling-lee-safety-powder-scale).

Since v1, a number of interesting "VL" ToF sensors have popped up on the makers market. With a VL6180X, it should be possible to measure the position of an analogue scale beam, and decrease the trickling speed inversely proportional to the it rising. 

## Vibrators
