from abc import ABC, abstractmethod

class ST:

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def put(self, key, val):
        pass

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def delete(self, key):
        pass

    @abstractmethod
    def contains(self, key):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def keys(self):
        pass

class SequentialSearchST(ST):

    def __init__(self):
        self._first = None
        self._n = 0
    
    class Node:
        def __init__(self, key, val, next):
            self._key = key
            self._val = val
            self._next = next

    def get(self, key):
        x = self._first
        while x:
            if x._key == key:
                return x._val
            x = x._next
        
    def put(self, key, val):
        x = self._first
        while x:
            if x._key == key:
                x._val = val
                return
            x = x._next
        
        self._first = self.Node(key, val, self._first)
    
    def delete(self, key):
        p = None
        x = self._first
        while x:
            if x._key == key:
                if p:
                    p._next = x._next
                else:
                    self._first = x._next
                return
            p = x
            x = x._next

    def contains(self, key):
        x = self._first
        while x:
            if x._key == key:
                return True
        
        return False

    def is_empty(self):
        return self._n == 0
    
    def size(self):
        return self._n