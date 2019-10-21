
def HeapMaximum(array):
    return array[0];

def HeapExtractMax(array):
    heapSize = len(array) -1
    if heapSize < 0:
        raise HeapError("Heap underflow")

    max = array[0]
    array[0] = array[heapSize]
    heapSize = heapSize - 1
    MaxHeapify(array, heapSize, 0)
    return max

def HeapIncreaseKey(array, index, key):
    if key < array[index]:
        raise HeapError("New key is smaller than current key")
    array[index] = key
    while i > 0 and array[ParentNode(index)] < array[index]:
        temp = array[index]
        array[index] = array[ParentNode(index)]
        array[ParentNode(index)] = temp
        indext = ParentNode(index)




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
def MaxHeapify(array, heapSize, index):
    leftNode  = LeftNode(index)
    rightNode = RightNode(index)
    # If the left node exists and is larger than the end node, than it is recorded as the largest node, else the end node is recorded as the largest node.
    if leftNode <= heapSize and array[leftNode] > array[index]:
        largest = leftNode
    else:
        largest = index

    # If the right node exists and is larger than the node currently marked as the largest, then the right node is recorded as the largest node.
    if rightNode <= heapSize  and array[rightNode] > array[largest]:
        largest = rightNode

    #If the largest node isn't last node, then it is exchanged with the last one, and runs heapify on the remaining branch of the tree.
    if largest != index:
        temp = array[index]
        array[index] = array[largest]
        array[largest] = temp
        MaxHeapify(array, heapSize, largest)
