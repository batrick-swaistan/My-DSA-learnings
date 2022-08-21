from collections import deque
class Stack:
    def __init__(self):
        self.container=deque()
        
    def push(self,value):
        self.container.append(value)
        
    def pop(self):
        self.container.pop()
        
    def seek(self):
        self.conatiner[-1]
    
    def is_emptyy(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
def reverse(st):
    stack=Stack()
    
    for i in st:
        stack.push(i)
    
    rst=" "
    while stack.size()!=0:
        rst+=stack.pop()
    
    return rst

if __name__=='__main__':
    print(reverse("Batrick"))
