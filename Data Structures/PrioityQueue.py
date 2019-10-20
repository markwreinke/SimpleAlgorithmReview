
def HeapMaximum(array):
    return array[0];

def HeapExtractMax(array):
    if len(array) < 1:
        raise HeapError("Heap underflow")
