from gpiozero import Motor

class MotorController:
    def __init__(self):
        self.motor = Motor(forward=16, backward=20, enable=21)

    def forward(self, power):
        self.motor.forward(power)

    def backward(self, power):
        self.motor.backward(power)

    def stop(self):
        self.motor.stop()
        
    def getSpeed(self):
        return self.motor.value