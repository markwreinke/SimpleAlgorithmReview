



# This Method finds the ontinuous subarray within an inputlist with the maximum sum of its elements,
# and returns the location and sum value
# Works by using divide and Conquer to split the list into three parts:
#   left side of the list
#   right side of the list
#   crossList that stratles the midpoint
# This method has the  recurrence T(n) = {Theta(1) if n = 1, 2T(n/2) + Theta(n) if n > 1} n being the length of the input lists
# The solution is Theta(n log n) the same as mergeSort
#
# @param inputList - The list to find the subarray of
# @param lowIndex - The beginning of the list to be considered
# @param highIndex - The end of the list to be considered
#
# @return (lowIndex || leftLowIndex || rightLowIndex || crossLowIndex) the low index of the maximumSubarray
# @return(highIndex || leftHighIndex || rightHighIndex || crossHighIndex) the high index of the maximumSubarray
# @return(inputList[lowIndex] || leftSum || rightSum || crossSum) the sum of elements of the maximumSubarray
def FindMaxSubarray(inputList, lowIndex, highIndex):

    if lowIndex == highIndex: # base case - list only has one element
        return([lowIndex, highIndex, inputList[lowIndex]])
    else:
        mid = (highIndex + lowIndex) // 2
        print(mid)

        # Initializing variables to divide the list
        leftLowIndex = lowIndex
        leftHighIndex = mid
        leftSum = 0
        leftSubList = [leftLowIndex, leftHighIndex, leftSum]

        rightLowIndex = mid + 1
        rightHighIndex = highIndex
        rightSum = 0
        rightSubList = [rightLowIndex, rightHighIndex, rightSum]

        crossLowIndex = lowIndex
        crossHighIndex = highIndex
        crossSum = 0
        crossSubList = [crossLowIndex, crossHighIndex, crossSum]

        # Sets the three sublists to find their respective subarrays recursively
        leftSubList = FindMaxSubarray(inputList, lowIndex, mid)
        rightSubList = FindMaxSubarray(inputList, mid + 1, highIndex)
        crossSubList = FindMaxCrossingSubarray(inputList, lowIndex, mid, highIndex)

        # Why can't Python just pass things by reference?
        rightSum = int(rightSubList[2])
        leftSum = int(leftSubList[2])
        crossSum = int(crossSubList[2])

        # Returns the sublist with the highest sum sublist
        if leftSum >= rightSum and leftSum >= crossSum:
            return([leftLowIndex, leftHighIndex, leftSum])
        elif rightSum >= leftSum and rightSum >= crossSum:
            return([rightLowIndex, rightHighIndex, rightSum])
        else:
            return([crossLowIndex, crossHighIndex, crossSum])


# this method finds the max subarray that crosses the midpoint of an array
# This method takes BTheta(n) timeas the for loops take (mid-low +1) + (high-mid) = high - low +1 = n iterations
# @param inputList - this is the array being studied
# @param lowIndex - this is the beginning of the array
# @param midIndex - this is the midpoint of the array
# @param highIndex - the end of the array
#
# @return maxLeftIndex - the beginning of the max subarray crossing the midpoint
# @return maxRightIndex - the end of the max subarray of the subarray crossing the midpoint
# @return leftSum+rightSum the value of the max subarray
def FindMaxCrossingSubarray(inputList, lowIndex, midIndex, highIndex):
    #Finding the maximum subarray of the left half
    leftSum = -10000
    sum = 0
    maxLeftIndex = 0
    for i in range(midIndex, lowIndex -1, -1):
        print("i = ",i, " midIndex = ", midIndex)
        sum += inputList[i]
        if sum > leftSum:
            leftSum = sum
            print("lefsum = ", leftSum)
            maxLeftIndex = i

    #Finding the maximum subarray of the right half
    rightSum = -10000
    sum = 0
    rightMaxIndex = 0
    for j in range(midIndex + 1, highIndex + 1):
        print("j = ", j)
        sum += inputList[j]
        if sum > rightSum:
            rightSum = sum
            print("rightSum = ", rightSum)
            rightMaxIndex = j

    print("maxLeftIndex = ", maxLeftIndex, " rightMaxIndex = ", rightMaxIndex, " leftSum+rightSum = " , leftSum+rightSum)
    return([maxLeftIndex, rightMaxIndex, leftSum+rightSum])

# Testing
test = [2,13,-15,5,7]
blah = FindMaxSubarray(test, 0, len(test)-1)
print(blah)
