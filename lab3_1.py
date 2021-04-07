def draw_frame_of_symbols(width, height, symbol):
    print("\n")
    
    w = width - 2
    
    if height == 1: 
        print(symbol*width)
    else:
        print(symbol*width)
        for _ in range(height-2):
            if width == 1: 
                print(symbol)
            else:    
                print(symbol + " "*w + symbol)
        print(symbol*width)



try:
    width = int(input("Width: "))
    height = int(input("Height: "))
    symbol = str(input("Symbol: "))

    if len(symbol) > 1:
        print("You entered more than one char!")
        quit()
except ValueError:
    print("You write wrong number!")
    quit()

draw_frame_of_symbols(width, height, symbol)