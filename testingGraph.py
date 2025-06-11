import matplotlib.pyplot as plt
import matplotlib.animation as animation
from gyro import Gyro
import math

fig, ax = plt.subplots()


sensor = Gyro()
x, y = [], []
time = 0

def animate(i):
    global time
    time += 1
    x.append(time)

    # calculate angle
    roll = math.atan2(sensor.getAccel("y"), math.sqrt(math.pow(sensor.getAccel("x"), 2) + math.pow(sensor.getAccel("z"), 2))) * 180 / math.pi
    pitch = math.atan2(-sensor.getAccel("x"), math.sqrt(math.pow(sensor.getAccel("y"), 2) + math.pow(sensor.getAccel("z"), 2))) * 180 / math.pi

    yData = sensor.getAccel("x")
    y.append(yData)
    print(yData)

    ax.clear()
    ax.plot(x,y)
    ax.set_ylim(-100, 100)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()