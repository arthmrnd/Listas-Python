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
while(cont < nl[0]):
    a = input().split()
    a = [int(n) for n in a]
    m2.append(a)
    cont = cont + 1

c = []

cont = 0
while(cont < nl[0]):
    sub = []
    for il, ik in zip(m1[cont],m2[cont]):
        a = il - ik
        sub.append(a)
    c.append(sub)
    cont = cont + 1
    
for li in c:
    dr = ""
    for x in li:
        dr = dr + str(x) + " "
    dr.lstrip()
    print(dr)

