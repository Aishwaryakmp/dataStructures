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
    
    def deleteInnerElement(self,data):
        n = self.head
        n2 = None
        while(n.data!= data):
            n2  = n
            n = n.next
        n2.next = n.next
        return n.data
            
    def push(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            newNode = Node(data)
            lastNode = self.findLastNode()
            lastNode.next = newNode
            
    # popping last element        
    def pop(self):
       n = self.head
       n2 = None
       while(n.next != None):
           n2 = n
           n = n.next
       n2.next = None
    # popping first element
    def popFirstElement(self):
        value = self.head.data
        self.head = self.head.next
        return value
    
    #popping node 
    def popElement(self,data):
        n = self.head
        #delete first element
        if (n!= None and n.data == data):
            p = n
            self.head = n.next
            return p.data
        #delete last element
        elif (self.findLastNode().data == data):
            n1 = self.head
            n2 = None
            while (n1.next != None):
                n2 = n1
                n1 = n1.next
            n2.next = None
            return n1.data
        #delete middle element
        else:
            self.deleteInnerElement(data)
            
    def print(self):
        print("------")
        n = self.head
        while (n!=None):
            print(n.data)
            n = n.next
        print("------")
            
LL = linkedList()
LL.push(1)
LL.push(2)
LL.push(3)
LL.push(4)
LL.push(5)
LL.print()
LL.popElement(5)
LL.print()
LL.popElement(1)
LL.print()
LL.popElement(3)
LL.print()