from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()

"""This program should make a brick house"""

x = pos.x
y = pos.y
z = pos.z

width = 10
height = 5
length = 6


cobble = 4
air = 0

mc.setBlocks(x,y,z, x + width, y + height, z + length, brick)
mc.setBlocks(x+1,y+1,z+1, x + width-1, y + height-1, z + length-1, air)
mc.setBlock(x+4,y+1,z, air)
mc.setBlock(x+4,y+2,z, air)
