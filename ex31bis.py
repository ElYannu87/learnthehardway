print("Are you ready to make some choices with python?")

choice = input("please enter your choice between 1 and 3: >")

if choice == "1":
    print("Well you took the easy road !")
    print("1 is clearly the first number on your keyboard")
    print("Now you have a decision to make")
    print("Choose 1. To erease your computer")
    print("Choose 2. To see what else will happen")

    decision = input("Your decision between 1 and 2: >")

    if decision == "1":
        print("You really like to live dangerously? Say bye bye to your computer")
    elif decision == "2":
        print("Got scared? Good! You just saved yourself!")
    else:
        print("Ha! aren't you a clever one ! thinking outside the box!")
        print("You just saved your ass")

elif choice == "2":
    print("Humm, you thought with a 2. you were save?")
    print("Gotcha ! I am encrypting your files!")

elif choice == "3":
    print("aha ! 3 the lucky number?")
    print("not so much :-(")
    print("Your PC is runnning very hot, don't you think so?")
    print("ON FIRE !")

else:
    print("You're really a smart one!")
    print("making your own choice!")
    print("welcome !")
