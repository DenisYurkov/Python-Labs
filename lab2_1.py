import random

def lab2_1():
    try:
        random_number = random.randint(1, 100)
        i = 0
        while True:
            user_input = int(input("Write number: "))
            i += 1 

            if user_input == random_number:
                break
            if user_input > random_number:
                print("The planned number is less.")
            if user_input < random_number:
                print("The planned number is greater.")

        print("You guessed the number in " + str(i) + " tries.")
        print("You guessed right, the correct number is " + str(random_number) + ".")
    except ValueError:
        print("\nYour write wrong number. Try again!")
        lab2_1()

lab2_1()