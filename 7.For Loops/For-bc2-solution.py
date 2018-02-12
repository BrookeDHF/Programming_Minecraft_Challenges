from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time


time.sleep(60)

"""the function to make a list of hits is pollBlockHits"""
blockHits = mc.events.pollBlockHits()

"""You have to use len() to get the length of the list"""
blockHitsLength = len(blockHits)
"""use str() to convert the len data to a string"""
mc.postToChat("Your score is " + str(blockHitsLength))