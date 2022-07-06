n = int(input())
u = []
u = input().split()
v = []
v = input().split()
d = []
d = input().split()
ui = []
vi = []
di = []

for ns in u:
    ui.append(int(ns))
for ns in v:
    vi.append(int(ns))
for ns in d:
    di.append(int(ns))

p = []
i = 0
for nu in ui:
    x = nu + vi[i]
    p.append(x)
    i = i+1

if(di == p):
    print("OK")
else:
    print("NOPE :(")

