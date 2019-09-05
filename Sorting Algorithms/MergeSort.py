

def mergeSort(unsortedList):
    if len(unsortedList) <= 1:
        return unsortedList
    else:
        left, right = splitList(unsortedList)
        return merge(mergeSort(left), mergeSort(right))



def splitList(inputList):
    midpoint = len(inputList)//2
    return inputList[:midpoint], inputList[midpoint:]

# Merges two sorted lists
# Theta(n) time  n = {length of leftList + length of rightList}
def merge(leftList, rightList):

    # Block handling if one or both of the input arrays are empty
    if len(leftList) == 0:
        return rightList
    elif len(rightList) == 0:
        return leftList

    index_left = 0
    index_right = 0
    merged_list = []
    final_list_len  = len(leftList) + len(rightList)
    while len(merged_list) < final_list_len:
        if(index_right < len(rightList) and leftList[index_left] <= rightList[index_right]):
            merged_list.append(leftList[index_left])
            index_left += 1
        else:
            merged_list.append(rightList[index_right])
            index_right += 1
        if(index_left == len(leftList)):
            merged_list += (rightList[index_right:])
        elif(index_right == len(rightList)):
            merged_list += (leftList[index_left:])
    return merged_list



left = [1,3,6,8,9]
right = [2,4,4,6,7]
merged = merge(left, right)
print(merged)

left = [9]
right = [3]
merged = merge(left, right)
print(merged)

inputList = [1,3,6,8,9,2,4,4,6,7,15]
listSplat = splitList(inputList)
print(listSplat)
merged2 = merge(listSplat[0], listSplat[1])
print(merged2)

inputList = [6,5,7,8,9,2,4,2,6,7,1]
inputList = mergeSort(inputList)
print(inputList)
