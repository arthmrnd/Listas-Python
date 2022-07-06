n = int(input())
nl = []
nl = input().split()
c = int(input())

np = -1

nl = [int(n) for n in nl]

for nu in nl:
    if(nu == c):
        np = nu

print(np)
