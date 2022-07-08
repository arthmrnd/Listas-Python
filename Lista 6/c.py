x = int(input())

mat = []
c = 0
while(c < x):
    nl = []
    nl = input().split()
    ni = []
    for n in nl:
        ni.append(int(n))
    mat.append(ni)
    c = c + 1

li = []
for l in mat:
    li.append(l[1])
    
li.sort()
for n in li[::-1]:
    for x in mat:
        if(n == x[1]):
            print(x[0],x[1])