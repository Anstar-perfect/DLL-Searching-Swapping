class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLL:
    def __init__(self):
        self.head = None
    def search(self,data):
        t = 0
        temp = self.head
        while temp:
            if temp.data == data:
                t=1
                break
            temp = temp.next
        if t==1:
            print('The element was found')
        else:
            print('Oops element not found')

    def display(self):
        if self.head == None:
            print('That is an empty list')
        else:
            temp = self.head
            while temp:
                print(temp.data,'--->',end=' ')
                temp = temp.next 

l = DoublyLL()
n = Node(10)
l.head = n
n1 = Node(20)
n.next = n1
n2 = Node(30)
n2.prev = n1
n1.next = n2
n3 = Node(40)
n2.next = n3
n3.prev = n2
n4 = Node(50)
n3.next = n4
n5 = Node(60)
n4.next = n5
n5.prev =n4

l.display()
print('\n')
l.search(50)