from mcpi.minecraft import Minecraft
mc = Minecraft.create()


RainbowList = [0, 1, 2, 3, 4, 5]
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

""" the L in RainbowList is not capitalized """
for color in Rainbowlist:
    """ missing the argument for the color, and wool is not defined """
    mc.setBlock(x, y, z, wool)
    """ should be y +=1 """
    y + 1
