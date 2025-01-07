# Vibra-trickler-3
My third and best take on creating a fast, simple and reliable automatic powder trickler for handloading. 

**Since changing a lot (most!) of the code, this readme file is under reconstruction, so please check back next week. (I don't usually test my code, but when I do - I do it in Main branch.)**

Overview and operations (video): \
<a href="https://youtu.be/m2H_ZvZXtMM"><img src="./media/overview.jpg" width="400" ></a>

The key features of this design is:
- Fast, automatic weighing of powder. _40gr takes ~15...20s._
- Cheap and easy to build, event for non-nerds. _Only twelve electrical components and some common garage hardware._
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

### Scale:
- 1x [Lee Safety scale](https://leeprecision.com/powder-handling-lee-safety-powder-scale) 
- 1x [Small magnet](https://www.electrokit.com/en/magnet-neo35-8mm-x-4mm) for improved eddy dampening. _Makes the beam less whimsy around zero._
- 100mm length of bendable wire just to hold sensors. _I used one strand of [solid core 230V 1.5mm$`^2`$ installation cable](https://www.biltema.se/en-se/construction/electrical-installations/installation-cables/ekk/ekk-cable-3g-15-mm2-10-m-2000062454) but it could have been soft plastic, steel wire etc._

### Electronics:
- 1x [Raspberry Pi Pico](https://www.electrokit.com/en/raspberry-pi-pico-h) or [Pico W](https://www.electrokit.com/en/raspberry-pi-pico-wh). _Pico 2 or 2W should work but are not tested._
- 1x Mini vibrator from a scrapped cellphone.
- 1x [IR fork sensor](https://www.electrokit.com/en/modul-med-optisk-lasgaffel)
- 1x [IR reflection/line sensor](https://www.electrokit.com/en/qre1113-linjefoljare-monterad-pa-kort)
- 1x [Breadboard](https://www.electrokit.com/en/kopplingsdack-400-anslutningar) or [breadboard pattern PCB](https://www.electrokit.com/en/experimentkort-breadboard-400-hal)
  - _If PCB: Consider 2x [20pin headers](https://www.electrokit.com/en/hylslist-2.54mm-1x20p) to make the Pico removable._
- 2x Scrapped USB or Ethernet cable for attaching sensors and vibrator.
- 1x Micro-USB cable and power supply (USB powerbank/charger)
- 2x [100mA PTC fuses](https://www.electrokit.com/en/ptc-sakring-60v-0.1a-aterstallningsbar)
- 1x [20kohm trimpot](https://www.electrokit.com/en/trimpot-3296w-20kohm-25-varv)
- 1x [1kohm resistor](https://www.electrokit.com/en/motstand-kolfilm-0.25w-1kohm-1k)
- 1x [1N4007 diode](https://www.electrokit.com/en/1n4007-do-41-1000v-1a)
- 1x [BC547C transistor](https://www.electrokit.com/en/bc547c-to-92-npn-45v-100ma).
  - **Note the "C"! Do not use lower-gain BC547 variants!**
- 2x [PCB push button](https://www.electrokit.com/en/tryckknapp-pcb-6x6x4.8mm-svart)

### Powder hopper alt. A, 3D printed:
- 3D printed PLA [parts for powder hopper](./3D-parts/Hopper-parts.stl). _[Preview here](https://a360.co/3W1Bod9)._
- 95mm length of 6x8mm aluminium tube [like this](https://www.byggmax.se/r%C3%B6r-aluminium-silver-%C3%B88x11m-p208114) [or this](https://www.stahl-shop24.de/Alu-Rundrohr-8x1mm-1000mm)
- 1x Powder funnel, or cut off powder bottle top. _HDPE bottles are fine. Avoid PET due to static electricity._
- 2x 140mm length of M5 threaded rods. Some nuts to fit, and a small screw.

### Powder hopper alt. B, garage style:
If you don't have access to a 3D printer, you can probably piece something together from stuff in your garage, like [my prototype](./media/DIY_hopper.jpg). The key thing is a _light_ but _non-static_ drop tube at a slight _downward angle_. A _baffle_, such as the funnel makes  powder flow consistently regardless is it's near empty or near full. 

## Assembly
Now, let's assemble all the goodies above...

### 1. Make drop tube and attach vibrator
1. See [top](./media/detail_hopper_above.jpg) and [bottom](./media/detail_hopper_below.jpg) images of what your'e trying to accomplish.
1. Drill six 5mm holes in the tube, as shown above. Grind the back end to an angle to fit the back of the hopper.
1. Connect a cable to the vibrator, and attach the vibrator to the tube as shown above.
   - **Make sure to isolate the wires from the tube!**

### 2. Attach drop tube to 3D printed powder hopper
1. See See [overview](./media/3D_parts.jpg) of what your'e trying to accomplish.
1. Glue the 6x12mm plug into the tube's back end. Then drill and screw it against the mark on the hoppers back (a small dimple 19mm up).
1. Glue the four half-moon shaped parts to the hopper plate, as shown above. _For adjusting angle if powder flows too fast or slow._
1. Put something soft, such as a rubber band, under the hopper to facilitate vibration.
1. Mount the baseplate, hopper plate and funnel holder together as shown above.

### 3. Attach sensors to scale
1. See [left](./media/detail_sensors_left.jpg) and [right](./media/detail_sensors_right.jpg) view images of what your'e trying to accomplish.
1. Paint a small dab of white paint/tippex/nailpolish to the tip of the beam, to improve IR reflection for sensors.
1. Solder the sensors to a cable. _The `VCC` and `GND` wires can be shared by both sensors, but `OUT` must be separate._
(./media/breadboard_above.jpg) diagrams.
1. Attach the bendable wire to the scale, by drilling and screwing it as shown above. Take caution not to damage the eddy damper magnets inside! 
1. Attach the sensors to the bendable wire. _I used solder and a screw. Glue would probably work just as well._
1. Bend the wire so the sensors "see" the beam in it's bottom and top position. _Notice that the QRE1113 sensor must be really close to the beam, about 1mm._

### 4. Assemble electronics in breadboard/PCB
1. Use a multimeter to check polarity of the push buttons. _On breadboard, you will probably need to twist their legs 90 degrees to make them fit in the right direction._
1. Attach the Pico and all components including sensors ans vibrator according to the [circuit](./media/circuit_diagram.jpg) and [breadboard](./media/breadboard_above.jpg) diagrams.

### 5. Program the Pico from a computer
1. First, download [CircuitPython](https://circuitpython.org/downloads?q=raspberry+pico) firmware `*.UF2` file for your Pico. _I used v9.1.0 but 'latest' should be fine._
1. Then, write the firmware to Pico like this:
   1. Make sure your Micro-USB cable is "real" and ont only for charging.
   1. Press and hold Pico `BOOTSEL` button while connecting it by USB to computer.
   1. The Pico's firmware volume should now appear as `RPI-RP2` in your file explorer. Let go of `BOOTSEL` button.
   1. Copy the firmware `*.UF2` file to the `RPI-RP2` volume.
   1. Firmware auto-installs in a few seconds. The Pico's main storage volume will appear as `CIRCUITPI` or `PICODRIVE`.
1. Finally, download/save Vibra-trickler [code.py](https://raw.githubusercontent.com/Arve2/Vibra-trickler-3/refs/heads/main/code.py) to the Pico's storage volume.

### 6. That's it (?)



------**The text below must be revised. Ignore it for now!**------
TBD:
- Power up.
- Start+Stop button+LED.
- Thonny/REPL
- Tweaking vibrator.
- Start with a powder _equivalent_!
- 

## Install and configure Thonny editor
On PC...
1. Download, install and start [Thonny](https://thonny.org/). _I used v4.1.4_
1. Go to `Tools` > `Options` > `Interpreter` > 
   - Interpreter dropdown: `MicroPython (Raspberry Pi Pico)`
   - Port or WebREPL: `CircuitPython CDC control @ COMx` _Auto-detection sometimes fail with CircuitPython._
   - Click `OK`
1. Thonny should now show, at the bottom right `MicroPython (Raspberry Pi Pico) - Board CDC @ COMX`.

# Design considerations
I am quite pleased with my original [Vibra-trickler 1](https://youtu.be/v3MtZg-lgy8?si=bmgzrVPSmXZy_p-L) but would like it to throw charges _faster_. This prooved hard because of physical latency/inertia of the scale beam. It was also quite cumbersome to reproduce (solder!) the extensive circuitry. Hence I tried an all-out digital and app-controlled design in [Vibra-trickler 2](https://github.com/Arve2/Vibra-trickler-2). However, the signal noise had to be mitigated, resulting in _computing_ latencies. So the time saved was only a few seconds compared to v1. 

The main ideas behind this v3 project is to use
- the vibra-trickling approach and a trusted analogue scale from v1, but 
- digital processing and PWM control from v2, and
- a scale with lighter beam (=lower latency), such as the [Lee Safety scale](https://leeprecision.com/powder-handling-lee-safety-powder-scale).

Since v1, a number of interesting "VL" ToF sensors have popped up on the makers market. With a VL6180X, it should be possible to measure the position of an analogue scale beam, and decrease the trickling speed inversely proportional to the it rising. 

## Vibrators
