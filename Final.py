#Nathan
#1/15/25

#initialization
#urban stunt racer

#functions
print("Wlecome, are you ready to be a stunt race driver?")
print("you will choose your preferance of car and gass to see if you will get aressted")
def stunt_racer():
    car = input("please enter lambo or mustang being used")

    gas = input("please enter if you want gas full or half when pressing the pedal for gass")


    if car == "lambo" and gas == "full":
        print("you are going 250 miles per hour")
    speed = input("please enter what speed you are going in MPH")
    if car == "lambo" and gas == "half":
        print("you are going 125 miles an hour")
    if car == "mustang" and gas == "full":
        print("you are going 300 miles an hour")
    if car == "mustang" and gas == "half":
        print("you are going 150 miles an hour")
    if speed <= "150":
        print("you are not going over the speed limit")
    if speed > "150":
        print("you are now getting pulled over, you are going over the speed limit")
    for i in range(4):
        print("you are aressted")

#main
stunt_racer()



#Variables: A variable holds the value with a set name

#Loops: A loop is used to repeat what you choose to be the command and you can pic the amount of times to repeat

#Conditionals: are comparison and logical operator statments that can determain the condition of the variable
