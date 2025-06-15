import numpy

class PIDController:
    def __init__(self):
        self.P = 10
        self.I = .2
        self.D = 1

        self.BALANCE_POINT = 0

    def getOutput(self, pitchAngle):
        error = self.BALANCE_POINT - pitchAngle
        
        if (abs(error) <= 5):
            output = 0
        else:
            pMode = error * self.P
            output = numpy.tanh(pMode)


        return output