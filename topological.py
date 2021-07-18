from stack import LinkedListStack
from queue import Queue

class DirectedCycle:
    def __init__(self, g):
        self._on_stack = [False] * g.v()
        self._edge_to = [None] * g.v()
        self._marked = [False] * g.v()
        self._cycle = None
        for v in range(g.v()):
            if not self._marked[v]:
                self._dfs(g, v)
    
    def _dfs(self, g, v):
        self._on_stack[v] = True
        self._marked[v] = True
        for w in g.adj(v):
            if self.has_cycle():
                return
            elif not self._marked[w]:
                self._edge_to[w] = v
                self._dfs(g, w)
            elif self._on_stack[w]:
                self._cycle = LinkedListStack()
                x = v
                while x != w:
                    self._cycle.push(x)
                    x = self._edge_to[x]
                self._cycle.push(w)
                self._cycle.push(v)
        self._on_stack[v] = False

    def has_cycle(self):
        return self._cycle is not None

    def cycle(self):
        return self._cycle

class DepthFirstOrder:

    def __init__(self, g):
        self._pre = Queue()
        self._post = Queue()
        self._reverse_post = LinkedListStack()
        self._marked = [False] * g.v()
        for v in range(g.v()):
            if not self._marked[v]:
                self._dfs(g, v)

    def _dfs(self, g, v):
        self._pre.enqueue(v)
        self._marked[v] = True
        for w in g.adj(v):
            if not self._marked[w]:
                self._dfs(g, w)
        
        self._post.enqueue(v)
        self._reverse_post.push(v)
    
    def pre(self):
        return self._pre
    
    def post(self):
        return self._post

    def reverse_post(self):
        return self._reverse_post

class Topological:

    def __init__(self, g):
        self._order = None
        cyclefinder = DirectedCycle(g)
        if not cyclefinder.has_cycle():
            dfs = DepthFirstOrder(g)
            self._order = dfs.reverse_post()
    
    def order(self):
        return self._order
    
    def is_dag(self):
        return self._order is not None
    
