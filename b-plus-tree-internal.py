import bisect

def insert(arr, data):
    bisect.insort(arr, data, key = lambda d: d.k)

def split(arr):
    midpoint = len(arr) // 2
    arr2 = arr[midpoint:]
    return arr[:midpoint], arr2

class Data:
    def __init__(self, k, payload):
        self.k = k
        self.payload = payload

class InternalNode:
    def __init__(self, next=None, max_size = 0):
        self.arr = []
        self.next = next
        self.max_size = max_size

    def insert(self, data):
        if len(self.arr) < self.max_size:
            insert(self.arr, data)
            return
        
        self.arr, arr2 = split(self.arr)

        if data.k < arr2[0]:
            insert(self.arr, data)
        else:
            insert(arr2, data)


