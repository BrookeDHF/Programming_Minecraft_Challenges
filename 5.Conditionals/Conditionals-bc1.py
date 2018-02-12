from mcpi.minecraft import Minecraft
mc = Minecraft.create()

"""This code should create an opening if a specific block is set at the x,y,z"""

x = 10
y = 11
z = 12

gift = mc.getBlock(x, y, z)
if gift does not = 0:
    if gift = diamond:
        mc.setBlocks(5, -2, 5, 6, -1, 6, 0)
    else:
        mc.setBlocks(4, -3, 4, 7, -3, 4, 10)
else:
    mc.postToChat("Place an offering on the pedestal.")