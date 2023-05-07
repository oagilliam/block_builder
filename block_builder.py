# DESCRIPTION:
# Write a class Block that creates a block (Duh..)

#Requirements/;
#The constructor should take an array as an argument, this will contain 3 integers of the form [width, length, height] 
#from which the Block should be created.

# Date: 5/07/23
class Block:
    def __init__(self, arr):
        self.width = arr[0]
        self.height = arr[1]
        self.length = arr[2]

    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def get_length(self):
        return self.length
    
    def get_volume(self):
        return (self.width * self.length * self.height)
    
    def get_surface_area(self):
        return (2(self.width*self.length + self.width*self.height + self.length*self.height))


b = Block([2,4,6])
print(b.get_width())
print(b.get_length())
print(b.get_height())
print(b.get_volume())
print(b.get_surface_area())
