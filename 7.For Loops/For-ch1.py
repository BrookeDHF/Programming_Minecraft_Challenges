from mcpi.minecraft import Minecraft
mc = Minecraft.create()

"""Create a list that checks for diamonds in the 50 blocks below you"""

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

depth = 50
Diamond = 56


"""Make for loop for range in depth"""
    block = mc.getBlock(x, y - "depth list variable", z)
    """Create a conditional to break the loop and post to chat diamons were found. 
    Bonus points if they list the exact block."""

"""Create a conditional statement to post to chat that no daimonds are below you"""