q1, q2, q3 = input().split()
e1, e2, e3 = input().split()
q1 = int(q1)
q2 = int(q2)
q3 = int(q3)
e1 = int(e1)
e2 = int(e2)
e3 = int(e3)

r1 = (q1-e1)-(e1*2)
r2 = (q2-e2)-(e2*2)
r3 = (q3-e3)-(e3*2)

resta = int(r1+r2+r3)
print(resta)
