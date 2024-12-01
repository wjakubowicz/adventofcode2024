import os
from collections import Counter

def read_file_to_arrays(filename):
    array1 = []
    array2 = []

    with open(filename, 'r') as file:
        for line in file:
            values = line.split()
            array1.append(int(values[0]))
            array2.append(int(values[1]))

    return array1, array2

filename = os.path.expandvars(r'%USERPROFILE%\Downloads\advent01.txt')
array1, array2 = read_file_to_arrays(filename)

# print("Array 1:", array1)
# print("Array 2:", array2)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

sorted_array1 = quicksort(array1)
sorted_array2 = quicksort(array2)

# print("Sorted Array in Ascending Order:")
# print(sorted_array1)
# print(sorted_array2)

def subtract_arrays(array1, array2):
    return [a - b for a, b in zip(array1, array2)]

subtracted_array = subtract_arrays(sorted_array1, sorted_array2)
absolute_subtracted_array = [abs(x) for x in subtracted_array]
sum_of_subtracted_elements = sum(absolute_subtracted_array)

# print("Absolute Subtracted Array:", absolute_subtracted_array)
print("Sum of Absolute Subtracted Elements:", sum_of_subtracted_elements)

def similarity():
	count_array2 = Counter(array2)
	similarity_score = sum(num * count_array2[num] for num in array1)
	return similarity_score

print("Similarity Score:", similarity())