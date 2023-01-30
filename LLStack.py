class Node():
    def __init__ (self,data):
        self.data = data
        self.next = None
class linkedList:
    def __init__ (self):
        self.head = None
        
    def findLastNode(self):
        n = self.head
        while(n.next!=None):
            n = n.next
        return n
        
    def push(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            newNode = Node(data)
            lastNode = self.findLastNode()
            lastNode.next = newNode
   
    def print(self):
        n = self.head
        while (n!=None):
            print(n.data)
            n = n.next
            
LL = linkedList()
LL.push(2)
LL.push(3)
LL.push(4)
LL.push(5)
LL.print()
