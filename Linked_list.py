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
    def inser_at(self,pre_node,new_data):
        if pre_node is None:
            print("The given Node is not in Linked List")
            return
        new_node=Node(new_data)
        new_node.next=pre_node.next
        pre_node.next=new_node
    def insertlast(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            new_node=self.head
            return
        last=self.head
        while (last.next):
            last=last.next
        last.next=new_node
    
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
