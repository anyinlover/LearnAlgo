from graph import Graph
class Digraph(Graph):

    def add_edge(self, v, w):
        self._adj[v].add(w)
        self._e += 1

    def reverse(self):
        r = Digraph(self._v)
        for v in range(self._v):
            for w in self._adj[v]:
                r.add_edge(w, v)
        return r