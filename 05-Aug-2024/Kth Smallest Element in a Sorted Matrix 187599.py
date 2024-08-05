# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Heap:
    def __init__(self):
        self.heap = [None]

    def push(self, num):
        self.heap.append(num)
        if len(self.heap) > 2:
            i = len(self.heap) - 1
            while i > 1 and self.heap[i] > self.heap[i // 2]:
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
                i = i // 2

    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        
        root = self.heap[1]
        self.heap[1] = self.heap.pop()      
        i = 1
        while True:
            left = 2 * i
            right = 2 * i + 1
            largest = i
            if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                largest = left
            if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != i:
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                i = largest
            else:
                break
        return root

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        hp = Heap()
        for lis in matrix:
            for n in lis:
                hp.push(n)
                while len(hp.heap) > (k + 1):
                    hp.pop()
        return hp.heap[1]


        