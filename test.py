import time
from adafruit_crickit import crickit

motor = crickit.dc_motor_1

motor.throttle = 1.0
time.sleep(2)
motor.throttle = 0

motor.throttle = -1.0
time.sleep(2)
motor.throttle = 0
