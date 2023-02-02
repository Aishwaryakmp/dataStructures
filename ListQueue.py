class Queue():
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.data = []
    def enqueue(self, data):
        self.data.append(data)
        self.rear = self.rear+ 1
    def dequeue(self):
        self.front = self.front + 1
    def debug(self):
        print(self.data[self.front:self.rear])
        print(self.front)
        print(self.rear-1)
        
q = Queue()
for i in range(1,10):
    q.enqueue(i)
q.dequeue()
q.dequeue()
q.dequeue()

q.debug()


