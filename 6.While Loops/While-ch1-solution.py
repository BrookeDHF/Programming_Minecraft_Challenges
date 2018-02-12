from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time



x = 6
y = 12
z = 80

countdown = 0

while countdown  < 10:
    print(countdown)
    countdown -= 1
    time.sleep(1)

