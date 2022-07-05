t = int(input())
cond = 0
while(cond==0):
    p = int(input())
    if(p>t):
        cond=2
        print("ALARME")
    if(p==0):
        cond=1

if(cond==1):
    print("O Havai pode dormir tranquilo")
