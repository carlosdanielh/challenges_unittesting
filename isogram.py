def is_isogram(string):
    lower_string = string.lower()

    for letter in lower_string:
        if lower_string.count(letter) == 2:
            return False
    return True


def duplicate_count(text):
    # list_counted = []
    # word = text.lower()
    # count = 0

    # for letter in word:
    #     if word.count(letter) > 1 and letter not in list_counted:
    #         count += 1
    #         list_counted.append(letter)
    #         print(list_counted)
    # return count
############################################
    # count = 0
    # for c in set(text.lower()):
    #     if text.lower().count(c) > 1:
    #         count += 1
    # return count
############################################
# from collections import Counter
#     return sum(1 for c, n in Counter(text.lower()).iteritems() if n > 1)
############################################
# return len([c for c in set(s.lower()) if s.lower().count(c)>1])


print(duplicate_count('carclossSbbBSSiiiSS'))
print(is_isogram('Dermatoglyphics'))

# Test.assert_equals(is_isogram("Dermatoglyphics"), True )
# Test.assert_equals(is_isogram("isogram"), True )
# Test.assert_equals(is_isogram("aba"), False, "same chars may not be adjacent" )
# Test.assert_equals(is_isogram("moOse"), False, "same chars may not be same case" )
# Test.assert_equals(is_isogram("isIsogram"), False )
# Test.assert_equals(is_isogram(""), True, "an empty string is a valid isogram" )