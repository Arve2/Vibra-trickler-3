# Vibra-trickler-3
My third and best take on creating a fast, simple and reliable automatic powder trickler for handloading. 

**Since changing a lot (most!) of the code, this readme file is under reconstruction, so please check back next week. (I don't usually test my code, but when I do - I do it in Main branch.)**

Overview and operations (video): \
<a href="https://youtu.be/m2H_ZvZXtMM"><img src="./media/overview.jpg" width="400" ></a>

The key features of this design is:
- Fast, automatic weighing of powder. _40gr takes ~15...20s._
- Cheap and easy to build, event for non-nerds. _12 electrical components, a 3D print and some common garage hardware._
- Safety. _I.e. not mixing gunpowder with high current motors._
- Reliability. _I.e. being able to see any deviations on a trusted analog scale._

| Circuit view | Breadboard view |
|----|----|
|<a href="./media/circuit_diagram.jpg"><img src="./media/circuit_diagram.jpg" width="300" ></a>|<a href="./media/breadboard_above.jpg"><img src="./media/breadboard_above.jpg" width="300" ></a>|

## Intended audience
_Me_, I'm an electronics nerd and a handloader. If _you_ are "only" a handloader looking to automate your Lee scale: just follow the do's and dont's in the first part of this readme. If you are a nerd, wanting to replace components or tweak the design: There will be a part for you at the end.

# Part 1: Do It Yourself

## Disclaimer
**This build is quite literally "cooking with gas". It is _not_ controlled by any authorities or munitions manufacturer, and I suspect they would be quite nervour to see it. I can take no responsibility for damages caused by it. Proceed at your own risk!**

## Bill of materials
First, let's get some stuff. If the exact components are not available, see part two for specifications and alternatives.

Scale:
- 1x [Lee Safety scale](https://leeprecision.com/powder-handling-lee-safety-powder-scale) 
- 1x [Small magnet](https://www.electrokit.com/en/magnet-neo35-8mm-x-4mm) for improved eddy dampening. _Makes the beam less whimsy around zero._
- 100mm length of bendable wire to hold sensors, such as one strand of [solid core 230V 1.5mm$`^2`$ installation cable](https://www.biltema.se/en-se/construction/electrical-installations/installation-cables/ekk/ekk-cable-3g-15-mm2-10-m-2000062454) or [copper wire](https://www.electrokit.com/en/koppartrad-2.00mm-rulle-3.5m).
- 1x small nut and bolt to attach the bendable wire to the scale.

Electronics:
- 1x [Raspberry Pi Pico](https://www.electrokit.com/en/raspberry-pi-pico-h) or [Pico W](https://www.electrokit.com/en/raspberry-pi-pico-wh). _Pico 2 or 2W should work but are not tested._
- 1x Mini vibrator from a scrapped cellphone.
- 1x [IR fork sensor](https://www.electrokit.com/en/modul-med-optisk-lasgaffel)
- 1x [IR reflection/line sensor](https://www.electrokit.com/en/qre1113-linjefoljare-monterad-pa-kort)
- 1x [Breadboard](https://www.electrokit.com/en/kopplingsdack-400-anslutningar) or [breadboard pattern PCB](https://www.electrokit.com/en/experimentkort-breadboard-400-hal)
  - _If PCB: Consider 2x [20pin headers](https://www.electrokit.com/en/hylslist-2.54mm-1x20p) to make the Pico removable._
- 2x Small-guage cable for sensors and vibrator, such as scrapped USB cable
- 1x Micro-USB cable and power supply (USB powerbank/charger)
- 2x [100mA PTC fuses](https://www.electrokit.com/en/ptc-sakring-60v-0.1a-aterstallningsbar)
- 1x [20kohm trimpot](https://www.electrokit.com/en/trimpot-3296w-20kohm-25-varv)
- 1x [1kohm resistor](https://www.electrokit.com/en/motstand-kolfilm-0.25w-1kohm-1k)
- 1x [1N4007 diode](https://www.electrokit.com/en/1n4007-do-41-1000v-1a)
- 1x [BC547C transistor](https://www.electrokit.com/en/bc547c-to-92-npn-45v-100ma).
  - **Note the "C"! Do not use lower-gain BC547 variants!**
- 2x [PCB push button](https://www.electrokit.com/en/tryckknapp-pcb-6x6x4.8mm-svart)

Powder hopper:
- 3D printed [parts for powder hopper](./3D-parts/Hopper-parts.stl). _[Preview here](https://a360.co/3W1Bod9)._
- 95mm length of 6x8mm aluminium tube [like this](https://www.byggmax.se/r%C3%B6r-aluminium-silver-%C3%B88x11m-p208114) [or this](https://www.stahl-shop24.de/Alu-Rundrohr-8x1mm-1000mm)
- 1x Powder funnel, or cut off powder bottle top. _HDPE bottles are fine. Avoid PET due to static electricity._
- 2x 140mm length of M5 threaded rods.
- 10...12x of M5 nuts.
- 1x small screw to fasten the tube.

## Assembly
Now, let's assemble all the goodies above...

**Vibrator to tube to powder hopper:**
1. See [overview](./media/3D_parts.jpg), [top](./media/detail_hopper_above.jpg) and [bottom](./media/detail_hopper_below.jpg) images of what your'e trying to accomplish.
1. Drill six 5mm holes in the tube, as shown above. Grind the back end to an angle to fit the back of the hopper.
1. Glue the 3D printed 6x12mm plug into the tube's back end, then drill and screw it to the hopper at the mark (a small dimple 19mm up).
1. Connect a cable to the vibrator, and attach it to the tube as shown above.
   - **Make sure to isolate the wires from the tube!**

**Hopper stand:**
1. Glue the four half-moon shaped parts to the hopper plate, as shown above. _These are really only needed to adjust the angle if the powder runs too fast or slow._
1. Put some vibration absorber on the hopper plate, such as a rubber band or piece of cloth.
1. Mount the baseplate, hopper plate and funnel holder on the threaded rods with nuts, as shown above.

**Breadboard/PCB:**
1. Use a multimeter to check polarity of the push buttons. _On breadboard, you will probably need to twist their legs 90 degrees to make them fit in the right direction._
1. Attach the Pico and all components according to the [circuit](./media/circuit_diagram.jpg) and [breadboard](./media/breadboard_above.jpg) diagrams.

**Cable to sensors to scale:**
1. See [left](./media/detail_sensors_left.jpg) and [right](./media/detail_sensors_right.jpg) view images of what your'e trying to accomplish.
1. Paint a small dab of white paint/tippex/nailpolish to the tip of the beam, to improve IR reflection for sensors.
1. Solder the sensors to a cable. The `VCC` and `GND` wires can be shared by both sensors, but `OUT` must be separate.
1. Attach the sensor cable wires to the breadboard/PCB according to the [circuit](./media/circuit_diagram.jpg) and [breadboard](./media/breadboard_above.jpg) diagrams.
1. Attach the bendable wire to the scale, by drilling and screwing it as shown above. Take caution not to damage the eddy damper magnets inside! 
1. Attach the sensors to the bendable wire. _I used solder for the top sensor, and screw for the bottom. Glue would probably work just as well._
1. Bend the wire so the sensors "see" the beam in it's bottom and top position. _Notice that the QRE1113 sensor must be really close to the beam, about 1mm._


------**The text below must be revised. Ignore it for now!**------


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
