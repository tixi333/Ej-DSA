class HashMap:
    def __init__(self, size):
        self.hash_map = {}
        self.size = size
        
        for e in range(self.size):
            self.hash_map[e] = []
           
        
    def add(self, value):
        key = self.get_key(value)
        
        lista = self.hash_map[key]
        if value in lista:
            return
        else:
            lista.append(value)
    
    def delete(self,value):
        key = self.get_key(value)
        
        lista = self.hash_map[key]
        if value in lista:
            lista.remove(value)
        else:
            return
    
    def search(self):
        pass
    
    def show(self):
        pass
    
    def modify(self):
        pass
    
    def get_key(self,value):
        u = 0
        for char in value:
            u += ord(char)
        
        return u%self.size
    

hash = HashMap(10)

hash.add("Arroz")
hash.add("ChowFan")
hash.add("Caterpie")