class Graph:
    def __init__(self,edges):
        self.edges=edges
        self.graph_dict={}
        for start,end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start]=[end]
        print(self.graph_dict)
    
    def get_path(self,start,end,path=[]):
        path +=[start]
        
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        
        paths=[]
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths=self.get_path(node,end,path)
                for p in new_paths:
                    paths.append(p)
        return paths
    def get_short_path(self,start,end,path=[]):
        path= path + [start]
        
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return None
        
        short_path=None
        for node in self.graph_dict[start]:
            if node not in path:
                sp=self.get_short_path(node,end,path)
                if sp:
                    if short_path is None or len(sp) < len(short_path):
                        short_path=sp
        return short_path
                
                
if __name__=="__main__":
    routes=[
        ("Mumbai","Paris"),
        ("Mumbai","Dubai"),
        ("Paris","Dubai"),
        ("Paris","New York"),
        ("Dubai","New York"),
        ("New York","Toronto")
    ]
    
    start="Mumbai"
    end="New York"
    
#     nodes=Graph(routes)
#     print(nodes.get_path(start,end))
#     routes=[
#         ("Mumbai","Paris"),
#         ("Mumbai","Dubai"),
#         ("Paris","New York"),
#         ("Dubai","London"),
#         ("London","New York"),
#         ("New York","Toronto")
#     ]
    
#     start="Mumbai"
#     end="New York"
    
#     nodes=Graph(routes)
#     print(nodes.get_short_path(start,end))
