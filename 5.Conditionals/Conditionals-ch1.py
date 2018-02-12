from mcpi.minecraft import Minecraft
mc = Minecraft.create()

"""This program should create a hole below Steve if a user answers yes to a user input that prompts them"""


"""Make an input that asks if you would like to make a crater"""

"""create an if statement that runs the nested code if the input answer is yes"""
    pos = mc.player.getPos()
    mc.setBlocks(pos.x + 1, pos.y + 1, pos.z + 1, pos.x - 1, pos.y - 1, pos.z - 1, 0)
    mc.postToChat("Boom!")

"""make another statement for if the answer is no"""
    mc.postToChat("ok")