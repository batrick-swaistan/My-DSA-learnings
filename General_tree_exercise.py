class TreeNode:
    def __init__(self,name,designation):
        self.name=name
        self.designation=designation
        self.children=[]
        self.parent=None
    def get_lvl(self):
        level=0
        d=self.parent
        while d:
            level+=0
            d=d.parent
        return level
    
    def add_child(self,child):
        self.children.append(child)
        child.parent=self
        
    def print_tree(self,property_name):
        if property_name=='both':
            value= self.name+ "("+self.designation+")"
        if property_name=='name':
            value=self.name
        else:
            value=self.designation
        spaces=' '*self.get_lvl()*3
        prefix= spaces + "|______" if self.parent else ""
        print(prefix+value)
        if self.children:
            for i in self.children:
                i.print_tree(property_name)

def company():
    comp=TreeNode("Nilupul","CEO")
    
    mem=TreeNode("Chinmay","CTO")
    submem=TreeNode("Vishwa","Infrastructure Head")
    submem.add_child(TreeNode("Dhaval","Cloud Manager"))
    submem.add_child(TreeNode("Abijith","App Manager"))
    mem.add_child(submem)
    mem.add_child(TreeNode("Amir","Application Head"))

    
    mem2=TreeNode("Gels","HR Head")
    mem2.add_child(TreeNode("Peter","Requirement Manager"))
    mem2.add_child(TreeNode("Waqus","Product Manager"))
    
    comp.add_child(mem)
    comp.add_child(mem2)
    
    return comp
#     infra_head = TreeNode("Vishwa","Infrastructure Head")
#     infra_head.add_child(TreeNode("Dhaval","Cloud Manager"))
#     infra_head.add_child(TreeNode("Abhijit", "App Manager"))

#     cto = TreeNode("Chinmay", "CTO")
#     cto.add_child(infra_head)
#     cto.add_child(TreeNode("Aamir", "Application Head"))

#     # HR hierarchy
#     hr_head = TreeNode("Gels","HR Head")

#     hr_head.add_child(TreeNode("Peter","Recruitment Manager"))
#     hr_head.add_child(TreeNode("Waqas", "Policy Manager"))

#     ceo = TreeNode("Nilupul", "CEO")
#     ceo.add_child(cto)
#     ceo.add_child(hr_head)

#     return ceo

if __name__=="__main__":
    ff=company()
    ff.print_tree("both")
