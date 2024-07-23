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

pwm_max = 60000 # (60000 --> 3,9V)
pwm_min = 6000 # (7000 --> Starts MOST times. 6000 --> Starts SOME times)
vl_far = 50 #millimeters. Scale beam down at bottom.
vl_near = 10 #millimeters. Scale beam up near target weight.

vl_scl = board.GP27 #SCL pin for VL6180X on leg 32
vl_sda = board.GP26 #SDA pin for VL6180X on leg 31
vib_gp = board.GP16 #PWM pin to vibrator (transistor array) on leg 21

led = digitalio.DigitalInOut(board.LED) #On-board LED
led.direction = digitalio.Direction.OUTPUT

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
    print('Time spent:', (time() - seconds_start), 'seconds')
    print('Median (kinda):', sorted_array[int(n/2)])
    print('Min:',sorted_array[0], 'Max:', sorted_array[-1])

# Start trickling powder...
def trickle():
    should_run = True
    while True:
        #sleep(0.5)
        led.value = not led.value #Toggle on/off to indicate activity
        distance = vl.range
        #Stop trickling if target weight is achieved
        if distance <= vl_near:
            should_run = False
        #Calculate PWM DC inversely proportional to distance
        vl_fraction = (distance - vl_near) / (vl_far - vl_near)
        dc = vl_fraction * (pwm_max - pwm_min) + pwm_min
        #Remove decimals and verify PWM range
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
#         if distance > vl_far:
#             pwm_dc = pwm_max
#             print(distance, ' > ', vl_far, 'vl_fraction is', vl_fraction,'DC should be', pwm_dc)
#         elif distance > vl_near:
#             #LOGIX!
#             pwm_dc = 20000
#             print(distance, ' > ', vl_near, 'vl_fraction is', vl_fraction,'DC should be', pwm_dc)
#         elif distance <= vl_near:
#             should_run = False #STOP trickling
#             pwm_dc = 0
#             print(distance, ' <= ', vl_near, 'vl_fraction is', vl_fraction,'DC should be', pwm_dc)

            