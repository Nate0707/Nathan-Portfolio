#Nathan Gonzalez
#10/15
#Name Generator

print ("Welcome to your Superhero name generator")
print ("Answer the question with the 1 or 2 as one being first option and 2 being the second option")
ans = input ("are you Smart(1) or Strong(2)?")
#first question
if ans == "1": 
    ans = input ("do you like to Climb(1) or Technology(2)?")
    if ans == "1":
        ans = input ("would you rather date Mary(1) Jane or the Wasp(2)?")
        if ans == "1":
            print ("you are Spider-Man")
        elif ans == "2":
            print ("you are Ant-Man")
        else:
            print ("restart")
    if ans == "2":
        ans = input ("are you Cocky(1) or Sad(2)?")
        if ans == "1":
            print ("you are Iorn-Man")
        elif ans == "2":
            print ("You are cyborg")
        else:
            print ("restart")

if ans == "2":
    ans = input ("Would you rather Be An Alien(1) or Have Magic(2)?")
    if ans == "1":
        ans = input ("Would you rather be a Tree(1) or be Kryptonian(2)?")
        if ans == "2":
            print ("You are Super-Man")
        elif ans == "1":
            print ("You are Groot")
        else:
            print ("restart")
    if ans == "2":
        ans = input ("would you rather Have Dark Magic(1) or Have Ligtning(2)?")
        if ans == "2":
            print ("You are Shazam")
        elif ans == "1":
            print ("You are Raven")
        else:
            print ("restart")


1
