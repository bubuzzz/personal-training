# continue to swap 2 numbers until nothing can be

def sort(arr):
    maximum = 0
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp

    return arr

arr = [5,9,3,1,2,8,4,7,6]
for i in range(0, 10):
    arr = sort(arr)


print (arr)
