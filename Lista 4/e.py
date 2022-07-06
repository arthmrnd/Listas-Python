a, b = input().split()
a = int(a)
b = int(b)

li = []
z = 0
while(z < b):
    li.append(0)
    z = z+1


c = 0
while(c < a):
    s = int(input())
    x = 0
    while(x < b):
        if(x==0 or x%s==0):
            li[x] = 1
        x = x +1
    c = c+1
    
pr = ""
for n in li:
    pr = pr + str(n) + " "
    
pr.lstrip()
print(pr)
