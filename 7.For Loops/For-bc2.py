from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

"""this code should count the blocks you hit then list your score"""

time.sleep(60)


blockHits = mc.events.blockHits()


blockHitsLength = blockHits
mc.postToChat("Your score is " + blockHitsLength)