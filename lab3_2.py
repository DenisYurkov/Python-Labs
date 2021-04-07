def fn(a, d, n):
    if n == 1:
        return a
    return fn(a+d, d, n-1)


try:
    start_num = int(input("Write first element of the progression: "))
    dif_progress = int(input("Write difference progression: "))
    find_num = int(input("Write the element you want to find: "))
except ValueError:
    print("Your write wrong number!")
    quit()

print("Result:", fn(start_num, dif_progress, find_num))