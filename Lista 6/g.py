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

n = int(input())
pl = input().split()
x = int(input())
vi = input().split()

mat = []
cont = 0
while(cont < n):
    li = []
    li = input().split()
    li = list(map(int, li))
    mat.append(li)
    cont += 1
    
pos = 0
dis = 0
for p in vi:
    d = binary(pl,p)
    dis = dis + mat[pos][d]
    pos = d

print(dis)
    