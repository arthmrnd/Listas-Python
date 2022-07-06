p = int(input())
l1 = input().split()
l1 = [int(n) for n in l1]
l2 = input().split()
l2 = [int(n) for n in l2]
l3 = input().split()
l3 = [int(n) for n in l3]
l4 = input().split()
l4 = [int(n) for n in l4]
l5 = input().split()
l5 = [int(n) for n in l5]
l6 = input().split()
l6 = [int(n) for n in l6]
l7 = input().split()
l7 = [int(n) for n in l7]
l8 = input().split()
l8 = [int(n) for n in l8]
l9 = input().split()
l9 = [int(n) for n in l9]
l10 = input().split()
l10 = [int(n) for n in l10]

cont = 0
for n in l1:
    if(n==p):
        cont = cont + 1
for n in l2:
    if(n==p):
        cont = cont + 1
for n in l3:
    if(n==p):
        cont = cont + 1
for n in l4:
    if(n==p):
        cont = cont + 1
for n in l5:
    if(n==p):
        cont = cont + 1
for n in l6:
    if(n==p):
        cont = cont + 1
for n in l7:
    if(n==p):
        cont = cont + 1
for n in l8:
    if(n==p):
        cont = cont + 1
for n in l9:
    if(n==p):
        cont = cont + 1
for n in l10:
    if(n==p):
        cont = cont + 1

if(cont>0):
    print("sim")
if(cont==0):
    print("nao")
