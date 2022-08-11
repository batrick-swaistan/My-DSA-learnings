class Node:
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # Initialize next as null

class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def adddd(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data,end=" ")
            temp = temp.next
            
       
if __name__=='__main__':

    # Start with the empty list
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second # Link first node with second
    second.next = third # Link second node with the third node
    llist.adddd(5)
    llist.printList()
