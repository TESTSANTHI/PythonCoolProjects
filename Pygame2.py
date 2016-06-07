import time
global gold 
global apples 
gold = 0
apples = 0 

def start():
    print ("hello and welcome!")
    name = input("What's your name: ")
    print ("welcome, " + name + "!")
    print ("The object of this game is to collect apples.")
    print ("After collecting the apples you sell them.")
    choice = input("Do you want to play? y/n")
    while choice != "y" or "n":
        if choice == "y":
            begin()
            break
        elif choice == "n":
            print ("Okay, bye...")
            break
        else:
            choice = input("please choose y/n")

def end():
    global gold 
    global apples
    if gold > 99:
        print("you payed your taxes and can live another day!")
    elif gold < 99:
         print("you couldn't pay your taxes so they broke your leg.")
    
    choice = input("Do you want to play again? y/n")
    if choice == "y":
        gold = 0
        apples = 0
        begin()
    elif choice == "n":
        print ("Okay, bye...")
    else:
        choice = input("please choose y/n")


def sell():
    global apples
    global gold
    sell = input("do you want to sell your apples? y/n")
    while sell != "y" or "n":
        if sell == "y":
            print("you have sold {} apples".format(apples))
            gold = apples * 10 
            apples = 0
            print("you now have {} gold".format(gold))
            end()
            break
        elif sell == "n":
            print ("your apples went bad sorry.")
            apples = 0
            print ("you have {} apples".format(apples))
            end()
            break
        else:
            sell = input("Please choose y/n")

def pick():
    global apples
    global gold
    pick = " "
    while pick != "y" or "no":
        pick = input ("Do you want to pick an apple? y/n")
        if pick == "y":
            time.sleep(1)
            print("you pick an apple!")
            apples = apples + 1
            print ("you currently have {} apples".format(apples))

        elif pick == "n":
            if apples > 0:                
                sell()
                break
            else:
                end()
        else:
            print("please choose y/n")

def begin():
    global apples
    global gold
    print ("Let's start!")
    pick()

start()
