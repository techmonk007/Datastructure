class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self,head,data):
        newNode = Node(data)
        newNode.next = head
        return newNode

    def insertAtEnd(self,head,data):
        newNode = Node(data)
        if head == None:
            head = newNode
        else:
            current = head
            while current.next:
                current = current.next
            current.next = newNode


    def traverse(self,head):
        current = head
        if current is None:
            print("SLL is empty")
        else:
            while current:
                print(current.data)
                current = current.next



sll = SinglyLinkedList()
sll.head = sll.insertAtBeginning(sll.head, 10)
sll.head = sll.insertAtBeginning(sll.head, 100)
sll.head = sll.insertAtBeginning(sll.head, 120)
sll.head = sll.insertAtBeginning(sll.head, 130)
sll.insertAtEnd(sll.head,1000)
sll.traverse(sll.head)
