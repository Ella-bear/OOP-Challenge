from pet import Pet

# Create a pet object
my_pet = Pet(name="Meowmeow")  

while True:
    print("\nWhat would you like to do?")
    print("1. Feed your pet")
    print("2. Let your pet sleep")
    print("3. Play with your pet")
    print("4. Check pet status")
    print("5. Teach a new trick")
    print("6. Show learned tricks")
    print("7. Exit")

    choice = input("Enter a choice (1–7): ")

    if choice == "1":
        my_pet.eat()
    elif choice == "2":
        my_pet.sleep()
    elif choice == "3":
        my_pet.play()
    elif choice == "4":
        my_pet.get_status()
    elif choice == "5":
        trick = input("Enter a trick to teach: ")
        my_pet.train(trick)
    elif choice == "6":
        my_pet.show_tricks()
    elif choice == "7":
        print("Bye!")
        break
    else:
        print("Invalid input. Try again.")
