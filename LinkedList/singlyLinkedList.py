class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def insertAtBeginning(self,head,data):
        newNode = Node(data)
        newNode.next = head
        return newNode

    def traverse(self,head):
        current = head
        while current:
            print(current.data)
            current = current.next



sll = SinglyLinkedList()
head = None
head = sll.insertAtBeginning(head, 10)
head = sll.insertAtBeginning(head, 100)
head = sll.insertAtBeginning(head, 120)
head = sll.insertAtBeginning(head, 130)

sll.traverse(head)

