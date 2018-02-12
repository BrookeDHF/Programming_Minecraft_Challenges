from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random
"""This script should put random blocks in a range around the player"""

def randomBlockLocations(blockType, repeats):

    count = 0
    while count < repeats:
        x = random.randrange(-127, 128)
        z = random.randrange(-127, 128)
        y = mc.getHeight(x, z)
        mc.setBlock(x, y, z, blockType)
        count += 1
