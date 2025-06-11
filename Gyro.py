from mpu6050 import mpu6050
import time
import math

class Gyro:
    def __init__(self):
        self.sensor = mpu6050(0x68)

        self.A_offset_x = .124
        self.A_offset_y = .033
        self.A_offset_z = -.545

    def getAccelX(self):
        return self.sensor.get_accel_data()["x"] - self.A_offset_x

    def getAccelY(self):
        return self.sensor.get_accel_data()["y"] - self.A_offset_y

    def getAccelZ(self):
        return self.sensor.get_accel_data()["z"] - self.A_offset_z

    def getPitchAngle(self):
        return math.atan2(-self.getAccelX(), math.sqrt(math.pow(self.getAccelY(), 2) + math.pow(self.getAccelZ(), 2))) * 180 / math.pi

# i = Gyro()
# while True:
#     #print(i.getAccelZ(), "\t\t\t", i.getAccelX(), "\t\t\t", i.getAccelY())
#     print(i.getPitchAngle())
#     time.sleep(0.5)