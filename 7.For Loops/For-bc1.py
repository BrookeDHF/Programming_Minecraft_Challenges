from mcpi.minecraft import Minecraft
mc = Minecraft.create()

"""This script should make a tower of rainbow wool. Each block a different color than the last. 
Look at the console errors for hints """

RainbowList = [0, 1, 2, 3, 4, 5]
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

for color in Rainbowlist:
    mc.setBlock(x, y, z, wool)
    y + 1
