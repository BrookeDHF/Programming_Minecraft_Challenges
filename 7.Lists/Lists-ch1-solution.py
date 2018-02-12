from mcpi.minecraft import Minecraft
mc = Minecraft.create()

sandwich_list = ["bread", "bacon", "lettuce", "tomato", "bread"]
ingredients = 5

mc.postToChat("How do you make your favorite sandwich?")

while ingredients >= len(sandwich_list):
    mc.postToChat(sandwich_list[0])
    mc.postToChat(sandwich_list[1])
    mc.postToChat(sandwich_list[2])
    mc.postToChat(sandwich_list[3])
    mc.postToChat(sandwich_list[4])

    ingredients -= 1