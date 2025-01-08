# Vibra-trickler-3
My third and best take on creating a good DIY autotrickler for handloading.

Overview and operations (video): \
<a href="https://youtu.be/m2H_ZvZXtMM"><img src="./media/overview.jpg" width="400" ></a>

The key features of this project is:
- Fast, automatic weighing of powder. _40gr takes ~15...20s._
- Easy and cheap to build, even for non-nerds. _Only twelve electrical components and some common garage hardware._
- Safety. _I.e. not mixing gunpowder with high current motors._
- Reliability. _I.e. being able to see any deviations on a trusted analog scale._

| Circuit view | Breadboard view |
|----|----|
|<a href="./media/circuit_diagram.jpg"><img src="./media/circuit_diagram.jpg" width="300" ></a>|<a href="./media/breadboard_above.jpg"><img src="./media/breadboard_above.jpg" width="300" ></a>|

## Intended audience
Me, I'm an electronics nerd and a handloader. If you are "only" a handloader looking to automate your Lee scale: just follow the do's and dont's in the DIY part of this readme. If you _are_ a nerd, wanting to replace components or tweak the design: There will be a part for you at the end.

# Part 1: Do It Yourself

## Disclaimer
**_This build is quite literally "cooking with gas". It is not controlled by any authorities or munitions manufacturer, and I suspect they would be quite nervous if they saw this build. I can take no responsibility for damages caused by it. Proceed at your own risk!_**

## Bill of materials
First, let's get some stuff. If the exact components are not available, see part two for specifications and alternatives.

### Scale parts:
- 1x [Lee Safety scale](https://leeprecision.com/powder-handling-lee-safety-powder-scale) 
- 1x [Small magnet](https://www.electrokit.com/en/magnet-neo35-8mm-x-4mm) for improved eddy dampening. _Makes the beam less whimsy around zero._
- 100mm length of bendable wire to hold sensors. _I used one strand of [solid core 230V 1.5mm$`^2`$ installation cable](https://www.biltema.se/en-se/construction/electrical-installations/installation-cables/ekk/ekk-cable-3g-15-mm2-10-m-2000062454) but it could have been soft plastic, steel wire etc._

### Electronic parts:
- 1x [Raspberry Pi Pico](https://www.electrokit.com/en/raspberry-pi-pico-h) or [Pico W](https://www.electrokit.com/en/raspberry-pi-pico-wh). _Pico 2 or 2W should also work but I have not tested._
- 1x [Mini vibrator](https://www.aliexpress.com/item/1005008051767872.html) (from a scrapped cellphone).
- 1x [IR fork sensor](https://www.electrokit.com/en/modul-med-optisk-lasgaffel)
- 1x [IR reflection/line sensor](https://www.electrokit.com/en/qre1113-linjefoljare-monterad-pa-kort)
- 1x [Breadboard](https://www.electrokit.com/en/kopplingsdack-400-anslutningar) or [breadboard pattern PCB](https://www.electrokit.com/en/experimentkort-breadboard-400-hal)
  - _If PCB: Consider 2x [20pin headers](https://www.electrokit.com/en/hylslist-2.54mm-1x20p) to make the Pico removable._
- 2x Scrapped USB or network cable for attaching sensors and vibrator.
- 1x Micro-USB cable and power supply (USB powerbank/charger)
- 2x [100mA PTC fuses](https://www.electrokit.com/en/ptc-sakring-60v-0.1a-aterstallningsbar)
- 1x [20kohm trimpot](https://www.electrokit.com/en/trimpot-3296w-20kohm-25-varv)
- 1x [1kohm resistor](https://www.electrokit.com/en/motstand-kolfilm-0.25w-1kohm-1k)
- 1x [1N4007 diode](https://www.electrokit.com/en/1n4007-do-41-1000v-1a)
- 1x [BC547C transistor](https://www.electrokit.com/en/bc547c-to-92-npn-45v-100ma).
  - **Note the "C"! Do not use lower-gain BC547A or BC547C!**
- 2x [Push buttons](https://www.electrokit.com/en/tryckknapp-pcb-6x6x4.8mm-svart)

### Powder hopper:
- [3D printed PLA](./3D-parts/Hopper-parts.stl) or ["home brew"](./media/DIY_hopper.jpg) powder hopper. _[Preview 3D parts here](https://a360.co/3W1Bod9)._
- 95mm length of 6x8mm aluminium tube [like this](https://www.byggmax.se/r%C3%B6r-aluminium-silver-%C3%B88x11m-p208114) [or this](https://www.stahl-shop24.de/Alu-Rundrohr-8x1mm-1000mm)
- 1x Powder funnel, or top of plastic bottle. _HDPE bottles are fine. Avoid PET due to static electricity._
- 2x 140mm length of M5 threaded rods, some nuts and a small screw for assembly.

## Assembly
Now, let's assemble all the goodies above...

### 1. Make the drop tube and attach vibrator
1. See [top](./media/detail_hopper_above.jpg) and [bottom](./media/detail_hopper_below.jpg) images of what your'e trying to accomplish.
1. Drill six 5mm holes in the tube, as shown above. Grind the back end to an angle to fit the back of the hopper.
1. Connect a cable to the vibrator, and attach the vibrator to the tube as shown above.
   - **Make sure the wires are isolated from the aluminium tube!**

### 2. Attach drop tube to 3D printed powder hopper
1. See [overview](./media/3D_parts.jpg) of what your'e trying to accomplish.
1. Glue the 6x12mm plug into the tube's back end. Then drill and screw it against the mark on the hoppers back (a small dimple 19mm up).
1. Glue the four half-moon shaped parts to the hopper plate, as shown above. _For adjusting angle if powder flows too fast or slow._
1. Put something soft, such as a rubber band, under the hopper to facilitate vibration.
1. Mount the baseplate, hopper plate and funnel holder together as shown above.

### 3. Attach sensors to scale
1. See [left](./media/detail_sensors_left.jpg) and [right](./media/detail_sensors_right.jpg) view images of what your'e trying to accomplish.
1. Paint a small dab of white paint/tippex/nailpolish to the tip of the beam, to improve IR reflection for sensors.
1. Solder the sensors to a cable. _The `VCC` and `GND` wires can be shared by both sensors, but `OUT` must be separate._
1. Attach the bendable wire to the scale, by drilling and screwing it as shown above. Take caution not to damage the eddy damper magnets inside! 
1. Attach the sensors to the bendable wire. _I used solder and a screw. Glue would probably work just as well._
1. Bend the wire so the sensors "see" the beam in it's bottom and top position. _Notice that the QRE1113 sensor must be really close to the beam, about 1mm._

### 4. Assemble electronics in breadboard/PCB
1. Use a multimeter to check polarity of the push buttons. _On breadboard, you will probably need to twist their legs 90 degrees to make them fit in the right direction._
1. Attach the Pico and all components including sensors ans vibrator according to the [circuit](./media/circuit_diagram.jpg) and [breadboard](./media/breadboard_above.jpg) diagrams.

### 5. Program the Pico from a computer
1. First, download [CircuitPython](https://circuitpython.org/downloads?q=raspberry+pico) firmware `*.UF2` file for your Pico. _I used v9.1.0 but 'latest' should be fine._
1. Then, write the firmware to Pico like this:
   1. Make sure your Micro-USB cable is "real" and not only for charging.
   1. Press and hold Pico `BOOTSEL` button while connecting it by USB to computer.
   1. _The Pico's firmware volume should now appear as `RPI-RP2` in your file explorer._ Let go of `BOOTSEL` button.
   1. Copy the firmware `*.UF2` file to the `RPI-RP2` volume.
   1. _Firmware auto-installs in a few seconds. The Pico's storage volume will appear as `CIRCUITPI` or `PICODRIVE`._
1. Finally, download/save Vibra-trickler [code.py](https://raw.githubusercontent.com/Arve2/Vibra-trickler-3/refs/heads/main/code.py) to the Pico's storage volume.

### 6. Try trickling
First try trickling sugar, salt or something less volatile than powder! Your kit will need some initial tweaking:
- Try the buttons for start (left) and stop (right).
- Measure the voltage to the vibrator. It should be around 3.0 to 3.7V.
- Let the vibrator run for a while, then make sure it's not feeling hot.
- Adjust the sensors:
   - _Vibra-trickler registers the sensors default state at power-on, so you may have to power-cycle the vibra-trickler after adjusting sensors._
   - Top sensor should detect the scale's beam when the set weight of powder is in the pan, to stop the vibration.
   - Bottom sensor should detect the scale's beam at it's very bottom, but _not_ when the beam lifter (spring) has pushed up the beam a few millimeters.

After checking the above you can try proper powder and adjust the trickling speeds. 
- High speed (while beam is low) should pour powder fast, but not so fast that the beam jumps up past the set weight. Adjust the flow by tilting the powder hopper back/fourth.
- Hlow speed (while beam is approaching set weight) should be slow enough that the beam stops immediately at zero when the top sensor is triggered. Adjust the vibrator speed by turning the trim potentiometer.

**That's it!**

------**The text below must be revised. Ignore for now!**------

# Part 2: Design considerations
TBD...
