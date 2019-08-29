# insertionSort is O(n^2) --> for each iteration of the for loop, there is up to n iterations of the while loop

def insertionSort(unsortedList):
    # The index j indicates the key, the value being evaluated/moved
    for j in range(2, len(unsortedList)):
        key = unsortedList[j]
        i = j-1
        while i > 0 and unsortedList[i] > key:
            unsortedList[i+1] = unsortedList[i]
            i -= 1

        unsortedList[i+1] = key


test = [1,6,3,8,4,9,4,8,34,21,3,6]
insertionSort(test)
print(test)
