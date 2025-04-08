class Item: 
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

class Movie(Item): 
    def __init__(self, name, rating, length):
        super().__init__(name, rating)
        self.length = length
    def total_length(self):
        return self.length 
    
shawshank = Item("Vykoupeni z věznice Shawshank", 9.9)
print(shawshank.total_length())

# program zkončí chybou AttributeError