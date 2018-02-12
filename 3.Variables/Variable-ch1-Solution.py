from mcpi.minecraft import Minecraft
mc = Minecraft.create()

"""Use variable to reply with a user inputed block type"""

blockType = int(input("Enter a block type: "))
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

mc.setBlock(x, y, z, blockType)
