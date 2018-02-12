import time

condition = 0


#this while loop adds one to the condition variable so it no longer meets the condition to run the loop again
#so the loop ends
while condition == 0:
    print("the variable 'condition' is equal to 0")
    condition += 5

print("the variable 'condition' is no longer equal to 0 so the loop is over")

time.sleep(5)

#this loop will run as long as the condition variable is not equal to 0
while condition != 0:
    print("the variable 'condition' is equal to " +str(condition))
    condition -= 1

print("the variable 'condition' is back to 0")

time.sleep(5)

#this loop will run forever or until you use break
while True:
    condition -= 1
    print("the variable 'condition' is equal to " +str(condition))
    if condition == -7:
        break

print("no more loop")