cond = 0
while(cond == 0):
    p, s = input().split()
    s = int(s)
    if(s<90 and s!=0):
        print(p+" Internar")
    if(s>=90):
        print(p+" Alta")
    if(p == '#' and s == 0):
        cond = 1
