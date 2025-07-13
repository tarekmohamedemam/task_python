def sort_list():
    my_list = []
    for i in range(5):
        x = input("Enter value: ")
        my_list.append(x)

    asc = sorted(my_list)
    desc = sorted(my_list, reverse=True)

    return asc, desc