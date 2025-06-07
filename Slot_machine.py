#Nathan Gonzalez
#1/28/25
#Slot Machine

#Initalize
import random
slot_symbols = [ "☃", "☔", "7","☃", "☔" ]
credit = 100
print(slot_symbols)
#Function
def slot_machine():
    global slot_symbols
    global credit
    print("Welcome to Slot Machine these are your symbols")

    while True:

        option = input("would you like to spin or quit?")
        if credit > 0:
            if option == "spin":
                print( "Machine is spinning...")
                credit = credit - 1
                print("you now have "+ str(credit)+ " credits")# linking multiple strings

                slot1 = random.choice(slot_symbols)
                slot2 = random.choice(slot_symbols)
                slot3 = random.choice(slot_symbols)

                print(slot1)
                print(slot2)
                print(slot3)

                if slot1 == "7" and slot2 == "7" and slot3 == "7":
                    print("there is a match, JACKPOT YOU WON 10 CREDITS!!!")
                    credit = credit + 10
                    print("you now have"+ str(credit) + "credits")

                elif slot1 == slot2 and slot2 == slot3:
                    print("there is a match, YOU WON 5 CREDITS!!")
                    credit = credit + 5
                    print("you now have"+ str(credit) + "credits")
                elif slot1 == slot2:
                    print("you won 2 credits")
                    credit = credit + 2
                elif slot2 == slot3:
                    print("you won 2 credits")
                    credit = credit + 2
                elif slot1 == slot3:
                    print("you won 2 credits")
                    credit = credit + 2

                else:
                    print(" you lost, play again :)")
                if credit == "0":
                    print(" you lost no more credits :(")

            else:
                print("you quit")
                break
        else:
            print("You have no more credits, go get some more")
#Main
slot_machine()
#1.Introduction
#2.Ask player if they'd like to spin or quit
#3.Randomly pull three symbols from oue list
#Advice: Make sure to remmember these three symbols(VARIABLE)
#4.Dispay the three symbols
#5.Determine the outcome (Jackpot, Match, Loss)(IF ELIF ELSE)


#Expansion
#Add Credit system
#Start the player with 100
#every spin subtract 1 credits
#Jackpot (10x)
#Match (3-5x)
#2 of a kind(2x)
#loss (Nothing)
