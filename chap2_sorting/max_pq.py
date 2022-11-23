class MaxPQ:

    def __init__(self, max_n):
        self._pq = [None] * (max_n + 1)
        self._n = 0

    def insert(self, v):
        self._n += 1
        self._pq[self._n] = v
        self._swim(self._n)

    def max(self):
        return self._pq[1]

    def del_max(self):
        amax = self._pq[1]
        self._pq[1] = self._pq[self._n]
        self._pq[self._n] = None
        self._n -= 1
        self._sink(1)
        return amax

    def is_empty(self):
        return self._n == 0

    def size(self):
        return self._n

    def _swim(self, k):
        while k > 1 and self._pq[k//2] < self._pq[k]:
            self._pq[k//2], self._pq[k] = self._pq[k], self._pq[k//2]
            k //= 2
    
    def _sink(self, k):
        while k * 2 <= self._n:
            j = k * 2
            if j < self._n and self._pq[j] < self._pq[j+1]:
                j += 1
            if self._pq[k] >= self._pq[j]:
                break
            self._pq[k], self._pq[j] = self._pq[j], self._pq[k]
            k = j


if __name__ == "__main__":
    max_pq = MaxPQ(10)
    datas = [4, 5, 7, 2, 1, 6, 3]
    for d in datas:
        max_pq.insert(d)
    while not max_pq.is_empty():
        print(max_pq.del_max())