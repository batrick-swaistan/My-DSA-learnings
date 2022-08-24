class Tree_node:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
        
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level +=1
            p=p.parent
        return level
        
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
        
    def print_tree(self):
        spaces=" " *self.get_level()
        prefix=spaces + "|_____" if self.parent else ""
        print(prefix+self.data)
        if self.children:
            for i in self.children:
                i.print_tree()
            
def college():
    rcet=Tree_node("Engineering")
    
    dept=Tree_node("Computer Science")
    dept.add_child(Tree_node("Infosys"))
    dept.add_child(Tree_node("Tcs"))
    dept.add_child(Tree_node("Chainsys"))
    
    
    dept2=Tree_node("ECE")
    dept2.add_child(Tree_node("Wipro"))
    dept2.add_child(Tree_node("Nirman"))
    dept2.add_child(Tree_node("Capegemini"))
    
    
    dept3=Tree_node("Mech")
    dept3.add_child(Tree_node("Ashok Leyland"))
    dept3.add_child(Tree_node("Tata"))
    dept3.add_child(Tree_node("Eicher"))
    
    rcet.add_child(dept)
    rcet.add_child(dept2)
    rcet.add_child(dept3)
    
    return rcet
if __name__=="__main__":
    pret=college()
    pret.print_tree()
    
    
    
    
    
        
