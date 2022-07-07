n = int(input())

e = []
e = input().split()

e = [int(x) for x in e]

f=[]
cont = 0
for i in e:
    if(i==1):
        f.append(i)
        cont = cont+1
    if(i==2):
        f.append(i)
        cont = cont+1
    if(i==3):
        f.append(i)
        cont = cont+1
    if(i==4):
        f.append(i)
        cont = cont+1
    if(i==5):
        f.append(i)
        cont = cont+1
    if(i==6):
        f.append(i)
        cont = cont+1
    if(i==7):
        f.append(i)
        cont = cont+1
p = ""
f.sort()
for n in f:
    p = p + str(n) + " "
    
p.lstrip()
print(p)

if(cont==7):
    print("Saia Shenlong e realize o meu desejo")
else:
    print("Nao encontramos todas")
    
