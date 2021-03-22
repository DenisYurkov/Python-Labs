def binary_search(lists, item):
    low = 0
    high = len(lists) - 1

    while low <= high:
        mid = (low + high) // 2 # // разделение без остатка
        guess = lists[mid]

        if guess == item: # find number
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9, 12]

print(binary_search(my_list, 5))
