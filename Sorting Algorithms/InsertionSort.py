# insertionSort is O(n^2) --> for each iteration of the for loop, there is up to n iterations of the while loop
# All values in [0....j-1] are sorted, and all values in [j+1....n] are unsorted.

def insertionSort(unsortedList):
    # The index j indicates the key, the value being evaluated/moved
    for j in range(1, len(unsortedList)):
        key = unsortedList[j]
        #  i is the index in which the key is being compared to for its location data. i is a value in the
        # "sorted part' of the list"
        i = j-1
        # This while loop basically pushes all of the values larger
        #than the key over to the right, in order to make room for the
        #key to be in it's sorted spot
        while i >= 0 and unsortedList[i] > key:
            unsortedList[i+1] = unsortedList[i]
            i -= 1
        # now that there is a correct spot available in the list, the key is placed
        unsortedList[i+1] = key


# testing
test = [5,3,1,6,3,8,4,9,4,8,34,21,3,6]
insertionSort(test)
print(test)
