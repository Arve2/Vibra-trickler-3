print('code.py starting...')

# Imports:
import time
import board
import pwmio #For PWM output
import digitalio #For buttons
import analogio  #For analog sensors

# On-board LED:
led = digitalio.DigitalInOut(board.LED) 
led.direction = digitalio.Direction.OUTPUT

# Input from buttons:
btn_start = digitalio.DigitalInOut(board.GP4)  #Leg 6
btn_start.direction = digitalio.Direction.INPUT
btn_start.pull = digitalio.Pull.UP
btn_start_default = btn_start.value #Store default state at boot
def start_is_active(): #True if changed since boot
    return (btn_start.value != btn_start_default) 

btn_stop = digitalio.DigitalInOut(board.GP12) #Leg 16
btn_stop.direction = digitalio.Direction.INPUT
btn_stop.pull = digitalio.Pull.UP
btn_stop_default = btn_stop.value #Store default state at boot
def stop_is_active(): #True if changed since boot
    return (btn_stop.value != btn_stop_default) 

# Wait a few seconds for sensors to starta up and stabilize:
time.sleep(2) 

# Sensor settings:
one_adc_volt = 65536 / 3.3 #65536 ADC steps divided by system voltage.
sensor_detect_volts = 1.0 #Detect sensor deviations over/under this many volts from their value at boot.
sensor_detect_adc = int(one_adc_volt * sensor_detect_volts) #Convert volts to ADC values for coding.

# Sensor readings:
#  Sensors are considered active if the value has changed more than sensor_detect_volts since boot.
#  This logic allows for analog (0.0 to 3.3V) as well as digital (0.0 or 3.3V) sensors. It also allows for
#  both linear output (excitement --> low voltage) and reverse output (exceitement --> high voltage) sensors.
sens_low =  analogio.AnalogIn(board.A0) #Leg 31 for low position sensor
sens_low_at_boot = sens_low.value
def beam_is_low(): #True if sensor value is mostly unchanged since boot (beam still at bottom):
    unchanged = (sens_low_at_boot - sensor_detect_adc) < sens_low.value < (sens_low_at_boot + sensor_detect_adc)
    return unchanged

sens_high = analogio.AnalogIn(board.A1) #Leg 32 for high position sensor
sens_high_at_boot = sens_high.value
def beam_is_high(): #True if sensor value has changed since boot (beam has reached top):
    unchanged = (sens_high_at_boot - sensor_detect_adc) < sens_high.value < (sens_high_at_boot + sensor_detect_adc)
    return not unchanged

def beam_is_mid(): #True if neither sensor has been changed since boot.
    return (not beam_is_low()) and (not beam_is_high()) 


# Input from trim potentiometer between AGND@33 and ADC_VREF@35:
potentiometer = analogio.AnalogIn(board.A2) #Leg 34
def get_potentiometer_dc(): # Get PWM duty_cycle range minus potentiometer reading. I.e. Clockwise --> Higher speed.
    return 65535 - potentiometer.value

print(f"Boot values: Low sensor={(sens_low_at_boot / one_adc_volt):.2f}V / {sens_low_at_boot}ADC. High sensor={(sens_high_at_boot / one_adc_volt):.2f}V / {sens_high_at_boot}ADC. Trimpot PWM DC={get_potentiometer_dc()}ADC.")

# PWM for vibrator, and high-speed settings:
vib = pwmio.PWMOut(board.GP16) #Leg 21 for PWM output to vibrator transistor array
vib_dc_fast = 65535 #Maximum DC: An int in the range 0...65535. May need tweaking!

# Function for tweaking fixed PWM DC value, e.g. pwm_max. Attach a voltage meter over the vibrator and try different DC.
def try_vib_fast(dc=vib_dc_fast, time_period=2.0):
    print('About to run PWM at', dc,'for', time_period, 'seconds...')
    vib.duty_cycle = dc
    led.value = True
    time.sleep(time_period)
    vib.duty_cycle = 0
    led.value = False

# Function for tweaking adjustable PWM DC value with potentiometer. Turn the potentiometer to trickle faster/slower.
def try_vib_slow(time_period=10.0):
    led.value = True
    start_time = time.monotonic()
    while time.monotonic() < (start_time + time_period): #Run during time_period.
        print('Potentiometer reads',potentiometer.value,'so setting PWM DC to:',get_potentiometer_dc())
        vib.duty_cycle = get_potentiometer_dc()
        time.sleep(0.25)
    vib.duty_cycle = 0
    led.value = False

# Try input from buttons and sensors:
def try_inputs(time_period=15.0):
    start_time = time.monotonic()
    while time.monotonic() < (start_time + time_period): #Run during time_period.
        #Use "int(x)" below to get a table-like output with "1/0" instead of "True/False"
        print(f"Start btn: {int(start_is_active())}. Stop btn: {int(stop_is_active())}. Low sensor: {int(beam_is_low())}@{(sens_low.value / one_adc_volt):.2f}V. High sensor: {int(beam_is_high())}@{(sens_high.value / one_adc_volt):.2f}V. Trimpot PWM DC: {get_potentiometer_dc()}.")
        time.sleep(0.1)

def trickle():
    phase = 0 #Trickling phase (beam/speed). Default to 0 --> waits for start button
    iterations = 0 #Count iterations for stats
    start_time = time.monotonic() #Will be set again each time start is pressed.
    time_period = 60 #Time fuse (seconds). I.e. stop trickling if the kids need my attention and I leave the powder pan off for more than a minute!
    
    while True:
        time.sleep(0.05) #Slow down a bit. Otherwise ~300 iterations per second.
        iterations += 1 #Count iterations
                
        if start_is_active(): #Start button pressed
            led.value = False #Indicate button press
            if phase != 1: #First iteration in this phase:
                iterations = 1 #Reset counter
                start_time = time.monotonic()
                print('\n\n\nStarting at timestamp',start_time)
            phase = 1 #Change to first active phase
                
        elif stop_is_active(): #Stop button pressed
            led.value = False #Indicate button press
            if phase != 0: #First iteration in this phase:
                print('Stopping at timestamp',start_time)
            phase = 0 #Reset to phase 0
        else:
            led.value = not led.value #Flicker LED to indicate each cycle
        
        if (time.monotonic() - start_time) > time_period: #Don't run forever in case of neglect or errors
            if phase != 0: #First iteration in this phase:
                print(f"Stopping because time_period was exceeded at {int(time.monotonic() - start_time)}s / {iterations} iterations...")
            phase = 0
        
        if phase == 0: #If phase set to 0: Stop PWM and skip the rest of this iteration
            vib.duty_cycle = 0
            continue 
        
        if beam_is_low(): #Beam resting on bottom --> full speed!
            if phase == 1 and vib.duty_cycle == 0: #First iteration in this phase:
                print(f"Phase is 1, but PWM not yet started at 0 seconds / {iterations} iterations...")
            if phase == 1:
                vib.duty_cycle = vib_dc_fast
                
        elif beam_is_mid(): #Beam between bottom and top --> slow down to potentiometer adjusted speed!
            if phase < 2: #First iteration in this phase:
                if start_is_active():
                    print('Start button pressed while beam in phase 2.')
                else:
                    print('Letting beam settle before phase 2')
                    vib.duty_cycle = 0
                    time.sleep(1.5) #Wait a moment to let beam stabilize
                print(f"Starting phase 2 at {int(time.monotonic() - start_time)}s / {iterations} iterations...")
                phase = 2
            if phase == 2:
                vib.duty_cycle = get_potentiometer_dc()
                
        elif beam_is_high(): #Beam up at top --> powder throw complete.
            if phase > 0: #First iteration in this phase:
                print(f"Done! Resetting to phase 0 at {int(time.monotonic() - start_time)}s / {iterations} iterations...")
                phase = 0
            if phase == 0:
                vib.duty_cycle = 0
            
trickle() #Auto-start trickling. Thonny/REPL console will interrupt this to enable editing.
