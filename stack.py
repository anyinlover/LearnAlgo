from abc import ABC, abstractmethod

class Stack(ABC):

    @abstractmethod
    def push(self, item):
        pass
    
    @abstractmethod
    def pop(self):
        pass
    
    @abstractmethod
    def is_empty(self):
        pass
    
    @abstractmethod
    def size(self):
        pass

class ResizingArrayStack(Stack):

    def __init__(self):
        self._a = [None] * 10
        self._n = 0

    def push(self, item):
        if len(self._a) == self._n:
            self._resize(self._n * 2)
        self._a[self._n] = item
        self._n += 1
    
    def pop(self):
        self._n -= 1
        r = self._a[self._n]
        self._a[self._n] = None
        if self._n > 0 and self._n == len(self._a) // 4:
            self._resize(self._n * 2)
        return r
    
    def is_empty(self):
        return self._n == 0

    def size(self):
        return self._n

    def _resize(self, cap):
        tmp = [None] * cap
        tmp[:self._n] = self._a[:self._n]
        self._a = tmp

class LinkedListStack(Stack):

    class Node:
        def __init__(self):
            self._item = None
            self._next = None
    
    def __init__(self):
        self._first = None
        self._n = 0
    
    def push(self, item):
        old = self._first
        self._first = self.Node()
        self._first._item = item
        self._first._next = old
        self._n += 1

    def pop(self):
        r = self._first._item
        self._first = self._first._next
        self._n -= 1
        return r
    
    def is_empty(self):
        return self._n == 0

    def size(self):
        return self._n

if __name__ == "__main__":
    stack = LinkedListStack()
    for i in range(10):
        stack.push(i)
    while not stack.is_empty():
        print(stack.pop())
