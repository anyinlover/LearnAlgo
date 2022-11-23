from abc import ABC, abstractmethod
from chap1_fundamentals.stack import LinkedListStack
from chap1_fundamentals.queue import Queue

class Paths(ABC):

    @abstractmethod
    def __init__(self, g, s):
        pass

    @abstractmethod
    def has_path_to(self, v):
        pass

    @abstractmethod
    def path_to(self, v):
        pass

class DepthFirstPaths(Paths):

    def __init__(self, g, s):
        self._marked = [False] * g.v()
        self._edge_to = [None] * g.v()
        self._s = s
        self._dfs(g, s)

    def _dfs(self, g, v):
        self._marked[v] = True
        for w in g.adj(v):
            if not self._marked(w):
                self._edge_to[w] = v
                self._dfs(g, w)
    
    def has_path_to(self, v):
        return self._marked[v]

    def path_to(self, v):
        if self.has_path_to(v):
            path = LinkedListStack()
            x = v
            while x != self._s:
                path.push(x)
                x = self._edge_to[x]
            path.push(x)
            return path

class BreadthFirstPaths(DepthFirstPaths):

    def __init__(self, g, s):
        self._marked = [False] * g.v()
        self._edge_to = [None] * g.v()
        self._s = s
        self._bfs(g, s)
    
    def _bfs(self, g, s):
        queue = Queue()
        self._marked[s] = True
        queue.enqueue(s)
        while not queue.is_empty():
            v = queue.dequeue()
            for w in g.adj(v):
                if not self._marked[w]:
                    self._edge_to[w] = v
                    self._marked[w] = True
                    queue.enqueue(w)
