#! PYTHON 3
'''
Given an array of ints, return True if one of the first 4 elements in the array
is a 9. The array length may be less than 4.


array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False

'''

def array_front9(nums):
    '''TRUE'''
    tamano = len(nums)
    for index in range(tamano):    
        if index < 4 and nums[index] == 9:
            return True
    return False

lista = [1,2,9,4,5,6]

print(array_front9(lista))
