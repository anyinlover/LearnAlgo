class Bag:
    def __init__(self):
        self._first = None
        self._n = 0

    def __iter__(self):
        x = self._first
        while x:
            yield x._item
            x = x._next 
    
    class Node:
        def __init__(self):
            self._item = None
            self._next = None

    def add(self, item):
        old = self._first
        self._first = self.Node()
        self._first._item = item
        self._first._next = old
        self._n += 1
    
    def is_empty(self):
        return self._n == 0

    def size(self):
        return self._n

if __name__ == "__main__":
    bag = Bag()
    for i in range(5):
        bag.add(i)
    
    for i in bag:
        print(i)
