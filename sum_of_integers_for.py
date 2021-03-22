# for.
def sum_of_int():
    try:    
        print("\nWrite only int numbers")
        first_input_number = int(input("First number: "))
        last_input_number = int(input("Last number: "))
        
        # create list.
        number_list = list(range(first_input_number, last_input_number+1))

        if number_list!=None:
            print("Result: " + str(sum(i for i in number_list)) + "!")
    except ValueError:
        print("\nYour write wrong number. Try again!")
        sum_of_int()
sum_of_int()