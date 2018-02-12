from mcpi.minecraft import Minecraft
mc = Minecraft.create()

"""This program should take a user input generated number and apply it to the function below to create a block"""


"""User input code goes here"""
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

mc.setBlock(x, y, z, """user input variable goes here""")
