def binary(array, x):
    l = 0
    r = len(array) - 1
    
    while (l <= r): 
        m = (l + r) // 2 
        if (array[m] == x):
            l = r +1
        elif (array[m] < x): 
            l = m + 1
        else: 
            r = m - 1
            
    cnt = 0
    while(cnt == 0):
        if(m <= r and array[m] <= x):
            m += 1
        else:
            cnt = 1
    return m

n, m = input().split()
n = int(n)
m = int(m)

mat = []
cont = 0
while(cont < n):
    li = input().split()
    for xap in li:
        mat.append(int(xap))
    cont += 1

mat.sort()

c = int(input())
con = input().split()
con = list(map(int, con))
cont = 0
while(cont < c):
    sum = 0
    las = binary(mat,con[cont])
    print(las)
    cont += 1
