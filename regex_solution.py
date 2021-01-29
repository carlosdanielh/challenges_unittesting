'''
Log
['#', '!']
'\n' should equal ''
Log
#
['#', '!']
'\n' should equal ''
Log
§
['#', '§']
'' should equal '\n'
Log
apples, pears # and bananas
grapes
bananas !apples
[]
STDERR
Traceback (most recent call last):
  File "main.py", line 15, in <module>
    Test.assert_equals(solution("apples, pears # and bananas\ngrapes\nbananas 
    !apples", []), "apples, pears # and bananas\ngrapes\nbananas !apples")
  File "/home/codewarrior/solution.py", line 7, in solution
    if markers[counter] in string:
IndexError: list index out of range
'''


def solution(string, markers):

    is_in_string = False
    for element in markers:
        if element in string:
            is_in_string = True
            break
            
    if is_in_string:
        markers_in_string = True
        counter = 0
        while markers_in_string:
            if markers[counter] in string:
                start_point = string.find(' ' + markers[counter])
    
                if start_point == -1:
                    start_point = string.find(markers[counter])
    
                if string[start_point:].find('\n') != -1:
                    end_point = string[start_point:].find('\n') + start_point
                    delete = string[start_point:end_point]
                else:
                    delete = string[start_point:] 
    
                string = string.replace(delete, '', 1)
    
            counter += 1
            if counter == len(markers):
                for element in markers:
                    if element in string:
                        markers_in_string = True
                        counter = 0
                        break
                    else:
                        markers_in_string = False

        if len(string)==1 and string=='\n':
            return '\n'
        if string.endswith('\n'):
            return string
        else:
            return string.rstrip()  
    return string
