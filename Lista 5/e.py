n, m = input().split()
n = int(n)
m = int(m)

mat = []
cont = 0
while(cont < n):
    l = input().split()
    l = [int(x) for x in l]
    mat.append(l)
    cont += 1
    
ver = []
cont = 0
while(cont < m):
    l = input().split()
    l = [int(x) for x in l]
    ver.append(l)
    cont += 1

kill = 0
for i in range(m):
    for j in range(ver[i][0]):
        if(mat[ver[i][0]-1-j][ver[i][1]] == 1):
            kill += 1
            mat[ver[i][0]-1-j][ver[i][1]] = 0
            break
        else:
            continue
        
print(kill)
