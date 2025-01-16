#nathan gonzalez
#10/29

#99 bottles
def bottles():
    milk = 99 #variable
    print(str(milk) + " bottles of milk on the wall")
    for i in range(98): #loop
        milk = milk - 1
        print(str(milk) + " bottles of milk on the wall " + "take one down, pass it around")
    if milk == 1:
        print("No more bottles of milk on the wall. Boohoo!")
bottles()

