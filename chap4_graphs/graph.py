from chap1_fundamentals.bag import Bag

class Graph:
    def __init__(self, v):
        self._v= v
        self._e = 0
        self._adj = [Bag() for _ in range(v)]

    def __str__(self):
        s = f"{self.v()} vertices, {self.e()} edges\n"
        s += "\n".join(" ".join(str(w) for w in self.adj(v)) for v in range(self.v()))
        return s

    def v(self):
        return self._v

    def e(self):
        return self._e

    def add_edge(self, v, w):
        self._adj[v].add(w)
        self._adj[w].add(v)
        self._e += 1

    def adj(self, v):
        return self._adj[v]
    
    def degree(self, v):
        return self.adj(v).size()
    
    def max_degree(self):
        best = 0
        for v in range(self.v()):
            best = max(self.degree(v), best)
        return best
        
    def avg_degree(self):
        return 2 * self.e() / self.v()

    def number_of_self_loops(self):
        count = 0
        for v in range(self.v()):
            for w in self.adj(v):
                if v == w:
                    count += 1
        
        return count // 2


if __name__ == "__main__":
    graph = Graph(10)
    for v in range(3):
        for w in range(4):
            if v != w:
                graph.add_edge(v, w)
    print(graph.degree(2))
    print(graph.max_degree())
    print(graph.avg_degree())
    print(graph.number_of_self_loops())
    print(graph.v())
    print(graph.e())
