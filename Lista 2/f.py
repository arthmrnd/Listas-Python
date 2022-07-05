a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

percent = ((a+b+c)/110)*100
percent = int(percent)
if((a+b+c) > 110):
    print("Hum, parece que houve um erro")
else:
    if(percent >= 0 and percent <= 50):
        print("Seu pokemon nao fara progresso em batalhas")
    if(percent >= 51 and percent <= 66):
        print("Seu pokemon esta acima da media")
    if(percent >= 67 and percent <= 79):
        print("Seu pokemon certamente me chamou atencao")
    if(percent >= 80 and percent <= 100):
        print("Seu pokemon e uma maravilha")

