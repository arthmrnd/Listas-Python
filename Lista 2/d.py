n = int(input())

cv = 0
vv = 0
lm = 0

cont = 0
while(cont < n):
    if(cont < n):
        cv = cv + 1
        cont = cont + 1
    if(cont < n):
        vv = vv + 1
        cont = cont + 1
    if(cont < n):
        lm = lm + 1
        cont = cont + 1
        
print("Chapeuzinho Vermelho " + str(cv))
print("Vovozinha " + str(vv))
print("Lobo Mau " + str(lm))
