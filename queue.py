class Queue:
    class Node:
        def __init__(self):
            self._item = None
            self._next = None
    
    def __init__(self):
        self._first = None
        self._last = None
        self._n = 0

    def enqueue(self, item):
        old = self._last
        self._last = self.Node()
        self._last._item = item
        if self.is_empty():
            self._first = self._last
        else:
            old._next = self._last
        self._n += 1

    def dequeue(self):
        r = self._first._item
        self._first = self._first._next
        self._n -= 1
        if self.is_empty():
            self._last = None
        return r
    
    def is_empty(self):
        return self._n == 0
    
    def size(self):
        return self._n

if __name__ == "__main__":
    queue = Queue()
    for i in range(10):
        queue.enqueue(i)
    while not queue.is_empty():
        print(queue.dequeue())
