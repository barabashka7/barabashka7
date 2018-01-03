import random
def initm(size,sposob):
    m=[]
    if(sposob==0):
        for i in range(size):
            sp=[]
            for j in range(size):
                a=int(input())
                sp.append(a)
            m.append(sp)
        return m
    else:
        a = int(input("Введите начало: "))
        b = int(input("Введите конец: "))
        for i in range(size):
            sp=[]
            for j in range(size):
                sp.append(random.randint(a,b))
            m.append(sp)
        return m
def initm2(size):
    m = []
    for i in range(size):
        sp = []
        for j in range(size):
            sp.append(0)
        m.append(sp)
    return m
class M:
    count=0
    def __init__(self,size,sposob):
        M.count+=1
        self.size=size
        self.m=initm(size,sposob)

    def __str__(self):
        s=""
        for i in range(self.size):
            for j in range(self.size):
                s=s+str(self.m[i][j])+" "
            s=s+"\n"
        return s
    @staticmethod
    def getkol():
        return M.count

    def getsize(self):
        return self.size

    def maindiag(self):
        sum=0
        for i in range(self.size):
            sum+=self.m[i][i]
        return sum

    def trans(self):
        m2 = initm2(self.size)
        for i in range(self.size):
            for j in range(i,self.size,1):
                m2[i][j]=self.m[j][i]
                m2[j][i]=self.m[i][j]
        return m2
    def sum(self):
        sum=0
        for i in range(self.size):
            for j in range(self.size):
                sum+=self.m[i][j]
        return sum
    def __lt__(self,other):
        return self.sum()<other.sum()
    def __eq__(self, other):
        return self.sum()==other.sum()
    def __gt__(self, other):
        return self.sum()>other.sum()
    def __add__(self, other):
        if(self.size==other.size):
            m3=initm2(self.size)
            for i in range(self.size):
                for j in range(self.size):
                    m3[i][j]=self.m[i][j]+other.m[i][j]
            return m3
        else:
            print("Сложение не возможно!")
            return self.m
m1=M(5,1)
m2=M(5,1)
m3=M(4,1)
m4=M(4,1)
m5=M(2,0)
print(m1)
print("Сумма главной диагонали: ",m1.maindiag())
print(m2)
print("Сумма главной диагонали: ",m2.maindiag())
print("")
print("До: ")
print(m3)
print("После: ")
print(m3.trans())
print("До: ")
print(m4)
print("После: ")
print(m4.trans())
print("")
print("Сумма первых двух матриц: ")
print(m1+m2)
print("")
print("Самая большая по весу среди 3,4 и 5: ")
if(m3>m4 and m3>m5):
    print(m3)
else:
    if(m4>m5):
        print(m4)
    else:
        print(m5)
