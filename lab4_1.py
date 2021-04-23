def lab4_1():
    lst = []
    file = open('.\\projektowe.txt', "r")
    data = file.read()

    for x in data:
        if x in lst: continue
        lst.append(x)
        n = data.count(x)
        print("The count {0}: {1} ".format(x, n))

    print("How many characters are in the file: {0}".format(len(data)))
lab4_1()

