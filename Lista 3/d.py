x = int(input())
cond = 0
c=1
while(cond == 0):
    if(c > x):
        cond = 1
    if(c == x):
        print("Dattebayo")
        cond = 2
    c = c*2
if(cond == 1):
    print("Tururuuu")

