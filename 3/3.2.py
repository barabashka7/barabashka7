class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Predator:
    def bit(self, victim):
        if(isinstance(victim,Mammal)):
            victim.die()
class Mammal:
    def die(self):
        del self
class Tiger(Predator,Animal):
    pass
class Zebra(Mammal,Animal):
    pass
tiger=Tiger("tiger",54)
zebra=Zebra("zebra",23)
tiger.bit(zebra)
print(zebra.name)
