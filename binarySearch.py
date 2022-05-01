def binarySearch(low, mid, high):
    for x in range(100):
        if array[mid] == find:
            return mid
        if array[mid] < find:
            low = mid+1
            mid = int((low+high)/2)
        else:
            high = mid-1
            mid = int((low+high)/2)
    return -1
    
def arrayMaker():
    for x in range(size):
        array.append(x+1)

size = 100000

find = 27195
array = []
found = False
arrayMaker()
output = binarySearch(0, (int((len(array)-1)/2)), (int(len(array)-1)))
if output == -1:
    print("Failed")
else:
    print("Found at index: ")
    print(output)
