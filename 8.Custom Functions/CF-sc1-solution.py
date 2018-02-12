from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random

def growTree(x, y, z):
    wood = 17
    leaves = 89


    # trunk
    mc.setBlocks(x, y, z, x, y + 5, z, wood)

    # leaves
    mc.setBlocks(x - 2, y + 6, z - 2, x + 2, y + 6, z + 2, leaves)
    mc.setBlocks(x - 1, y + 7, z - 1, x + 1, y + 7, z + 1, leaves)

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

tree_count = 0

while tree_count < 20:
    disx = random.randint(1, 50)
    disz = random.randint(1, 50)

    growTree(x + disx, y, z + disz)
    tree_count += 1

