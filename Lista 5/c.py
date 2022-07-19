nl = []
nl = input().split()
nl = [int(n) for n in nl]

m1 = []
m2 = []
cont = 0
while(cont < nl[0]):
    a = input().split()
    a = [int(n) for n in a]
    m1.append(a)
    cont = cont + 1

cont = 0
nx = int(input())
while(cont < nx):
    a = input().split()
    a = [int(n) for n in a]
    a = [n-1 for n in a]
    m2.append(a)
    cont = cont + 1

c = []

for l in m2:
    m1[l[0]][l[1]] = 0
    
b = 0
for l in m1:
    b = b + sum(l)

if(b == 0):
    print("HASTA LA VISTA BABY")
else:
    print("ILL BE BACK")

