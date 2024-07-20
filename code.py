print('code.py starting...')
#Upload to /lib first!
#  ...\lib\adafruit_vl6180x.py
#  ...\lib\adafruit_bus_device\i2c_device.py


from time import sleep
import board
import busio
import pwmio
import digitalio
import adafruit_vl6180x

vl_scl = board.GP27 #SCL pin for VL6180X on leg 32
vl_sda = board.GP26 #SDA pin for VL6180X on leg 31
vib_gp = board.GP16 #PWM pin to vibrator (transistor array) on leg 21

led = digitalio.DigitalInOut(board.LED) #On-board LED
led.direction = digitalio.Direction.OUTPUT

i2c = busio.I2C(vl_scl, vl_sda) #I2C bus for VL ToF sensor
vl = adafruit_vl6180x.VL6180X(i2c, offset=-10) #VL ToF sensor object

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

# @ToDo: Start trickling powder...
def trickle():
    while True: #Read range and blink LED
        print(vl.range)
        led.value = not led.value #Toggle on/off to indicate activity
        sleep(0.1)
