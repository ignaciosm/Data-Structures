"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

# AS A LINKED LIST
import sys
sys.path.append('../singly_linked_list')
from singly_linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_tail()
        else:
            pass

# AS AN ARRAY

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.size += 1
#         self.storage.append(value)

#     def pop(self):
#         if self.size > 0:
#             self.size -= 1
#             return self.storage.pop()
#         else:
#             pass

# s = Stack()
# s.push(1)
# print(s.size)
# s.push(2)
# print(s.size)
# s.push(3)
# print(s.size)
# s.push(4)
# print(s.size)
# print("first", s.storage[0])
# print("last", s.storage[len(s.storage)-1])
# s.pop()
# print("first", s.storage[0])
# print("last", s.storage[len(s.storage)-1])