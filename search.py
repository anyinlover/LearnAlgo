from abc import ABC, abstractmethod

class Search(ABC):

    @abstractmethod
    def __init__(self, g, s):
        pass
    
    @abstractmethod
    def marked(self, v):
        pass

    @abstractmethod
    def count(self):
        pass

class DepthFirstSearch(Search):

    def __init__(self, g, s):
        self._marked = [False] * g.v()
        self._count = 0
        self._dfs(g, s)

    def _dfs(self, g, v):
        self._marked[v] = True
        self._count += 1
        for w in g.adj(v):
            if not self._marked[w]:
                self._dfs(g, w)

    def marked(self, v):
        return self._marked[v]

    def count(self):
        return self._count

