#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand):
        self.brand = brand
        self.color = None
        self.size = None
        self.material = None
        self.condition = None
        
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, value):
        self._color = value
        
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
            self._size = None
        else:
            self._size = value
            
    @property
    def material(self):
        return self._material
    @material.setter
    def material(self, value):
        self._material = value
        
    @property
    def condition(self):
        return self._condition
    @condition.setter
    def condition(self, value):
        self._condition = value
        
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
    
    