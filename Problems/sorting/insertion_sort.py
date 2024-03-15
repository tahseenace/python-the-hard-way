# Push bigger elements to right. 

list = [34, 72, 33, 27, 15, 37, 62]

def insertion_sort(list):
    n = len(list)
    for i in range(1,n): # start with second element
        j = i
        while j > 0 and list[j] < list[j-1]:
            list[j], list[j-1] = list[j-1], list[j]
            j -= 1

insertion_sort(list)
print(list)
