def binary(array, x):
    low = 0
    high = len(array) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if array[mid] < x:
            low = mid + 1
        elif array[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

n = int(input())

pl = input().split()
pl = [int(a) for a in pl]
ver = input().split()
ver = [int(b) for b in ver]


    
for i in ver:
    if(i == 0):
        break
    search = binary(pl,i)
    if(search != -1):
        print(search)
    else:
        print("Nao foi visitado ainda.")
