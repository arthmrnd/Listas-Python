m1 = []
cont = 0
while(cont < 10):
    a = input().split()
    m1.append(a)
    cont = cont + 1

i = 0
j = 0
while(i < 10):
    j = 0
    while(j < 10):
        if(m1[i][j] == 't'):
            if(i<9 and j<9 and i != 0 and j != 0):
                if(m1[i-1][j] == '*' or m1[i+1][j] == '*' or m1[i][j-1] == '*' or m1[i][j+1] == '*'):
                    m1[i][j] = 'p'
            if(i<9 and j>8 and i != 0 and j != 0):
                if(m1[i-1][j] == '*' or m1[i][j-1] == '*' or m1[i+1][j] == '*'):
                    m1[i][j] = 'p'
            if(i>8 and j>8 and i != 0 and j != 0):
                if(m1[i-1][j] == '*' or m1[i][j-1] == '*'):
                    m1[i][j] = 'p'
            if(i>8 and j<9 and i != 0 and j != 0):
                if(m1[i-1][j] == '*' or m1[i][j-1] == '*' or m1[i][j+1] == '*'):
                    m1[i][j] = 'p'
            if(i == 0 and j<9 and j != 0):
                if(m1[i][j-1] == '*' or m1[i][j+1] == '*' or m1[i+1][j] == '*'):
                    m1[i][j] = 'p'
            if(i == 0 and j>8):
                if(m1[i][j-1] == '*' or m1[i+1][j] == '*'):
                    m1[i][j] = 'p'
            if(j == 0 and i<9 and i != 0):
                if(m1[i-1][j] == '*' or m1[i+1][j] == '*' or m1[i][j+1] == '*'):
                    m1[i][j] = 'p'
            if(j == 0 and i>8 and i != 0):
                if(m1[i-1][j] == '*' or m1[i][j+1] == '*'):
                    m1[i][j] = 'p'
            if(i == 0 and j == 0):
                if(m1[i][j+1] == '*' or m1[i+1][j] == '*'):
                    m1[i][j] = 'p'
            
        j = j +1
    i = i + 1

for li in m1:
    print(*li, sep=' ')

            