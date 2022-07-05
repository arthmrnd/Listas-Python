def primo(n):
    for x in range(2,n):
        if n % x == 0:
            return False
    return True

a, b = input().split()
a = int(a)
b = int(b)

pri = 0
while(a <= b):
    if(primo(a)):
        pri += 1
    a += 1

print(pri)
