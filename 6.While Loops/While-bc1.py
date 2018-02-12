from mcip.minecraft import Minecraft
mc = Minecraft.create()

"""This should create a dancefloor under the player but it is not working for some reason. 
Look through the code for mistakes and get hints from the errors in the"""

pos = mc.player.getTilePos()
floorX = pos.x - 2
floorY = pos.y - 1
floorZ = pos.z - 2
width = 10
length = 10
block = 57

mc.setBlock(floorX, floorY, floorZ, floorX + width, floorY, floorZ + length, block)

pos = mc.player.getTilePos()

while floorX <= pos.x <= floorX + width and floorZ <= pos.z <= floorZ + length:
    if block == 57:
        block = 22
    else:
        block = 57
    mc.setBlocks(floorX, floorY, floorZ, floorX + width, floorY, floorZ + length, block)
    time.sleep(0.1)