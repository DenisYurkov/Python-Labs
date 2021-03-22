def change_word():
    print("Write only letters, do not write symbols and numbers!")
    user_input = input("Write word(minimum 8 letters): ")
    check = user_input.isalpha()
    reverse = user_input[::-1]

    if check and len(user_input) >= 8:
        print("\nFirst three letters: " + user_input[0:3])
        print("2nd letter from the end: " + user_input[-2])
        print("Four letters from the end: " + user_input[-4:])
        print("Characters 2 to the penultimate one in reverse order: " + reverse[1:-1])
    else:
        print("Wrong input, please try again!\n")
        change_word()
change_word()