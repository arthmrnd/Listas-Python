def binary(array, x):
    l = 0
    r = len(array) - 1
    while (l <= r): 
        m = (l + r) // 2 
        if (array[m] == x): 
            return m
        elif (array[m] < x): 
            l = m + 1
        else: 
            r = m - 1
    return -1

n, q = input().split()
n = int(n)
q = int(q)

mat = []
cont = 0
while(cont < q):
    li = input().split()
    li = list(map(int, li))
    mat.append(li)
    cont += 1

mat.sort(key=lambda x: x[1])
mat.sort(key=lambda x: x[0], reverse=True)

selec = []
cont = 0
while(cont < n):
    selec.append(mat[cont])
    cont += 1

c = int(input())

cont = 0
selec.sort()
while(cont < c):
    li = input().split()
    li = list(map(int, li))
    res = binary(selec,li)
    if(res == -1):
        print("Nao")
    else:
        print("Sim")
    cont += 1
