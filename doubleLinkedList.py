class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    
    def __init__(self):
        self.head = None
    
    def insertAtBegin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
    
    def deleteAtBegin(self):
        if self.head is None:
            print("List is Empty")
            return
        elif self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None
            
    def printAll(self):
        if self.head is None:
            print("List is empty")
            return
        current = Node()
        current = self.head
        while(current != None):
            print(current.data)
            current = current.next
        print()


head = DoubleLinkedList()
head.insertAtBegin(10)
head.insertAtBegin(20)
head.insertAtBegin(30)
print("List after inserting node at begining: ")
head.printAll()
head.deleteAtBegin()
print("List after deleting node from begining: ")
head.printAll()

            
        