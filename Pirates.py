import random

class Pirate:
    def __init__(self):
        self.name = input("Введите имя пирата: ")
        self.max_weight = int(input("Введите грузоподъемность: "))
        while (self.max_weight > 60):
            self.max_weight = int(input("Введите грузоподъемность: "))
        self.sum_gold = 0
        self.kol_chests = 0
        self.sum_ill_days = 0
        self.kol_empty_chests = 0
        self.weight = 0
    def open_chest(self):
        chest=Chest()
        if(self.weight < self.max_weight + chest.weight):
            self.weight += chest.weight
            self.kol_chests += 1
            self.sum_gold += chest.gold
            self.sum_ill_days += chest.ill_days
            if(chest.ill_days == 0 and chest.gold == 0):
                self.kol_empty_chests += 1
            return True
        else:
            return False
class Chest:
    def __init__(self):
        self.weight = random.randint(4, 10)
        type = random.randint(1, 3)
        if (type == 1):
            self.gold = random.randint(15, 100)
            self.ill_days = 0
        elif (type == 2):
            self.ill_days = random.randint(3, 10)
            self.gold = 0
        elif (type == 3):
            self.gold = 0
            self.ill_days = 0

pirates = []
for i in range(4):
    pirates.append(Pirate())
    flag = True
    while(flag):
        flag = pirates[i].open_chest()

for i in pirates:
    print(i.name," перевез сундуков: ",i.kol_chests)

max=-1
for i in pirates:
    if(i.sum_gold > max):
        max = i.sum_gold
        str = i.name
    elif(i.sum_gold == max):
        str = str + ", " + i.name
print("Максимальное кол-во золота: ",max, " - ",str)

max = -1
for i in pirates:
    if(i.sum_ill_days > max):
        max = i.sum_ill_days
        str = i.name
    elif(i.sum_gold == max):
        str = str + ", " + i.name
print("Максимальное кол-во дней с болезнью: ",max, " - ",str)

min = 16
for i in pirates:
    if(i.kol_empty_chests < min):
        min = i.kol_empty_chests
        str = i.name
    elif(i.sum_gold == min):
        str = str + ", " + i.name
print("Минимальное кол-во пустых сундуков: ",min, " - ",str)