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
- 1x Mini vibrator from [AliExpress](https://www.aliexpress.com/item/1005006636006743.html) or a scrapped cellphone.
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
  - **Note the "C"! Do not use lower-gain BC547A or BC547B!**
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
1. Glue the 6x12mm plug into the tube's back end. Then drill and screw it against the hole at the back of the hopper.
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
1. Attach the Pico and all components including sensors ans vibrator according to the [circuit](./media/circuit_diagram.jpg) and [breadboard](./media/breadboard_above.jpg) diagrams. _If using a [breadboard PCB](https://www.electrokit.com/en/experimentkort-breadboard-400-hal), the result will be [this](./media/PCB_above.jpg) dandy._

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
Your kit will need some initial tweaking before using real powder:
- Try the buttons for start (left) and stop (right).
- Measure the voltage to the vibrator. It should be around 3.0 to 3.7V.
- Let the vibrator run for a while, then make sure it's not feeling hot.
- Adjust the sensors:
   - _Vibra-trickler registers the sensors default state at power-on, so you may have to power-cycle the vibra-trickler after adjusting sensors._
   - Top sensor should detect the scale's beam when it reaches the set weight, to stop the vibration.
   - Bottom sensor should detect the scale's beam at it's very bottom, but _not_ when the beam lifter (spring) has pushed up the beam a few millimeters. _QRE1113 sensors have no LED indicator, but output voltage drops at detection._

After checking the above you can try real powder and adjust the trickling speeds. 
- High speed (while beam is low) should pour powder fast, but not so fast that the beam jumps up past the set weight. Adjust the flow by tilting the powder hopper back/fourth.
- Low speed (while beam is approaching set weight) should be slow enough that the beam stops immediately at zero when the top sensor is triggered. Adjust the vibrator speed by turning the trim potentiometer.

**That's it!**

# Part 2: Design considerations
_This is quite a nerdy wall of text, but it might be helpful in troubleshooting or replacing components._

## Scale
TL;DR: We all hate flimsy Lee scales, but for this project they are great.

I built my [first vibra-trickler](https://youtu.be/v3MtZg-lgy8) around a RCBS 5-10 powder scale. Very stable, but also _slow_: The weight of the beam creates inertia which leads to mechanical latency. I.e. the beam does not rise in a nanosecond, even if you dump 10gr of powder in at once. Thus the powder flow must be kept be painstakingly slow, not to jump past the set weight..

I tried to escape most of the mechanical latency with my [second vibra-trickler](https://github.com/Arve2/Vibra-trickler-2) by using a loadcell and an ADC (Analog to Digital converter). But since the converter output was imprecise, it needed to be smoothed out to a sliding window average. Thus, the weight in the computer would still lag behind the actual powder weight. Dead end. Also, I never felt _really_ sure about the accuracy. "How can I _know_ the charge weight is what the computer tells me?"

A Lee Safety scale by comparison, is annoyingly _fast_. The main critique is that "they are too whimsy"! For hand trickling I  agree. But for automation this is a _feature_! Whimsiness in all it's glory, enough is enough. The DIY part instructs to add an extra eddy damper magnet (Creds to fellow handloader S.S). If Lee did this themselves, RCBS and Redding would loose 50% of their scales sales! Anyways, the extra magnet makes the Lee Safety scale _fast but not whimsy_. Regarding accuracy: I have no reason to consider it less accurate than an expensive RCBS. If the computer or sensors are off, I can easily tell from looking at the beam.

## Vibration and flow
TL;DR: Lower current --> safer than conventional motors.

To speed up handloading, the powder needs to flow fast. Most rotating motors for such purpose draws current in the order of 0.5 to 1.0 amperes. Call me neurotic, but I do not want that much current anywhere near powder! A small cellphone-style vibrator on the other hand, only draws around 75 _milli_-amperes so it can be secured with a fuse rated at 100mA.

If the vibrator is too powerful or too feeble, the flow can be adjusted by tweaking some basic pshyics, such as
- Angle of feeding tube,
- Larger/smaller holes in feeding tube,
- More/less spongy material under powder hopper,
- Lowering/raising the funnel to lessen/ingrease mass of powder in hopper,

The low flow vibration (towards the end) is controlled by the potentiometer. The high flow vibration is hard coded in Python. It _is_ possible to change it though:
1. Connect the Pico to a PC and use a text editor to modify `code.py`.
1. Modify the variable `vib_dc_fast = 65535` (about half way down the file). 0 is 0% speed and 65535 is 100%.

If the amount of powder in a hopper decreases, is will absorb less vibrations, causing a higher flow though the drop tube. This effect is negated by the funnel acting as a baffle. Similar to a birds feeding table, the amount of powder (or birdseed) is kept consistant irrespective of the amount in the baffle.

## Sensors
TL;DR: you could probably go with almost any sensor breakout module.

To handle sensors of all (most?) different kinds, `code.py` reads all sensors as analog input i.e. _volts_. The values are read and stored at boot. While trickling, a sensor is considered as "detecting change" if the voltage differs significantly up or down from the boot value. Note that some line detecting sensors are "discharge time" sensors, such as [this QRE1113 breakout](https://www.sparkfun.com/sparkfun-line-sensor-breakout-qre1113-digital.html) - as they react in _time_ rather than _voltage_, they are not compatible with this project.

Some commonly available sensors that I have tried:
- [TCRT5000 breakout boards](https://grobotronics.com/infrared-sensor-tcrt5000.html): Digital signal. Reflection=3V. No reflection=0V. Very wide angle detection, needs some kind of blinders - [3D-printed](./3D-parts/TCRT5000-blinder.stl), heat shrink tube or simliar.
- [TCRT5000](https://grobotronics.com/tcrt5000-950nm.html): Analog signal. Voltage varies with distance. Proportionally or disproportionally depending on resistors circuit setup. Wide angle as above.
- [QRE1113 breakout board](https://www.electrokit.com/en/qre1113-linjefoljare-monterad-pa-kort): Analog signal. Voltage varies with distance. Reflection=lower V. No reflection=higher V. Very short range detection.
- [Fork sensor breakout board](https://www.electrokit.com/en/modul-med-optisk-lasgaffel): _Should_ be digital signal but works really bad, so the voltage is really more like 2.5V at detection and 1.5V at no detection. Precision is great though!
- [RPR-220](https://www.electrokit.com/en/rpr-220-fotointerruptor-6mm-800nm): Analog signal. Voltage varies with distance. Optimal detection range and angle! The downside is you need to solder your own breakout board around it. 47kohm to the transisor and 100ohm to the IR LED worked for me.

_I have also tried some ToF distance sensors, including [VL6180X](https://www.electrokit.com/en/avstandssensor-600mm-vl6180x) but the range detection was just too inconsistent._

## Code.py
The Python script [code.py](./code.py) is the main and only software component for this project. It is auto-started when the Pico powers up. No need to be gentle about power cycles - the Pico runs _firmware_ rather than an operating system. So just pull/insert the USB power cable to reboot it.

### Start/Stop buttons
The buttons are handled as digital inputs. Pressing a button connects it's pin to `GND`. Similar to the sensors, the buttons default values are stored at boot. They are then considered 'pressed' if their _value changes_. Thus, both NC (Normally CLosed) or NO (Normally Open) buttons may be used.

### ADC, for sensors and trimpot
The Pico has three ADC (Analog to Digital Converter) input pins. One is used for the bottom sensor, one for the top sensor, and one for the trim potentiometer. Consider these as volt meters in the range 0.0 to 3.3V. The variable `sensor_detect_volts` controls how much variation in voltage (up or down) is needed to consider a sensor as "detecting change".

### PWM, for vibrator voltage
The Pico provides PWM ([Pulse Width Modification](https://en.wikipedia.org/wiki/Pulse-width_modulation)) to control the voltage going to the vibrator by varying the PWM DC (Duty Cycle).
- At high speed, the PWM DC is set to 100% _(But still closer to 3 than 5 volts - maybe due to losses in the PTC fuse?)._
- At slow speed, the PWM DC is set to 100% minus the ADC input from the trim potentiometer.
- At stop, the PWM DC is set to 0%.

### Function trickle()
This is the main loop that auto-starts at boot and iterates every ~1/20 to ~1/10 second. It checks the input from buttons and sensors, plus a 60s time-fuse. It then adjusts the output PWM DC accordingly. The onboad LED flickers with each iteration, and turns dark to indicate buttons pressed.

The normal trickling process is as follows:
1. Booting up the Pico
   - resets trickling phase to `0` --> PWM DC = `0%` and
   - stores the sensors default ADC values. _The beam is resting at the bottom of the scale, i.e. detected by the low sensor._
1. Pressing start button
   - resets the time-fuse to 0s,
   - sets trickling phase to `1` --> PWM DC = `100%` --> powder drops fast.
1. Neither the low or high sensor detects the beam, so assume it's started moving up. This sets trickling phase to `2` -->
   - First, PWM DC = `0%` to let the beam stop swinging for a short while.
   - Then, PWM DC = `100% - trimpot ADC %`. _Trimpot value is refreshed in every iteration so you can tweak the slow speed 'live'._
1. The top sensor detects the beam, so it must be at zero - done! --> reset trickling phase to `0`.

Phase `0` may also be triggered by
- pressing stop button,
- the time passed since start exceeding 60s.

If connecting to a PC running Thonny, the trickle() loop will be terminated to enable editing. If started in a Thonny terminal, you will also be able to see the number of iterations and seconds spent in each trickling phase, and the total.

### Function try_vib_fast()
For tweaking/troubleshooting of the fast speed PWM DC, by running the vibrator for a given number of seconds at a given DC (int range 0...65535). Only available through Thonny or other Python terminal.

### Function try_vib_slow()
For tweaking/troubleshooting of the slow speed PWM DC, by running the vibrator for a given number of seconds while turning the trimpot. Only available through Thonny or other Python terminal.

### Function try_inputs()
For tweaking/troubleshooting of input from buttons, sensors and trimpot by showing their live status/voltages. Only available through Thonny or other Python terminal.

## CircuitPython
Vibra-tricker is coded in CurcuitPython, a minimal selection of regular Python. CircuitPython is less advanced than MicroPython, but has the advantage of presenting the Pico as a removable USB storage device - i.e. easier for non-nerds. If you _are_ a nerd, it is possible to edit the code using [Thonny](https://thonny.org/) or similar.

## Raspberry Pi Pico
The vibra-trickler will work with any Raspberry Pi Pico/PicoH/PicoW/PicoWH. You could probably try a clone or variant of Raspberry Pi Pico, but be aware: 
1. Bad clones may not provide sufficient voltage to the vibrator, even at at maximum PWM setting.
1. The pinout/positions may be completely different than an 'original' _Raspberry Pi_ Pico.

It 'should' be possible to adopt code.py to run on some completely different micro computer, such as ESP32. Bear in mind that not all commands may work on standard MicroPython. Also, the PWM pin and 3xADC pins need to be adjusted.

## 3D printable parts
The [3D parts](./3D-parts) for this project are not required, but might help. If you don't have access to a 3D printer, you can probably make something up, similar to my first/trial ["home brew"](./media/DIY_hopper.jpg) hopper. It is, however, important to note the funnel/baffle arrangement to get a consistent powder flow. 

`Hopper-parts.stl` is ready to slice and print. `Hopper-parts.f3d` is for anyone wanting to make changes to the design using Fusion 360 CAD. `TCRT5000-blinder.stl` is an attempt to decrease the detection angle if using a TCRT5000 sensor.

## Small components
### Transistor (array)
The Pico GPIO pins are can not (at least _should not_ ) provide enough current to run a vibrator motor at ~75mA. It _can_ however provide a few milliamps through the 1kohm resistor to the BC547C transistor. The transistor then acts as an amplifier to let current flow from the high power `VBUS` pin, through the vibrator, to `GND`. 

`BC547C` looks small, but it can
- provide a _100mA current_ (when fully off/on),
- _switch fast_ enough between fully off/on from the Pico PWM changes,
- _amplify_ a fem milliamps to well above 100mA, thus keeping it out of the active (heat producing) range.

Carefully consider the above if trying to replace the transistor with another part! "Powerful" transistors may lack in speed and amplification. Other small signal transistors may lack in max current and amplification.

### Diode
When current drops fast (such as in PWM) through an inductive load (such as a motor), a higher voltage will 'bounce' back from the load. I honestly don't think this voltage spike could harm a Pico, but hey - a diode costs almost nothing. You could probably go with any 1N4### diode or similar, or skip it completely if you dare.

### Trim potentiometer
This components only acts as a voltage selector to feed an ADC (which then affects the PWM DC through Python code). I chose a multi-turn potentiometer because it needs to be quite precise. The resistance is probably _not_ critical - anywhere between 1k and 100k should work.

It's _technically_ possible to control the slow flow speed using only code. But tweaking the speed in code is not very _practical_. E.g. tweaking the trickling speed when changing powder types would require a PC and Thonny editor every time.

### Buttons 
Most buttons should work. Just make sure they are correctly oriented to open/close the circuit from Pico GPIO-pin to Pico GND.
