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
        
        print(self.hash_map)
    
    def search(self,value):
        key = self.get_key(value)

        lista = self.hash_map[key]
        if value not in lista:
            return "{value} can not be found"
        
        else:
            return "{value} is located at buckeet {key}"
    
    def show(self):
        print(self.hash_map)
    
    def modify(self, value, replace):
        key_val = self.get_key(value)
        key_rep = self.get_key(replace)

        if key_val != key_rep:
            return "{value} can not be replaced"
        
        else:
            lista = self.hash_map[key_val]

            for index, e in enumerate(lista):
                if e == value:
                    lista.pop(index)
                    lista.insert(index,replace)
    
    def get_key(self,value):
        u = 0
        for char in value:
            u += ord(char)
        
        return u%self.size
    

hash = HashMap(10)

hash.add("Arroz")
hash.add("ChowFan")
hash.add("Caterpie")

hash.modify("Arroz","Bobe")