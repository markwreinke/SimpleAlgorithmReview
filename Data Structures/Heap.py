import math

# A class to manage a maxHeap data opbject, with the ability to add an remove elements.
class HeapArray():

    # Constructor to setup the heap and heapSize.
    def __init__(self, array):
        self.heap = array
        self.heapSize = len(array) - 1
        self.heapSize = self.BuildMaxHeap(self)

    # returns the maximum element of the heap
    def HeapMaximum(self, heap):
        return heap[0];

    # A function to remove the max element, calls MaxHeapify to maintain the maxHeap property
    def HeapExtractMax(self, heapArray):
        if heapArray.heapSize < 0:
            raise HeapError("Heap underflow")
        max = heapArray.heap[0]
        heapArray.heap[0] = heapArray.heap[heapArray.heapSize]
        heapArray.heapSize = heapArray.heapSize - 1
        self.MaxHeapify(heap, 0)
        return max, heapArray

    # A subfunction for MaxHeapInsert, it inputs a key into the heap, adjusting the heap to maintain its maxheap property
    def HeapIncreaseKey(self, heapArray, index, key):
        if key < heapArray.heap[index]:
            raise HeapError("New key is smaller than current key")
        heapArray.heap[index] = key
        while index > 0 and heapArray.heap[HeapArray.ParentNode(index)] < heapArray.heap[index]:
            heapArray.heap[index], heapArray.heap[HeapArray.ParentNode(index)] = heapArray.heap[HeapArray.ParentNode(index)], heapArray.heap[index]
            index = HeapArray.ParentNode(index)

        return heapArray

    # Inserts an element (here called a key) into a maxHeap
    def MaxHeapInsert(self, heapArray, key):
        heapArray.heapSize += 1
        if(heapArray.heapSize == len(heapArray.heap) - 1):
            heapArray.heap.append(float("-inf"))
        else:
            heapArray.heap[heapArray.heapSize] = float("-inf")
        heapArray = self.HeapIncreaseKey(heapArray, heapArray.heapSize, key)

        return heapArray


    # Determines the index of the parent node of the input index.
    def ParentNode(i):
        return math.floor(i/2)

    # Determins the index of the left child of the input index.
    def LeftNode(i):
        return 2*i + 1

    # Determines the index of the right child of the input index.
    def RightNode(i):
        return 2*i + 2

    # This function takes in the array, the heapsize to be considered, and the index of the end of the input heap. This method has O(lg n) runtime.
    def MaxHeapify(self, heapArray, index):
        leftNode  = HeapArray.LeftNode(index)
        rightNode = HeapArray.RightNode(index)

        # If the left node exists and is larger than the end node, than it is recorded as the largest node, else the end node is recorded as the largest node.
        if leftNode <= heapArray.heapSize and heapArray.heap[leftNode] > heapArray.heap[index]:
            largest = leftNode
        else:
            largest = index

        # If the right node exists and is larger than the node currently marked as the largest, then the right node is recorded as the largest node.
        if rightNode <= heapArray.heapSize  and heapArray.heap[rightNode] > heapArray.heap[largest]:
            largest = rightNode

        #If the largest node isn't last node, then it is exchanged with the last one, and runs heapify on the remaining branch of the tree.
        if largest != index:
            heapArray.heap[index], heapArray.heap[largest] = heapArray.heap[largest], heapArray.heap[index]
            heapArray = self.MaxHeapify(heapArray, largest)

        return heapArray

    # Turns the heap into a maxHeap. Runs MaxHeapify on the first n/2 nodes (since the last n/2 nodes are already 1 element heaps).
    #   This runs in O(n) time.
    def BuildMaxHeap(self, heapArray):
        for i in range(math.floor((heapArray.heapSize)/2), -1, -1):
            heapArray = self.MaxHeapify(heapArray, i)

        return heapArray

    # An alternate implementation of BuildMaxHeap. Turns the heap into a maxHeap. Runs MaxHeapify on the first n/2 nodes (since the last n/2 nodes are already 1 element heaps).
    #   Does not create the same exact tree as BuildMaxHeap
    #   This runs in O(n lg n) time.
    def BuildMaxHeapAlt(self, heapArray):
        heapArray.heapSize = 0
        for index in range(1, len(heapArray.heap) - 1):
            heapArray = self.MaxHeapInsert(heapArray, heapArray.heap[index])

        return heapArray



a = HeapArray([1,2,4,3, 15, 17, 0, 1, 5,6])
print("a = ", a.heap)

b = HeapArray([1,2,4,3, 15, 17, 0, 1, 5,6])
print("b = ", b.heap)


a = a.BuildMaxHeap(a)
print(a.heap)

b = b.BuildMaxHeapAlt(b)
print(b.heap)
