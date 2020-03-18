import sys
class MaxBinaryHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        iToFind = self.heap.index(i)
        return int((iToFind - 1)/2)
    
    def leftChild(self, i):
        iToFind = self.heap.index(i)
        return int((2 * iToFind) + 1)
    
    
    def rightChild(self, i):
        iToFind = self.heap.index(i)
        # print(int((2 * iToFind) + 2))
        return int((2 * iToFind) + 2)    
    
    def swap(self, arr, num1, num2):
        temp = arr.index(num2)
        arr[arr.index(num1)] = num2
        arr[temp] = num1
        
        
        
    def size(self):
        return len(self.heap)
    
    def maxHeapify(self, i):
        root = self.heap[self.heap.index(i)]
        leftChild = rightChild = -1
        

        if self.leftChild(i) < len(self.heap) :
            leftChild = self.heap[self.leftChild(i)]
        else:
            leftChild = -1
    
        if self.rightChild(i) < len(self.heap):
            rightChild = self.heap[self.rightChild(i)]
        else:
            rightChild = -1
        
        largest = max([root, leftChild, rightChild])
        
        if largest != root:
            if largest == leftChild:
                self.swap(self.heap, root, leftChild)
            elif largest == rightChild:
                self.swap(self.heap, root, rightChild)
            self.maxHeapify(largest)
        else:
            pass
    
    
    def insert(self, i):
        self.heap.append(i)      
        n = self.size()  
        
        while ( i != self.heap[0] and self.heap[self.parent(i)] < self.heap[self.heap.index(i)] ):
            self.swap(self.heap, self.heap[self.heap.index(i)], self.heap[self.parent(i)],)
            i = self.heap[self.heap.index(i)]
            
        
    def extractMax(self):
        max = self.heap[0]
        self.heap.remove(self.maxLookup())
        self.maxHeapify(self.heap[0])
        return max
    
    def maxLookup(self):
        return self.heap[0]

    def delete(self, i):
        self.heap.remove(self.heap[i])
        self.maxHeapify(self.heap[0])   

heap = MaxBinaryHeap()

for line in sys.stdin:
    line = line.split()
    
    if "size" in line:
        print(heap.size())
    elif "insert" in line:
        heap.insert(int(line[1]))
    elif "maxLookup" in line:
        print(heap.maxLookup())
    elif "extractMax" in line:
        heap.extractMax()
    elif "delete" in line:
        # print("del", int(line[1]))
        heap.delete(int(line[1]))
        