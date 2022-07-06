n = input()
lx = []
lx = input().split()
lx = list(map(int, lx))
lx = sorted(lx)
print(*lx, sep=" ")
