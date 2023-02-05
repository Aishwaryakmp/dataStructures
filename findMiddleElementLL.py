class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None
    
    def push(self,data):
            newNode = Node(data)
            if self.head == None:
                self.head = newNode
                self.last = self.head
            else:
                self.last.next = newNode
                self.last = self.last.next
            
    def print(self):
        n = self.head
        print("------")
        while(n.next != None):
            print(n.data)
            n = n.next
        
            
    def findMiddleElement(self):
        hare = self.head
        tortoise = self.head
        while hare.next != None:
            hare = hare.next.next
            tortoise = tortoise.next
        return tortoise.data
            

q = LinkedList()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)
q.push(6)
q.push(7)
q.push(8)
q.push(9)


# print(q.push(1))
# print(q.push(2))
# print(q.push(3))
# print(q.push(4))
# print(q.push(5))
# print(q.push(6))
# print(q.push(7))
q.print()
print("middleElement", q.findMiddleElement())


