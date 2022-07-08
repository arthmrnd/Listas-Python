q = input().split()
q[0] = int(q[0])

cont =  0
mat = []
while(cont < q[0]):
    li = input().split()
    li[1] = int(li[1])
    mat.append(li)
    cont += 1
    
if(q[1] == 'N' and q[2] == 'C'):
    mat.sort(key=lambda x: x[0])
if(q[1] == 'N' and q[2] == 'D'):
    mat.sort(key=lambda x: x[0],reverse=True)
if(q[1] == 'L' and q[2] == 'C'):
    mat.sort(key=lambda x: x[1])
if(q[1] == 'L' and q[2] == 'D'):
    mat.sort(key=lambda x: x[1],reverse=True)
    
for l in mat:
    print(*l, sep=' ')
