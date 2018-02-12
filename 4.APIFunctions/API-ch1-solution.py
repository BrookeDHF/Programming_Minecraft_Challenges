from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getPos()

x = pos.x
y = pos.y
z = pos.z

block = 1

mc.setBlocks(x,y,z, x + 5, y, z + 2,block)