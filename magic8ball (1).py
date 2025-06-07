#Nathan Gonzalez
#1/29/25

# Magic 8 ball
import random
import time
Magic8list = ["It is certain","It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Dont count on it", "MY reply is no", "My source say no", "Outlook not so good", "Very doubtful"]

def ball8():
    print("welcome to magic 8 balll")
    while True:
        quest = input("ask me a yes or no question")
        if quest.endswith("?"):
            print("shake...")
            time.sleep(1.5)# makes it wait the amout you put in the ()
            print("shake...")
            time.sleep(1.5)
            print(random.choice(Magic8list))
            ask = input("do ou want to shak the 8 ball again?") # new variable
            if ask == "no":
                break
            else:
                print("Make sure it ends with a question mark")
                return ball() #retuns user back to start if they dont end with qestion mark

ball8()
