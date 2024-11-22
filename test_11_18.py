from sys import exit

the_count = [1 ,2 , 3 ,4 , 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1 ,'pennies' , 2 ,'dimes' , 3 ,'quarters']

#this first kind of for-ioop goes through a list
for number in the_count:
    print(f"This is count {number}")

#same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

#also we can go through mixed lists too
#notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

#we can also build lists star with an empty one
elements = []
#then use the range function to do 0 to 5 counts
for i in range(0 ,6):
    print(f"Adding {i} to the list")
    #append is a function that lists understand
    elements.append(i)

#now we can print them out  too 
for i in elements:
    print(f"Element was:{i}")


#################################################

def gold_room():
    print("This room is full of gold. How much do you take?")
    choice = input(":>")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")
    if how_much < 50:
        print("Nice,you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print("There is a bear room.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False
    while True:
        choice = input(":>")
        if choice =="take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chewa your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it ,whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    choice = input(":>")
    if "flle" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why , "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to you right and left.")
    print("Which one do you take?")
    choice = input(":>")
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()
