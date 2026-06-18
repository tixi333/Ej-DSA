class HashTable:
    def __init__(self, size):
        self.hashtable = []
        self.size = size

        for e in range(self.size):
            self.hashtable.append([])
    
    def add(self, value):
        key = self.get_key(value)
        
        for e, lista in enumerate(self.hashtable):
            if e == key:
                if value in lista:
                    return
                else:
                    self.hashtable[e].append(value)

    def delete(self,value):
        key = self.get_key(value)
        
        for e,lista in enumerate(self.hashtable):
            if e == key:
                for index, val in enumerate(lista):
                    if val == value:
                        lista.pop(index)

    def search(self, value):
        key = self.get_key(value)
        
        for e, lista in enumerate(self.hashtable):
            if e == key:
                for val in lista:
                    if val == value:
                        return f"{value} located inside bucket {e}"
                    else:
                        return f"{value} can not be found"

    def show(self):
        print(self.hashtable)
    
    def get_key(self,value):
        u = 0
        for char in value:
            u += ord(char)
        
        return u%self.size
        
        
hash = HashTable(10)

hash.add("Arroz")
hash.add("ChowFan")
hash.add("Caterpie")

print(hash.search("ChowFan"))
print(hash.search("Hola"))

hash.delete("Arroz")
hash.show()

