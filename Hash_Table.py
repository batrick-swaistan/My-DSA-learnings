#Hash-Table


class Hashtable:
    def __init__(self):
        self.max=100
        self.arr=[None for i in range(self.max)]
    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h%self.max
    def __setitem__(self,key,value):
        h=self.get_hash(key)
        self.arr[h]=value
    def __getitem__(self,key):
        h=self.get_hash(key)
        return self.arr[h]
    def __delitem__(self,key):
        h=self.get_hash(key)
        self.arr[h]=None

#Handling Collision:


class Hashtable:
    def __init__(self):
        self.max=10
        self.arr=[[] for i in range(self.max)]
    def hash_fun(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h%self.max
    def __setitem__(self,key,value):
        h=self.hash_fun(key)
        found=False
        for idx,ele in enumerate(self.arr[h]):
            if len(ele)==2 and ele[0]==key:
                self.arr[h][idx]=(key,value)
                found=True
                break
        if not found:
            self.arr[h].append((key,value))
    def __getitem__(self,index):
        h=self.hash_func(index)
        return self.arr[h]
    def __delitem__(self,key):
        h=self.hash_func(key)
        for index,ele in enumerate(self.arr[h]):
            if ele[0]==key:
                del self.arr[h][index]
        
        
