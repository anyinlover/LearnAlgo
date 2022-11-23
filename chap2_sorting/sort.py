import sys
import random
from abc import ABC, abstractmethod

class Sort(ABC):

    @abstractmethod
    def sort(self, a):
        pass

    def is_sorted(self, a):
        for i in range(1, len(a)):
            if a[i] < a[i - 1]:
                return False
        return True

class SelectionSort(Sort):

    def sort(self, a):
        for i in range(len(a) - 1):
            min_idx = i
            for j in range(i + 1, len(a)):
                if a[j] < a[min_idx]:
                    min_idx = j
            a[i], a[min_idx] = a[min_idx], a[i]

class InsertionSort(Sort):

    def sort(self, a):
        for i in range(1, len(a)):
            j = i
            while j > 0 and a[j - 1] > a[j]:
                a[j], a[j - 1] = a[j - 1], a[j]
                j -= 1
    
class ShellSort(Sort):
    def sort(self, a):
        k = 1
        while k < len(a):
            k = 3 * k + 1
        while k >= 1:
            k = k // 3
            for i in range(k, len(a)):
                j = i
                while j >= k and a[j - k] > a[j]:
                    a[j], a[j - k] = a[j - k], a[j]
                    j -= k
        
class MergeSort(Sort):
    def _merge(self, a, lo, hi, mid):
        for i in range(lo, hi + 1):
            self.aux[i] = a[i]
        i = lo
        j = mid + 1
        for k in range(lo, hi + 1):
            if i > mid:
                a[k] = self.aux[j]
                j += 1
            elif j > hi or self.aux[i] < self.aux[j]:
                a[k] = self.aux[i]
                i += 1
            else:
                a[k] = self.aux[j]
                j += 1
            
    def _sort(self, a, lo, hi):
        if lo >= hi:
            return
        
        mid = (hi + lo) // 2 
        self._sort(a, lo, mid)
        self._sort(a, mid + 1, hi)
        self._merge(a, lo, hi, mid)

    def sort(self, a):
        self.aux = [0] * len(a)
        self._sort(a, 0, len(a) - 1)

class QuickSort(Sort):
    def _partition(self, a, lo, hi):
        i = lo + 1
        j = hi
        while True:
            while i <= hi and a[i] <= a[lo]:
                i += 1
            while j > lo and a[j] >= a[lo]:
                j -= 1
            if i >= j:
                break
            a[i], a[j] = a[j], a[i]
        a[lo], a[j] = a[j], a[lo]
        return j

    def _sort(self, a, lo, hi):
        if lo >= hi:
            return
        j = self._partition(a, lo, hi)
        self._sort(a, lo, j - 1)
        self._sort(a, j + 1, hi)

    def sort(self, a):
        random.shuffle(a)
        self._sort(a, 0, len(a) - 1)

class Quick3WaySort(Sort):
    def _sort(self, a, lo, hi):
        if lo >= hi:
            return
        lt = lo
        gt = hi
        i = lo + 1
        v = a[lo]
        while i <= gt:
            if a[i] < v:
                a[i], a[lt] = a[lt], a[i]
                i += 1
                lt += 1
            elif a[i] > v:
                a[i], a[gt] = a[gt], a[i]
                gt -= 1
            else:
                i += 1

        self._sort(a, lo, lt - 1)
        self._sort(a, gt + 1, hi)

    def sort(self, a):
        random.shuffle(a)
        self._sort(a, 0, len(a) - 1) 

class HeapSort(Sort):
    def sort(self, a):
        n = len(a)
        for k in reversed(range(1, n//2+1)):
            self._sink(a, k, n)
        while n > 1:
            a[1]


if __name__ == "__main__":
    data = list("SORTEXAMPLE")
    sortion = Quick3WaySort()
    sortion.sort(data)
    assert(sortion.is_sorted(data))
    print(data)    
