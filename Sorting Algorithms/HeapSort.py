import math


def HeapSort(array):
    heapSize = BuildMaxHeap(array)
    for i in range(len(array), 2, -1):
        temp = array[1]
        array[1] = array[i]
        array[i] = temp
        heapSize -= 1
        MaxHeapify(array, heapSize, 1)


def parentNode(i):
    return math.floor(i/2)

def LeftNode(i):
    return 2*i - 1

def RightNode(i):
    return 2*i

def MaxHeapify(array, heapSize, index):
    print( "index = ", index, "array = ", array)
    leftNode  = LeftNode(index)
    rightNode = RightNode(index)
    print("leftNode = ", leftNode, " rightNode = ", rightNode)
    if leftNode <= heapSize and array[leftNode] > array[index]:
        largest = leftNode
    else:
        largest = index

    if rightNode <= heapSize and array[rightNode] > array[largest]:
        largest = rightNode

    if largest !=index:
        temp = array[index]
        array[index] = array[largest]
        array[largest] = temp
        MaxHeapify(array, heapSize, largest)

def BuildMaxHeap(array):
    heapSize = len(array)
    for i in range(math.floor(heapSize/2), 1, -1):
        MaxHeapify(array, heapSize, i)

    return heapSize

a = [4,1,3,2,16,9,10,14,8,7]
HeapSort(a)
print(a)
