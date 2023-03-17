from  random import choice
z = ["учебник", "доска", "коробка", "бутылка", "кружка", "диван"]
hp = 9
x = choice(z).upper()	
xp = x
print("добро пожаловать на поле чудес")
v = ""
win = False
zv = z
v = list(len(x)"")
while hp != 0:
    print("количество попыток:", hp)
    print("Слово:", *v)
    print("Слово или буква?")
    print("[1] Слово")
    print("[2] Буква")
    dd = input()
    if dd == "1":
        gg = input().upper()	
        if gg == xp:
            print("Ты победил!")
            won = True
            break
        else:
            print("Неправильно. Переделывай")
            hp -= 1
    if dd == "2":
        gg = input().upper()	
        if gg in x:
            for c in range(len(x)):
                if gg == x[c]:
                    v[c] = gg
        else:
            print("Этой буквы в слове нет")
            hp -= 1
    if v == x :
        win = True
        break
if win == True:
    print("Ты победил!")
else:
    print("Ты проиграл. Загаданное слово - ", xp)
