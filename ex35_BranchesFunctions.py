# ex35 Branches and Functions

from sys import exit  # Not needed though

def gold_room():
    print "The room is full of gold. How much do you take?"

    try:
        how_much = int(raw_input("> "))
    except ValueError as v:
        print v
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "You aren't greedy. You win!"
        exit(0)
    else:
        dead("You greedy")

def bear_room():
    print "There is a bear here"
    print "The bear is infront of another door"
    print "How are you going to move the door?"

    bear_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "Take honey":
            dead("The bear looks at you and slaps")
        elif choice == "Taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now"
            bear_moved = True
        elif choice == "Taunt bear" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means"

def cthulu_room():
    print "You see the evil Cthulu"
    print "Do you flee or eat your head?"

    choice = raw_input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("That was tasty")
    else:
        cthulu_room()

def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room"
    print "There is door to your left and to your right"
    print "Which one do you take?"
    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulu_room()
    else:
        dead("You stumble around until you starve")

gold_room()
#start()
