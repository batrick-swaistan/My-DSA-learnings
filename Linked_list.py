#Single-Linked-List
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
    
    
    #Double-Linked-List
    class Node():
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DoubleLinkedList():
    def __init__(self):
        self.head=None
    def fst(self,data):
        new_node=Node(data)
        new_node.next=self.head
        new_node.prev=None
        if self.head is not None:
            self.head.prev=new_node
        self.head=new_node
    def insrt_at(self,prev_node,new_value):
        if prev_node is None:
            print("Pre is empty")
            return
        new_node=Node(new_value)
        new_node.next=prev_node.next
        prev_node.next=new_node
        new_node.prev=prev_node
        if new_node.next is not None:
            new_node.next.prev=new_node
    def insrt_last(self,new_val):
        new_node=Node(new_val)
        if self.head is None:
            new_node=self.head
            new_node.prev=None
            return
            return
        tp=self.head
        while tp.next:
            tp=tp.next
        tp.next=new_node
        new_node.next=None
        new_node.prev=tp.next
    def printing(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
if __name__=="__main__":
    dllist=DoubleLinkedList()
    dllist.head=Node(1)
    second=Node(2)
    Third=Node(3)
    foruth=Node(4)
    
    dllist.head.next=second
    dllist.head.prev=None
    second.next=Third
    second.prev=dllist.head
    Third.next=foruth
    Third.prev=second
    foruth.next=None
    foruth.prev=Third
    dllist.fst(9)
    dllist.printing()
