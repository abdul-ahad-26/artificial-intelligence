# How to extract all number between a given range from a numpy array
import numpy as np

numbers = np.array([1, 3, 4, 6, 8, 10])

def extract_numbers(arr, lower_bound, upper_bound):
    filterd = np.where((upper_bound >= arr) & (arr >=lower_bound))
    return arr[filterd]

extracted_numbers = extract_numbers(numbers, 1,7)
print(extracted_numbers)