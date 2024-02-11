#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, condition="New"):
        self._brand = brand
        self._size = size
        self._condition = condition

    def get_brand(self):
        return self._brand
    
    def set_brand(self, brand):
        self._brand = brand

    brand = property(get_brand, set_brand)

    def get_size(self):
        return self._size
    
    def set_size(self, size):
        if type(size) == int:
            self._size = size
        else:
            print("size must be an integer")

    size = property(get_size, set_size)

    def get_condition(self):
        return self._condition
    
    def set_condition(self, condition):
        self._condition = condition

    condition = property(get_condition, set_condition)

    def cobble(self):
        print("Your shoe is as good as new!")
        self.set_condition("New")