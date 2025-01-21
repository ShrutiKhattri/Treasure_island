print("Welcome to the Treasure Island Game!")
print("Your mission is to find treasure by choosing the right choices, All the best Adventurer :)")
print("While travelling inside a forest, you came across a crossroad.")
way = input("Which path will you choose? left or right : ")
if way == "left" :
    print("You headed to the left route and reached a lake...")
    print("Once you reached the lake. Either you can swim or wait for the boat to come")
    opt = input("What will you do? swim or wait : ")
    if opt == "wait":
        print("A boat has arrived and you onboarded on it.")
        print("The boat departed within a few minutes and drop you to a port nearby.")
        print("After reaching the port you saw a house with three doors")
        print("There is a red door, a blue door and a yellow door.")
        door = input("Which one will you choose?")
        if door == "red":
            print("This room is full of flames!")
            print("Now you are a fried Turkey. So close buddy. Game over.")
        elif door == "blue":
            print("This room consists of poisonous gas!")
            print("You inhaled it and died in an instant. Game over buddy")
        elif door == "yellow":
            print("You found the Treasure!!!, Congrats you won the Game !")
    elif opt == "swim":
        print("The lake had alligators, and now they are dining on you")
        print("Game over buddy. Until next time.")

elif way == "right":
    print("You followed the road in fog and fell off the cliff")
    print("Game over buddy.")
