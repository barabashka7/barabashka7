class MyQueue:
    def __init__(self):
        self.items=[]
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items[self.size()-1]
    def size(self):
        return len(self.items)
    def isEmpty(self):
        if(self.size()==0):
            print("Пусто")
        else:
            print("Не пусто")
a=MyQueue()
a.isEmpty()
a.enqueue(5)
a.isEmpty()
a.enqueue(10)
print(a.size())
print(a.dequeue())
a.enqueue(15)
a.enqueue(20)
print(a.dequeue())
print(a.size())
