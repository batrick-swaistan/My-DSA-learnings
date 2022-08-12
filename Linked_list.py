class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class LinkedList:
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
        last.next=new_node
    def delnod(self,key):
        temp=self.head
        if temp is not None:
            if temp.data==key:
                self.head=temp.next
                temp=None
                return
        while temp is not None:
            if temp.data ==key:
                break
            prev=temp
            temp=temp.next
        if temp==None:
            return
        prev.next=temp.next
        temp=None
    
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
    llist.head.next = second 
    second.next = third 
    llist.adddd(5)
    llist.printList()
