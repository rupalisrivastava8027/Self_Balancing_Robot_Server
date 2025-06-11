import Gyro
from MotorController import MotorController
import time
import numpy
import math
motor = MotorController()
Gyro = Gyro.Gyro()
	
global BALANCEPOINT, Kp, Ki, Kd, integral, prev_err

BALANCEPOINT = 0.0
Kp = 10
Ki = 0.2
Kd = 2
integral = 0
prev_err = 0

def controlSignal():
    global integral, prev_err

    error = BALANCEPOINT - Gyro.getPitchAngle()

    pMode = error * Kp

    # integral += error
    # iMode = integral * Ki

    # derivative = error - prev_err
    # dMode = derivative * Kd

    if error <= 5 and error >= 0:
        output = 0

    else: 
        output = numpy.tanh(pMode)

    if output > 1:
        output = 1

    elif output < -1:
        output = -1

    prev_err = error

    return output

try:
    while (True):
        signal = controlSignal()


        print(signal)
        if (signal == 0):
            motor.stop()
        if (signal < 0):
            motor.forward(abs(signal))
        if (signal > 0):
           motor.backward(signal)
        
        # time.sleep(.15)


except KeyboardInterrupt:
    print("Stopping Motors and exiting")
    motor.stop()