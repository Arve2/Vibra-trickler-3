print('code.py starting...')
#Upload to /lib first!
#  ...\lib\adafruit_vl6180x.py
#  ...\lib\adafruit_bus_device\i2c_device.py


import time
import board
import busio
import pwmio
import digitalio
import adafruit_vl6180x

pwm_min =       7000  #Minimum DC, required to run vib. (7000 --> Starts MOST times. 6000 --> Starts SOME times)
pwm_approach =  10000 #Maximum DC, when approaching target weight.
pwm_max =       60000 #Maximum DC. (60000 --> 3,9V)
tof_near =      15.0   #Distance (mm) when scale beam is up near target weight.
tof_approach =  26.0  #Distance (mm) when scale beam is approaching target weight. I.e. just lifted by "approach to weight" spring.
#tof_far = 255 #Distance (mm) before approaching target weight.

tof_scl =    board.GP27  #SCL for ToF sensor on leg 32
tof_sda =    board.GP26  #SDA for ToF sensor on leg 31
pin_start =  board.GP4   #Start button on leg 6
pin_stop =   board.GP8   #Stop button on leg 11
pin_manual = board.GP12  #Manual run button on leg 16
vib_gp =     board.GP16  #PWM pin to vibrator (transistor array) on leg 21

led = digitalio.DigitalInOut(board.LED) #On-board LED
led.direction = digitalio.Direction.OUTPUT

btn_start = digitalio.DigitalInOut(pin_start) #Start button
btn_stop = digitalio.DigitalInOut(pin_stop) #Stop button
btn_manual = digitalio.DigitalInOut(pin_manual) #Manual run button. Not implemented (yet)
for btn in (btn_start, btn_stop, btn_manual):
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP #Default to high. Pushing button --> GND --> Low.

i2c = busio.I2C(tof_scl, tof_sda) #I2C bus for ToF sensor
tof = adafruit_vl6180x.VL6180X(i2c, offset=-0) #ToF sensor object

pwm = pwmio.PWMOut(vib_gp, frequency=1000, duty_cycle=0) #PWM output object for vib

# Short PWM burst with default/defined duty cycle and time period...
def pwm_burst(dc=32750, time_period=2.0):
    dc = int(dc) #No decimals
    if (dc < 0) or (dc > 65535): #Supported range
        print('FAIL! Duty cycle out of range (0...65535)')
    else:
        print('About to run PWM at', dc,'(out of 65535) for', time_period, 'seconds...')
        pwm.duty_cycle = dc
        time.sleep(time_period)
        pwm.duty_cycle = 0

# Scan for sensor on the I2C bus...
def tof_scan():
    i2c.try_lock()
    print('Scanning I2C bus on', tof_scl, '/', tof_sda, '...')
    i2c_addresses = i2c.scan()
    if not i2c_addresses:
        print('I2C device not found!')
    for address in i2c_addresses:
        print("I2C device found. Dec:", address, "Hex:", hex(address)) #Convert to Hex and print
    i2c.unlock()

# Get a number of readings from sensor...
#@Todo: Count in MILLI-seconds!
def tof_stats(n=80): #80 readings ~ 1.0s when no print()
    time_start = time.monotonic()
    array = []
    for counter in range(n):
        array.append(tof.range)
    sorted_array = sorted(array)
    average = sum(array) / len(array)
    print('Readings in order of distance:',sorted_array)
    print(n, 'readings in', round((time.monotonic() - time_start),2), 'seconds')
    print('Min:',sorted_array[0], 'Max:', sorted_array[-1],'Average: {0:.2f}'.format(average), 'Median (kind of):', sorted_array[int(n/2)])

# Test buttons...
def btn_test():
    while True:
        digit_start = int(not btn_start.value) #Convert Pressed/Low/False to 1
        digit_stop = int(not btn_stop.value)
        digit_manual = int(not btn_manual.value)
        print('Start button:', digit_start, '  Stop button:', digit_stop, '  Manual button:', digit_manual)
        if 1 in (digit_start, digit_stop, digit_manual): #Shine onboard LED i any button is pressed
            led.value = True 
        else:
            led.value = False
        time.sleep(0.3)

# Start trickling powder...
def trickle():
    smoothing_array = [100,100,100]
    should_run = False #Wait for start button before running
    last_distance = 0
    phase = 1
    
    while True:
        #sleep(0.5)
        
        #Check button input first...
        if not btn_stop.value: #Stop button --> Don't run
            should_run = False
            pwm.duty_cycle = 0
            led.value = False #LED off to indicate button down
        elif not btn_start.value: #Start button --> Run
            should_run = True
            last_distance = 999
            phase = 1
            led.value = False #LED off to indicate button down
        else:
            led.value = not led.value #LED flicker to indicate activity/iteration
            
        #ToF distance to PWM DC logic...
        smoothing_array.append(tof.range)
        smoothing_array.pop(0)
        distance = sum(smoothing_array) / len(smoothing_array)
        
        if distance >= last_distance:
            continue
        else:
            last_distance = distance
        
        if distance <= tof_near or phase == 3: #Phase 3: Beam near --> Stop running...
            should_run = False
            phase = 3
            led.value = False #LED off to indicate stop
        elif distance <= tof_approach or phase == 2: #Phase 2: Beam approaching target --> Decrease DC...
            if phase != 2: #First iteration in phase 2 --> Give the beam some rest
                print('Starting phase 2')
                pwm.duty_cycle = 0
                time.sleep(1.5)
            phase = 2
            #Calculate DC inversely proportional to distance, and in acceptable range...
            tof_fraction = (distance - tof_near) / (tof_approach - tof_near)
            dc = tof_fraction * (pwm_approach - pwm_min) + pwm_min
            dc = int(dc)
            if dc < pwm_min:
                dc = pwm_min #Never less than Min.
            if dc > pwm_approach:
                dc = pwm_approach #Never more than Max. (Probably superflous.)
            #should_run = False #############################################################
        else: #Phase 1: Beam down, not yet approaching target --> Max DC
            phase = 1
            dc = pwm_max

        #Control PWM DC...
        if should_run:
            pwm.duty_cycle = dc
        else:
            pwm.duty_cycle = 0
        
        #Console output - this steals a lot of time!
        print('Running:',int(should_run),' Distance: {0:.2f}'.format(distance),'Phase:',phase,'PWM DC:',dc)
        

trickle() #Auto-start trickling. Thonny/REPL console will interrupt this to enable editing.
