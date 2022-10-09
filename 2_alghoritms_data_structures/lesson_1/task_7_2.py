class Dequeue():
    def __init__(self):
        self.dequeue = []
    def add_front(self, elem):
        self.dequeue.insert(0, elem)
    def add_rear(self, elem):
        self.dequeue.append(elem)
    def from_front(self):
        return self.dequeue.pop()
    def from_rear(self):
        return self.dequeue.pop(0)
    def size_of_dequeue(self):
        return len(self.dequeue)

def polindrom(word: str):
    deq = Dequeue()
    for char in word:
        deq.add_rear(char)
    return deq

deq = polindrom('молоко делили ледоколом')
while deq.size_of_dequeue() > 1:
    if deq.from_rear() != deq.from_front():
        break

if deq.size_of_dequeue() <= 1:
    print('polindrom')
else:
    print('not polindrom')

pass