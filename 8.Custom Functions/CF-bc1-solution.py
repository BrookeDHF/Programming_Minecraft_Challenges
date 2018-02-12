from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random


def randomBlockLocations(blockType, repeats):

    count = 0
    while count < repeats:
        x = random.randrange(-127, 128)
        z = random.randrange(-127, 128)
        y = mc.getHeight(x, z)
        mc.setBlock(x, y, z, blockType)
        count += 1

"""Function needs to be called"""

randomBlockLocations(103, 10)
randomBlockLocations(35, 37)
randomBlockLocations(57, 102)
