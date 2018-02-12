from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()


x = pos.x
y = pos.y
z = pos.z

cobble = 4

"""Use setBlocks for multiple blocks"""

mc.setBlocks(x,y,z,x + 1, y + 10, z, cobble)