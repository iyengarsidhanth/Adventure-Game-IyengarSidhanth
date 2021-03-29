print(
    "Welcome to the Police Chase,You using a motercycle and trying to get far away from the  cops and you have jewels from the jewelry.Try,to not get caught and Good Luck!!"
)

exit = "f"

engineFuel = 15
thirstLevel = 0
policeDistance = 1
energyLevel = 10

while (exit != 'q'):
    

    print(
      "If you want to leave the game press 'q' or to continue press any other key "
    )
    print("(A) rest")
    print("(B) Drink water")
    print("(C) full speed")
    print("(D) Check Stats")
    print("(E) moderate speed")
    exit = input("Enter your choice: ").lower()

    if (exit == "a"):
        print("You want to rest")
        energyLevel += 10
        print("You are now fully rested")
        policeDistance -= 1
        print("The cops are gaining on you!")
    elif (exit == "b"):
        print("You want to drink water")
        thirstLevel = 0
        policeDistance -= 1
        ("The cops are getting closer..")

    elif (exit == "c"):
            print("You want to  go full speed!")
            engineFuel -= 2
            policeDistance += 2
            thirstLevel += 2
            energyLevel -= 2
            print("You are more thirsty now.")

            print("You are more farther from the cops!")
    elif (exit == "d"):
        print("You want to Check Stats")
        print("The cops are " + str(policeDistance) + " miles behind. Your energy level is " + str(energyLevel)+" out of 10!\nYour Thirst level is "+ str(thirstLevel)+" out of 10")
    elif (exit == "e"):
        print("You want to go moderate speed")
        print("Your engine fuel has decreased a little")
        policeDistance += 1
        print("You are a little ahead of the cops")
        print("You are a bit more thirsty now.")
        energyLevel -= 1
        thirstLevel += 1
    elif (exit != "q"):
      print("Invalid Input.")
      print("What would you like to do")
    

    if (policeDistance >= 20):
        print("YOU DID IT! YOU WON!!")
        exit = "q"
    if (policeDistance <= 2):
        print("You better speed up, cops are coming close")

    if (policeDistance <= 0):
        print("Aww Shucks the police caught you.\nGame Over!")
      
    if (thirstLevel > 10):
      print("You became dehydrated and got unconsious. You wake up in handcuffs. \nGAME OVER!")
      exit = input("Would you like to play again? If you want to to quit, enter 'q':\n")
    elif (thirstLevel + 2 >= 10):
      print(("YOU ARE VERY THIRSTY! DRINK WATER!"))

    if ( energyLevel < 0):
      print("You became so tired that you fell asleep in your car. The cops caught up.\nGAME OVER!")
      exit = input("Would you like to play again? If you want to to quit, enter 'q':\n")
    elif ( energyLevel <= 3 ):
      print("YOUR TOO TIRED TO DRIVE!")
