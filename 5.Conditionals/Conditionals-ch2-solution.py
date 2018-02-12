from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

home = (24,73,8)
apple_count = 0

while True:
    apple_count += 1
    time.sleep(1)
    print(apple_count)
    if apple_count == 7:
        mc.player.setTilePos(home)
        break


