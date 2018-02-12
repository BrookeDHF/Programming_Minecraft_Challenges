from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()

"""shorten the code"""

x = pos.x
y = pos.y
z = pos.z

cobble = 4

mc.setBlock(x,y,z, cobble)
mc.setBlock(x,y + 1,z, cobble)
mc.setBlock(x,y + 2,z, cobble)
mc.setBlock(x,y + 3,z, cobble)
mc.setBlock(x,y + 4,z, cobble)
mc.setBlock(x,y + 5,z, cobble)
mc.setBlock(x,y + 6,z, cobble)
mc.setBlock(x,y + 7,z, cobble)
mc.setBlock(x,y + 8,z, cobble)
mc.setBlock(x,y + 9,z, cobble)
mc.setBlock(x,y + 10,z, cobble)
mc.setBlock(x + 1,y,z, cobble)
mc.setBlock(x + 1,y + 1,z, cobble)
mc.setBlock(x + 1,y + 2,z, cobble)
mc.setBlock(x + 1,y + 3,z, cobble)
mc.setBlock(x + 1,y + 4,z, cobble)
mc.setBlock(x + 1,y + 5,z, cobble)
mc.setBlock(x + 1,y + 6,z, cobble)
mc.setBlock(x + 1,y + 7,z, cobble)
mc.setBlock(x + 1,y + 8,z, cobble)
mc.setBlock(x + 1,y + 9,z, cobble)
mc.setBlock(x + 1,y + 10,z, cobble)
