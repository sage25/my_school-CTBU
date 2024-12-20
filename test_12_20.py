def bubble_sort(lst):
    for i in range(0, len(lst)):
        for j in range(0, len(lst) -i - 1):
            if lst[j] > lst[j+1]:
                temp = lst[j+1]
                lst[j+1] = lst[j]
                lst[j] = temp
    return lst

lst = [2,7,2,6,3,7,19,0]
#      0 1 2 3 4 5 6
print(bubble_sort(lst))


