l, p = input().split()
l1, p1 = input().split()
l2, p2 = input().split()
l = int(l)
l1 = int(l1)
l2 = int(l2)
p = int(p)
p1 = int(p1)
p2 = int(p2)

l = l + l1 + l2
p = p + p1 + p2

if (l>p):
    print("Lucas")
if (l<p):
    print("Pedro")
if (l==p):
    print("Empate")
    