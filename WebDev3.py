print("You are off on your space mission. You've just taken off and left the Earth's atmosphere.The goal of this mission is to try to find life in the universe Where do you go?")
userInput = input("Enter A or B. A) Head towards Mars B) Head into empty space")

if userInput == 'A':
    print("You've set the spaceship's course for Mars. You approach, you see the red planet your crew prepares the rover for landing.")
    
    userInput_Mars = input("Where do you want to land on Mars? 1) North pole  2) Valles a vast canyon")
    
    if userInput_Mars == '1':
        print("You've chosen to land to the north pole. You explore the area, you find intriguing Ice that hint that mars possibly has life?")
    
    elif userInput_Mars == '2':
        print("You navigate the ship to land near the Valles As you explore yhhh you find evidence of dead aliens. The search for life on Mars becomes more intreging")
    
    else:
        print(" wrong. Please restart.")
    
elif userInput == 'B':
    print("You decide to venture into the unknown. As you head into empty space, you and your crew witness the views of stars and galaxies")
    
    userInput_Space = input("You detect a signal. What do you do? 1) Follow the signal 2) Continue where your going")
    
    if userInput_Space == '1':
        print("You decide to follow the signal. You approach, you discover a unknown alien space station.")
    
    elif userInput_Space == '2':
        print("You choose to stay put you continue your mission.")
    
    else:
        print(" Done. Please restart. ")
    
