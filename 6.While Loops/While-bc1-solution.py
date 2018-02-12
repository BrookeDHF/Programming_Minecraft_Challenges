from mcpi.minecraft import Minecraft
mc = Minecraft.create()
"""time needs to be imported"""
import time

pos = mc.player.getTilePos()
floorX = pos.x - 2
floorY = pos.y - 1
floorZ = pos.z - 2
width = 10
length = 10
block = 57
"""setBlock should be setBlocks"""
mc.setBlocks(floorX, floorY, floorZ, floorX + width, floorY, floorZ + length, block)

while floorX <= pos.x <= floorX + width and floorZ <= pos.z <= floorZ + length:
    if block == 57:
        block = 22
    else:
        block = 57
    mc.setBlocks(floorX, floorY, floorZ,
            floorX + width, floorY, floorZ + length, block)
    """player position needs to be checked in the while loop or it will only only use the initial position/
     where the player was when the code was first run"""
    pos = mc.player.getTilePos()
    time.sleep(0.1)