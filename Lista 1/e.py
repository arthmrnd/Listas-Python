s = int(input())

h = s//3600
sr = s%3600
m = sr//60
s = sr%60
h = str(h)+"h"
m = str(m)+"m"
s = str(s)+"s"

print(h,m,s)
