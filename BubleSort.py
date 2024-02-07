def BubbleSort(my_list: list) -> list:
    lenth = len(my_list)
    for i in range(0, lenth):
        for j in range(i, lenth):
            if my_list[j] < my_list[i]:
                my_list[i], my_list[j] = myList[j], my_list[i]
    return my_list
