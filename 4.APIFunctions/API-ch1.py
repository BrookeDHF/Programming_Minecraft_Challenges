from mcpi.minecraft import Minecraft
mc = Minecraft.create()

"""Create a short program making a compass to orient yourself"""

pos = mc.player.getPos()

"""set variables to set x,y, and z to player position"""

"""Set a variable for the blocks you want to use for your compass"""

mc.setBlocks(x,y,z, x, y, z, """block variable""")


"""how might you add to the ending x,y,z argument so you can tell the orientation of x vs z?"""