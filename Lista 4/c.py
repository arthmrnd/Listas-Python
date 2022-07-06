n = int(input())
u = []
u = input().split()
ui = []
vi = []
di = []

for ns in u:
    ui.append(int(ns))

for nu in ui:
    if(nu % 2 == 0):
        vi.append(nu)
    else:
        di.append(nu)

par = ""
for n in vi:
    par = par +str(n) + " "
   
impar = ""
for n in di:
    impar = impar +str(n) + " "
 
par = par.rstrip()
impar = impar.rstrip()

print(par)
print(impar)
