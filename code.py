print('code.py starting...')
#Upload to /lib first!
#  ...\lib\adafruit_vl6180x.py
#  ...\lib\adafruit_bus_device\i2c_device.py


from time import sleep, time
import board
import busio
import pwmio
import digitalio
import adafruit_vl6180x

pwm_max = 60000 #(60000 --> 3,9V)
pwm_min = 6000  #(7000 --> Starts MOST times. 6000 --> Starts SOME times)
vl_far =  50    #millimeters distance when scale beam is down at bottom.
vl_near = 10    #millimeters distance when scale beam is up near target weight.

vl_scl =     board.GP27  #SCL for VL6180X on leg 32
vl_sda =     board.GP26  #SDA for VL6180X on leg 31
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

i2c = busio.I2C(vl_scl, vl_sda) #I2C bus for VL ToF sensor
vl = adafruit_vl6180x.VL6180X(i2c, offset=-0) #VL ToF sensor object

pwm = pwmio.PWMOut(vib_gp, frequency=1000, duty_cycle=0) #PWM output object for vib

# Short PWM burst with default/defined duty cycle and time period...
def pwm_burst(dc=32750, time_period=2):
    dc = int(dc) #No decimals
    if (dc < 0) or (dc > 65535): #Supported range
        print('FAIL! Duty cycle out of range (0...65535)')
    else:
        print('About to run PWM at', dc,'(out of 65535) for', time_period, 'seconds...')
        pwm.duty_cycle = dc
        sleep(time_period)
        pwm.duty_cycle = 0

# Scan for sensor on I2C bus...
def vl_scan():
    i2c.try_lock()
    print('Scanning I2C bus on', vl_scl, '/', vl_sda, '...')
    i2c_addresses = i2c.scan()
    if not i2c_addresses:
        print('I2C device not found!')
    for address in i2c_addresses:
        print("I2C device found. Dec:", address, "Hex:", hex(address)) #Convert to Hex and print
    i2c.unlock()

# Try getting a number of readings from sensor...
def vl_stats(n=50):
    seconds_start = time()
    array = []
    for counter in range(n):
        array.append(vl.range)
        print(vl.range)
    sorted_array = sorted(array)
    #print('Raw distances:\n',array)
    #print('Sorted distances:\n',sorted(array))
    print(n, 'readings in', (time() - seconds_start), 'seconds')
    print('Min:',sorted_array[0], 'Max:', sorted_array[-1], 'Median (kind of):', sorted_array[int(n/2)])

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
        sleep(0.3)

# Start trickling powder...
def trickle():
    should_run = False #Default --> Don't run before Start button
    while True:
        #sleep(0.5)
        distance = vl.range
        if distance <= vl_near: #Beam near --> Don't run
            should_run = False
            led.value = False #LED off to indicate button press
        elif not btn_stop.value: #Stop button --> Don't run
            should_run = False
            led.value = False #LED off to indicate button press
        elif not btn_start.value: #Start button --> run
            should_run = True
            led.value = False #LED off to indicate button press
        else:
            led.value = not led.value #LED flicker to indicate activity
        #Calculate PWM DC inversely proportional to distance
        vl_fraction = (distance - vl_near) / (vl_far - vl_near)
        dc = vl_fraction * (pwm_max - pwm_min) + pwm_min
        #Remove decimals and limit PWM to acceptable range
        dc = int(dc)
        if dc < pwm_min:
            dc = pwm_min
        if dc > pwm_max:
            dc = pwm_max
        print('Running:',should_run,' Distance',distance,'PWM DC',dc)
        if should_run:
            pwm.duty_cycle = dc
        else:
            pwm.duty_cycle = 0

trickle() #Auto-start trickling. Thonny/REPL console will interrupt this.
