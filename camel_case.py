def to_camel_case(text):
    if text != '':
        text = text.replace('-', ' ').replace('_', ' ')
        is_lower_first_letter = False
        
        if text.split(' ')[0][0].islower():
            is_lower_first_letter = True

        list_word = text.split()
        text = ' '.join(list_word).replace(' ', '')

        if is_lower_first_letter:
            list_word = list(text)
            list_word[0] = list_word[0].lower()
            return ''.join(list_word)
        else:
            return text
    else:
        return ''


def to_camel_case1(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')

print(to_camel_case('A_Cat-is-Omoshiroi'))

print(to_camel_case1('A_Cat-is-Omoshiroi'))
###############################################################################
# test.describe("Testing function to_camel_case")
# test.it("Basic tests")
# test.assert_equals(to_camel_case(''), '', "An empty string was provided but not returned")
# test.assert_equals(to_camel_case("the_stealth_warrior"), "theStealthWarrior", "to_camel_case('the_stealth_warrior') did not return correct value")
# test.assert_equals(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior", "to_camel_case('The-Stealth-Warrior') did not return correct value")
# test.assert_equals(to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did not return correct value")


# Kata



# def to_camel_case(s):
#     return s[0] + s.title().translate(None, "-_")[1:] if s else s
# 1 similar code variation is grouped with this oneHide Variations

# def to_camel_case(s):
#     return s[0] + s.title().translate(None, "-_")[1:] if s else s
# Best Practices248Clever577
# 481ForkCompare with your solutionLink
# SwingKing, learningpython123, Chykki, Solunaticzz, AnastasiiaDemenkova, YuliaH
# def to_camel_case(text):
#     removed = text.replace('-', ' ').replace('_', ' ').split()
#     if len(removed) == 0:
#         return ''
#     return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])
# 2 similar code variations are grouped with this oneShow Variations

# Best Practices79Clever61
# 8ForkCompare with your solutionLink
# bse, ubeduris1, elliotchance, sohaya, dev_y_b, WillKen, trigger321, 11swswsw, Elijah , scaltunsoy
# import re
# def to_camel_case(text):
#     return re.sub('[_-](.)', lambda x: x.group(1).upper(), text)
# 3 similar code variations are grouped with this oneShow Variations

# Best Practices42Clever91
# 5ForkCompare with your solutionLink
# vokar, sbeverton, Herguejuan, svetkolukk, Ingeniero27, dauletyka, SerBeg, user6538049, Eselsmesse, svetusha1975 (plus 1 more warriors)
# def to_camel_case(text):
#     return text[:1] + text.title()[1:].replace('_', '').replace('-', '')
# 3 similar code variations are grouped with this oneShow Variations

# Best Practices37Clever54
# 5ForkCompare with your solutionLink
# jolaf, HIGH0101
# from re import compile as reCompile

# PATTERN = reCompile(r'(?i)[-_]([a-z])')

# def to_camel_case(text):
#     return PATTERN.sub(lambda m: m.group(1).upper(), text)
# 1 similar code variation is grouped with this oneShow Variations

# Best Practices18Clever9
# 1ForkCompare with your solutionLink
# daddepledge, BobrovAE308, Kolosov309, alex.zhangxl007
# def to_camel_case(text):
#     return text[0] + ''.join([w[0].upper() + w[1:] for w in text.replace("_", "-").split("-")])[1:] if text else ''
# 1 similar code variation is grouped with this oneShow Variations

# Best Practices16Clever109
# 14ForkCompare with your solutionLink
# slicklash, berylluolan, zornix
# def to_camel_case(text):
#     words = text.replace('_', '-').split('-')
#     return words[0] + ''.join([x.title() for x in words[1:]])
# 1 similar code variation is grouped with this oneShow Variations

# Best Practices15Clever18
# 0ForkCompare with your solutionLink
# cooperbaerseth, peterg27
# def to_camel_case(text):
#     cap = False
#     newText = ''
#     for t in text:
#         if t == '_' or t == '-':
#             cap = True
#             continue
#         else:
#             if cap == True:
#                 t = t.upper()
#             newText = newText + t
#             cap = False
#     return newText
# Best Practices10Clever14
# 1ForkCompare with your solutionLink
# lobeta
# def to_camel_case(text):
#     return "".join([i if n==0 else i.capitalize() for n,i in enumerate(text.replace("-","_").split("_"))])
# Best Practices7Clever8
# 0ForkCompare with your solutionLink
# BrookShuihuaLee
# import re
# def to_camel_case(text):
#     return reduce(lambda p, n: p + n[0].upper() + n[1:], re.split('[-_]', text))
# Best Practices6Clever26
# 2ForkCompare with your solutionLink
# orvill
# import re
# def to_camel_case(text):
#     arr = re.split('-|_', text)
#     return ''.join(arr[:1] + [t.title() for t in arr[1:]])
    
    
# Best Practices5Clever2
# 0ForkCompare with your solutionLink
# Edwin.01
# def to_camel_case(text):
#     return ''.join(x if text.index(x) == 0 else x.capitalize() for x in text.replace('-', ' ').replace('_', ' ').split())
# Best Practices4Clever9
# 0ForkCompare with your solutionLink
# betegelse
# from re import findall
# def to_camel_case(text):
#     text = findall(r"[^-_]+", text)
#     return text[0] + "".join(w.capitalize() for w in text[1:]) if text else ""
# Best Practices4Clever2
# 0ForkCompare with your solutionLink
# SilvestrePerret
# import re

# def to_camel_case(text):
#     words = re.split(r'[-_]', text)
#     words[1:] = list(map(str.capitalize, words[1:]))
#     return "".join(words)
# Best Practices4Clever1
# 0ForkCompare with your solutionLink
# ilovelynn
# def to_camel_case(text):
#     import re
#     return re.sub('[-_](.)',lambda x:x.group()[1].upper(),text)
# Best Practices4Clever1
# 0ForkCompare with your solutionLink
# Vladimir Kaigorodov
# def to_camel_case(text):
#     return text[0] + text.title().translate(str.maketrans('', '', '-_'))[1:] if text else ''
# Best Practices4Clever0
# 0ForkCompare with your solutionLink
# MangNguyen
# def to_camel_case(text):
#     return ''.join(ch if i == 0 else ch.title() for i, ch in enumerate(text.replace('_','-').split('-')))
# Best Practices4Clever0
# 0ForkCompare with your solutionLink
# mesolaries, maha4321
# import string
# def to_camel_case(text):
#     if text != '':
#         first = text[0]
#         text = text.title()
#         text = first + text[1:]
#         for i in text:
#             if i in string.punctuation:
#                 text = text.replace(i, '')
#         return text
#     return text
# 1 similar code variation is grouped with this oneShow Variations

# Best Practices3Clever0
# 0ForkCompare with your solutionLink
# mjjbycicle
# def to_camel_case(text):
#     if text=='':
#         return ''
#     res=[]
#     lst='_'.join(text.split('-')).split('_')
#     print(lst)
#     for i in range(len(lst)):
#         if i==0:
#             res.append(lst[i])
#         else:
#             n=[]
#             l=lst[i][:]
#             for x in range(len(lst[i])):
#                 if x==0:
#                     n.append(l[0].upper())
#                 else:
#                     n.append(l[x])
#             res.append(''.join(n))
#     return ''.join(res)
                    
# Best Practices2Clever2
# 0ForkCompare with your solutionLink
# W_2004
# import re

# def to_camel_case(text):
#     return re.sub('[_-](.)',lambda c:c[1].upper(),text)
# Best Practices2Clever0
# 0ForkCompare with your solutionLink
# karlatallah21
# def to_camel_case(text):
#     if text.replace('_', '').replace('-', '').istitle():
#         return text.title().replace('_', '').replace('-', '')
#     return text[0] + text.title().replace('_', '').replace('-', '')[1:] if text != '' else ''
# Best Practices2Clever0
# 0ForkCompare with your solutionLink
# CBoJI
# def to_camel_case(text):
#     words = text.replace('_', '-').split('-')
#     return ''.join([words[0]] + list(map(lambda i: i.title(), words[1:])))
# Best Practices2Clever0
# 0ForkCompare with your solutionLink
# URL 404
# import re
# def to_camel_case(t):
#     return re.split('-|_',t)[0]+''.join(map(lambda _: _.capitalize(),re.split('-|_',t)[1:]))
# Best Practices2Clever0
# 0ForkCompare with your solutionLink
# orangedavy
# def to_camel_case(s):
#     import re
#     return re.sub('[-_]([A-Za-z])', lambda m: m.group(1).upper(), s)
# Best Practices2Clever0
# 0ForkCompare with your solutionLink
# NunoDEV
# def to_camel_case(text):
#     text_lst = [letter for letter in text]
#     for i in range(len(text_lst)):
#         if i > 0:
#             if text_lst[i] == '-' or text_lst[i] == '_':
#                 text_lst[i+1] = text_lst[i+1].upper()
#                 text_lst[i] = ''
#     return ''.join(text_lst)
    
# Best Practices1Clever2
# 0ForkCompare with your solutionLink
# djkat
# def to_camel_case(text):
#     text=text.replace('_',' ').replace('-', ' ').split(' ')
#     caps=[text[0]]
#     for t in text[1::]:
#         caps.append(t[0].upper() + t[1::])
#     return "".join(caps)
# Best Practices1Clever2
# 0ForkCompare with your solutionLink
# falek-marcin
# from re import split

# def to_camel_case(text: str) -> str:
#     """ Converts dash/underscore delimited words into camel casing. """
#     converted_text = "".join(map(str.title, split("[-_]", text)))
#     return text[0] + converted_text[1:] if text else text
# Best Practices1Clever0
# 0ForkCompare with your solutionLink
# romaas
# import re
# def to_camel_case(text):
#     #your code here
#     if len(text) == 0:
#         return ''
    
#     if text.find('_') != -1: # found
#         text = text.split('_')
#         re_text = text[0] 
#         length = len(text)
#         i = 1
#         print(length)
#         while i < length: 
#             re_text += text[i].capitalize()
#             i  += 1
#         print(re_text)
#         if re_text.find('-') == -1: # not found    
#             return re_text
#         else:
#             re_text = re_text.split('-')
#             re_text_1 = re_text[0] 
#             length = len(re_text)
#             print(re_text)
#             i = 1
#             while i < length:
#                 cap_list = []
#                 cap_list = re.findall('[a-zA-Z][^A-Z]*', re_text[i])
#                 j = 0
#                 c_length = len(cap_list)
#                 print("cap_list is ")
#                 print(cap_list)
#                 if c_length !=0:
#                     while j  < c_length:
#                         re_text_1 += cap_list[j].capitalize()
#                         j  +=1
#                 else:
#                     re_text_1  += re_text[i].capitalize()
#                 i  += 1
#             print(re_text_1)
#             return re_text_1
            

#     if  text.find('-') != -1: # found
#         text = text.split('-')
#         re_text = text[0] 
#         length = len(text)
#         i = 1
#         while i < length:  
#             re_text += text[i].capitalize()
#             i  += 1
#         if re_text.find('_') == -1: # not found    
#             return re_text
#         else:
#             re_text_1 = re_text.split('_')
#             re_text_1 = re_text[0] 
#             length = len(re_text)
#             i = 1
#             while i < length:
#                 cap_list = []
#                 cap_list = re.findall('[a-zA-Z][^A-Z]*', re_text[i])
#                 j = 0
#                 c_length = len(cap_list)
#                 print("cap_list is ")
#                 print(cap_list)
#                 if c_length !=0:
#                     while j  < c_length:
#                         re_text_1 += cap_list[j].capitalize()
#                         j  +=1
#                 else:
#                     re_text_1  += re_text[i].capitalize()
#                 i  += 1
#             print(re_text_1)
#             return re_text_1            
# Best Practices1Clever0
# 0ForkCompare with your solutionLink
# romaas
# import re
# def to_camel_case(text):
#     #your code here
#     if len(text) == 0:
#         return ''
    
#     if text.find('_') != -1: # found
#         text = text.split('_')
#         re_text = text[0] 
#         length = len(text)
#         i = 1
#         print(length)
#         print(re_text)
#         while i < length: 
#             re_text += text[i].capitalize()
#             i  += 1
#         print(re_text)
#         if re_text.find('-') == -1: # not found    
#             return re_text
#         else:
#             re_text = re_text.split('-')
#             re_text_1 = re_text[0] 
#             length = len(re_text)
#             print(re_text)
#             i = 1
#             while i < length:
#                 cap_list = []
#                 cap_list = re.findall('[a-zA-Z][^A-Z]*', re_text[i])
#                 j = 0
#                 c_length = len(cap_list)
#                 print("cap_list is ")
#                 print(cap_list)
#                 if c_length !=0:
#                     while j  < c_length:
#                         re_text_1 += cap_list[j].capitalize()
#                         j  +=1
#                 else:
#                     re_text_1  += re_text[i].capitalize()
#                 i  += 1
#             print(re_text_1)
#             return re_text_1
            

#     if  text.find('-') != -1: # found
#         text = text.split('-')
#         re_text = text[0] 
#         length = len(text)
#         i = 1
#         while i < length:  
#             re_text += text[i].capitalize()
#             i  += 1
#         if re_text.find('_') == -1: # not found    
#             return re_text
#         else:
#             re_text_1 = re_text.split('_')
#             re_text_1 = re_text[0] 
#             length = len(re_text)
#             i = 1
#             while i < length:
#                 re_text_1 += re_text[i].capitalize()
#                 i  += 1
#             return re_text_1

# Best Practices1Clever0
# 0ForkCompare with your solutionLink
# bob0921
# def to_camel_case(text):
#     list = text.replace("-","_").split("_")
#     ans = [list[0]]    
#     for i in list[1:]:
#         ans.append(i.title())
#     return ''.join(ans)
# Best Practices1Clever0
# 0ForkCompare with your solutionLink
# Kebap
# def to_camel_case(text):
#     result = []
#     up = False
#     for char in text:
#       if char in "-_":
#         up = True
#       else:
#         if up:
#           up = False
#           result += char.upper()
#         else:
#           result += char
#     return "".join(result)
# Best Practices1Clever0
# 0ForkCompare with your solutionLink
# tscribs
# def to_camel_case(text):
#     output = ''
#     lst = list(text)
#     for index, i in enumerate(lst):
#         if i == '-' or i == '_':
#             del lst[index]
#             lst[index] = lst[index].upper()
#             output = ''.join(lst)
#     return output
# print(to_camel_case("Testing-function-to_camel_case"))
# print(to_camel_case("the_stealth-warrior"))
# Best Practices1Clever0
# 0ForkCompare with your solutionLink
# lovestar
# def to_camel_case(text):
#     llist = ('_'.join(text.split('-'))).split('_');
#     for i in range(1, len(llist)):
#         llist[i] = llist[i].capitalize()
#     return ''.join(llist)#your code here
# Best Practices1Clever0
# 0ForkCompare with your solutionLink
# SmnLpscmb
# def to_camel_case(text):
#     if len(text) == 0 :
#         return text
#     elif text.find("_") or text.find("-") :
#         a = text.split("_")
#         b = [elt.split("-") for elt in a]
#         if b[-1] == b[0] :
#             c = b[0]
#         else :
#             c = []
#             for i in range(len(b)):
#                 c+= b[i]
#         if c[0].istitle():
#             return "".join(elt.title() for elt in c)
#         else :
#             d = "".join(elt.title() for elt in c[1:])
#             return c[0] + d
# Best Practices1Clever0
# 0ForkCompare with your solutionLink
# proctro
# def to_camel_case(text):
#     if text == '':
#         return ''
#     elif '-' or '_' in text:
#         text = text.replace('-', ' ')
#         text = text.replace('_', ' ')
#     camel = ''.join(x for x in text.title() if not x.isspace())
#     if text[0].islower():
#         return camel[0].lower() + camel[1:]
#     else:
#         return camel
# Best Practices1Clever0
# 0ForkCompare with your solutionLink
# Shabba77
# def to_camel_case(text):
#     separators = ["-","_"]
#     for separator in separators:
#         while(True):
#             dash = text.find(separator)
#             if dash != -1 :
#                 text = text[0:dash] + text[dash+1].upper() + text[dash+2:]
#             else:
#                 break
#     return text
# Best Practices1Clever0
# 0ForkCompare with your solutionLink
# mariape
# import re

# def to_camel_case(text):
#     if len(text) == 0:
#         return text
#     res = ''.join([word.capitalize() for word in re.split('_|-', text)])
#     return text[0] + res[1:]
# Best Practices1Clever0
# 0ForkCompare with your solutionLink
# AMC11
# import re


# def to_camel_case(str_in: str) -> str:
#     words_list = re.split('[-_]', str_in)
#     res_str = words_list[0] + ''.join([curr_word[0].upper() + curr_word[1:] for curr_word in words_list[1:]])
#     return res_str
# Best Practices1Clever0
# 0ForkCompare with your solutionLink
# robert wang
# import re

# def to_camel_case(s):
#     p = re.compile('[-_](.)')
#     return p.sub(lambda s:s.group(1).upper(), s)    
    
# Best Practices1Clever0
# 0ForkCompare with your solutionLink
# robert wang
# def to_camel_case(s):
#     tab = str.maketrans("-_", '-_', "-_")
#     return s[0] + s.title().translate(tab)[1:] if s else s
# Best Practices1Clever0
# 0ForkCompare with your solutionLink
# Kebap
# def to_camel_case(text):
#     result = []
#     up = False
#     for char in text:
#       if char in "-_":
#         up = True
#       else:
#         if up:
#           up = False
#           result += char.upper()
#         else:
#           result += char
#     return "".join(result)
# Best Practices1Clever0
# 0ForkCompare with your solutionLink
# tscribs
# def to_camel_case(text):
#     output = ''
#     lst = list(text)
#     for index, i in enumerate(lst):
#         if i == '-' or i == '_':
#             del lst[index]
#             lst[index] = lst[index].upper()
#             output = ''.join(lst)
#     return output
# print(to_camel_case("Testing-function-to_camel_case"))
# print(to_camel_case("the_stealth-warrior"))
# Best Practices1Clever0
# 0ForkCompare with your solutionLink
# lovestar
# def to_camel_case(text):
#     llist = ('_'.join(text.split('-'))).split('_');
#     for i in range(1, len(llist)):
#         llist[i] = llist[i].capitalize()
#     return ''.join(llist)#your code here
# Best Practices1Clever0
# 0ForkCompare with your solutionLink
# SmnLpscmb
# def to_camel_case(text):
#     if len(text) == 0 :
#         return text
#     elif text.find("_") or text.find("-") :
#         a = text.split("_")
#         b = [elt.split("-") for elt in a]
#         if b[-1] == b[0] :
#             c = b[0]
#         else :
#             c = []
#             for i in range(len(b)):
#                 c+= b[i]
#         if c[0].istitle():
#             return "".join(elt.title() for elt in c)
#         else :
#             d = "".join(elt.title() for elt in c[1:])
#             return c[0] + d
# Best Practices1Clever0
# 0ForkCompare with your solutionLink
# proctro
# def to_camel_case(text):
#     if text == '':
#         return ''
#     elif '-' or '_' in text:
#         text = text.replace('-', ' ')
#         text = text.replace('_', ' ')
#     camel = ''.join(x for x in text.title() if not x.isspace())
#     if text[0].islower():
#         return camel[0].lower() + camel[1:]
#     else:
#         return camel
# Best Practices1Clever0
# 0ForkCompare with your solutionLink
# Shabba77
# def to_camel_case(text):
#     separators = ["-","_"]
#     for separator in separators:
#         while(True):
#             dash = text.find(separator)
#             if dash != -1 :
#                 text = text[0:dash] + text[dash+1].upper() + text[dash+2:]
#             else:
#                 break
#     return text
# Best Practices1Clever0
# 0ForkCompare with your solutionLink
# mariape
# import re

# def to_camel_case(text):
#     if len(text) == 0:
#         return text
#     res = ''.join([word.capitalize() for word in re.split('_|-', text)])
#     return text[0] + res[1:]
# Best Practices1Clever0
# 0ForkCompare with your solutionLink
# AMC11
# import re


# def to_camel_case(str_in: str) -> str:
#     words_list = re.split('[-_]', str_in)
#     res_str = words_list[0] + ''.join([curr_word[0].upper() + curr_word[1:] for curr_word in words_list[1:]])
#     return res_str
# Best Practices1Clever0
# 0ForkCompare with your solutionLink
# robert wang
# import re

# def to_camel_case(s):
#     p = re.compile('[-_](.)')
#     return p.sub(lambda s:s.group(1).upper(), s)    
    
# Best Practices1Clever0
# 0ForkCompare with your solutionLink
# robert wang
# def to_camel_case(s):
#     tab = str.maketrans("-_", '-_', "-_")
#     return s[0] + s.title().translate(tab)[1:] if s else s
# Best Practices1Clever0
# 0ForkCompare with your solutionLink
# Loading more solutions...
# © 2021 CodewarsAboutAPIBlogPrivacyTermsContact
# powered by

# Show the solutions of those that I am following