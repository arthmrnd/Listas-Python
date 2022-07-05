z, g = input().split()
d, c = input().split()
z = str(z)
g = str(g)
d = str(d)
c = str(c)

if(z!=d):
    print("Bloqueado")
if(z == d and g == c):
    print("Driblado")
    print("Gol")
if(z == d and g != c):
    print("Driblado")
    print("...e o goleiro pega")

