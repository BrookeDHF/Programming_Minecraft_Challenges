from mcpi.minecraft import Minecraft
"""Make sure M in minecraft is capitalized because it is referencing the 
import Minecraft, and make sure create has () because it is a function"""
mc = Minecraft.create()

"""Time needs to be imported to use time.sleep"""
import time

"""Make sure you have quotation marks around the string"""
mc.postToChat("Welcome to my home")
time.sleep(1)
"""If you use an apostraphy for ownership or contraction like can't you 
have to use quotation marks around the string and if you are doing """
mc.postToChat("My name's liz!")
