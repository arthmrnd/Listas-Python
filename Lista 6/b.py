n = input()

nl = []
nl = input().split()
ni = []
for n in nl:
    ni.append(int(n))
xl = []
xl = input().split()
xi = []
for n in xl:
    xi.append(int(n))

ni.sort()
xi.sort()
c = 0
for n in ni[::-1]:
    print(n,xi[c])
    c = c + 1
