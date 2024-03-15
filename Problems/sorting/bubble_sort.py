list = [72, 33, 27, 15, 37, 62]

def bubble_sort(list):
    n = len(list)
    for i in range(n):
        # print(list)
        for j in range(n-i-1):
            # print(f'i,j: {i}{j}   {list[j]},{list[j+1]}')
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

bubble_sort(list)
print(list)