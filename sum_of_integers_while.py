# while.
def sum_of_int():
    try:    
        print("\nWrite only int numbers")
        first_input_number = int(input("First number: "))
        last_input_number = int(input("Last number: "))

        if (last_input_number == first_input_number):
            print("\nYour write wrong number. Try again!")
            sum_of_int()

        # create list.
        number_list = list(range(first_input_number, last_input_number+1))

        i = 0
        result = 0 
        while i < len(number_list):
            result += number_list[i]
            i += 1
        print("Result: " + str(result)) 
    except ValueError:
        print("\nYour write wrong number. Try again!")
        sum_of_int()

sum_of_int()