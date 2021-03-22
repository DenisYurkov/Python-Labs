import random

def lab2_2():
    i = 0
    b = 0
    random_list = []
    user_number_list = []
    
    try:
        while True:
            user_input = int(input("Enter a number from 1 to 49: "))
            user_number_list.append(user_input)
            
            random_number = random.randint(1, 49)
            random_list.append(random_number)

            i += 1
            if i == 6:
                break
        print("\n---------------Result-------------------------")
        print("Random list numbers: " + str(random_list))
        print("User list numbers: " + str(user_number_list))
        
        for x in random_list:
            if x in user_number_list:
                b += 1
        print("You guessed " + str(b) + " numbers.")
    
    except ValueError:
        print("\nYour write wrong number. Try again!")
        lab2_2()
lab2_2()