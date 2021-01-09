'''
Sum of odd numbers
Given the triangle of consecutive odd numbers:
until all odd numbers from 1 to 99999
'''
def row_sum_odd_numbers(n):
    numbers_list = [num for num in range(1, 100000) if num % 2 == 1]
    start_index = 0
    for number in range(n):
        start_index += number
    end_row = start_index + n
    return sum(numbers_list[start_index:end_row])





triangle_odd = '''
             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
'''
b = triangle_odd.split()
print(row_sum_odd_numbers(5))