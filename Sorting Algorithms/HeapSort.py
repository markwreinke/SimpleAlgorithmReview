# The HeapSort algorithm that sorts an array by treating it as a tree, repetitively turning it into max trees, until it is sorted.
import math

# The main funtion, first calls BuildMaxHeap in order to turn the array into a max tree
#   Then, it steps down the array from the end, echanging the first element(which is always the largest, due to being a max tree)
#   with the index, until the index is at position 1, in which the array is sorted.
def HeapSort(array):
    heapSize = BuildMaxHeap(array)

    for i in range(len(array) - 1, 0, -1):
        temp = array[0]
        array[0] = array[i]
        array[i] = temp
        heapSize -= 1
        MaxHeapify(array, heapSize, 0)

# Determines the index of the parent node of the input index.
def parentNode(i):
    return math.floor(i/2)

# Determins the index of the left child of the input index.
def LeftNode(i):
    return 2*i + 1

# Determines the index of the right child of the input index.
def RightNode(i):
    return 2*i + 2

# This function takes in the array, the heapsize to be considered, and the index of the end of the input heap.
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

# Determines the heapSize of the entire array, then runs MaxHeapify on the first n/2 nodes (since the last n/2 nodes are already 1 element heaps)
def BuildMaxHeap(array):
    heapSize = len(array) -1
    for i in range(math.floor(heapSize/2), -1, -1):
        MaxHeapify(array, heapSize, i)

    return heapSize

a = [4,1,3,0,16,9,0,19,8,7]
HeapSort(a)
print(a)
