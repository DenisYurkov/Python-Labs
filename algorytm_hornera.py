import colorama

def horner():
    colorama.init()
    try:
        print(colorama.Fore.YELLOW)
        print("-------------------Program for determining a function at a point using Horner's algorithm.------------------------------")
        print("-------------------------------------Made by Denis Yurkov.--------------------------------------------------------------\n")

        print(colorama.Fore.GREEN)
        x = int(input("f(x): Write number x: "))
        num = list()
        
        print(colorama.Fore.BLUE)
        p = int(input("Enter the maximum degree: "))


        if p<0:
            print(colorama.Fore.RED)
            print("You cannot enter negative degrees, try again!")
            horner()
            
        i = p
        y = i-1
        while True:
            print(colorama.Style.BRIGHT)
            print(colorama.Fore.YELLOW)
            
            print("Please enter number <{0}>:".format(len(num)))
            user_input_num = int(input())
            num.append(user_input_num)
            
            result = 0
            f = "f(x)={0}*x^{1}".format(num[0], p)

            if len(num) >= p+1:
                for _ in range(1, len(num)):
                    f += "{0:+d}*x^{1}".format(num[_], y) 
                    y -= 1
                print("\nFunction:", f)
                print("\n-------Result-------")
                break
        
        for b in range(0, len(num)):
            print("f{0}={1}*{2}{3:+d}={4}".format(i, result, x, num[b], result * x + num[b]))       
            result = result * x + num[b]
            i-=1
        print("\nAnswer: f({0})={1}".format(x, result))
    except ValueError:
        print(colorama.Fore.RED)
        print("You write wrong number, try again!")
        horner()

    # don't close program, when it end.
    input("Enter......")
    horner()
horner()