from mcpi.minecraft import Minecraft
mc = Minecraft.create()

"""Shorten this code using a custom function"""
"""Hint: You could also use a while loop to make it even more iterable for bonus points"""


pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

wood = 17
leaves = 89


"""tree 1"""
# trunk
mc.setBlocks(x, y, z, x, y + 5, z, wood)

# leaves
mc.setBlocks(x - 2, y + 6, z - 2, x + 2, y + 6, z + 2, leaves)
mc.setBlocks(x - 1, y + 7, z - 1, x + 1, y + 7, z + 1, leaves)

"""tree 2"""
# trunk
mc.setBlocks(x + 3, y, z + 3, x + 3, y + 5, z + 3, wood)

# leaves
mc.setBlocks(x + 1, y + 6, z + 1, x + 5, y + 6, z + 5, leaves)
mc.setBlocks(x + 2, y + 7, z + 2, x + 4, y + 7, z + 4, leaves)

"""tree 3"""
# trunk
mc.setBlocks(x + 7, y, z, x + 7, y + 5, z, wood)

# leaves
mc.setBlocks(x + 7 - 2, y + 6, z - 2, x + 7 + 2, y + 6, z + 2, leaves)
mc.setBlocks(x + 7 - 1, y + 7, z - 1, x + 7 + 1, y + 7, z + 1, leaves)


"""tree 4"""
# trunk
mc.setBlocks(x + 15, y, z + 8, x + 15, y + 5, z + 8, wood)

# leaves
mc.setBlocks(x + 15 - 2, y + 6, z + 8 - 2, x + 15 + 2, y + 6, z + 8 + 2, leaves)
mc.setBlocks(x + 15 - 1, y + 7, z + 8 - 1, x + 15 + 1, y + 7, z + 8 + 1, leaves)

"""repeat to add more trees"""
