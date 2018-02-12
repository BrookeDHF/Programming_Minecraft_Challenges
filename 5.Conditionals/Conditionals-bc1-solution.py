from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 10
y = 11
z = 12
"""set variable for diamond"""
diamond = 57

gift = mc.getBlock(x, y, z)
"""Checking if something doesn't equal 0 is !="""
if gift != 0:
    if gift == diamond:
        mc.setBlocks(5, -2, 5, 6, -1, 6, 0)
    else:
        mc.setBlocks(4, -3, 4, 7, -3, 4, 10)
else:
    mc.postToChat("Place an offering on the pedestal.")
