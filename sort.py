import sys
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
    
if __name__ == "__main__":
    data = sys.stdin.readline().split()
    sortion = InsertionSort()
    sortion.sort(data)
    assert(sortion.is_sorted(data))
    print(data)    
