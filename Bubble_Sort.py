def bubbleSort(arr):
    for x in range(len(arr)):
        for y in range(len(arr)-1):
            if arr[y] > arr[y+1]:
                temp = arr[y]
                arr[y] = arr[y+1]
                arr[y+1] = temp
                print(arr)
    return arr

print(bubbleSort([1,5,6,3,2,4,150,863,243,2435,0,7]))