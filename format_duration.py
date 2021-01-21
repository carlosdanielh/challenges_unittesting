'''Your task in order to complete this Kata is to write a function which 
formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns
"now". Otherwise, the duration is expressed as a combination of:

                years, days, hours, minutes and seconds.

It is much easier to understand with an example:
print(format_duration(62))    # returns "1 minute and 2 seconds"
print(format_duration(3662))  # returns "1 hour, 1 minute and 2 seconds"

For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.
'''


def format_duration(sgs):
    if sgs == 0:
        return 'now'
    dict_segs = {
        'years': 31536000,
        'days': 86400,
        'hours': 3600,
        'minutes': 60,
        'seconds': 1
    }

    show = []
    for element in list(dict_segs.values())[:-1]:
        if round(sgs//element):
            show.append(sgs//element)
            sgs = sgs % element
        else:
            show.append(sgs//element)

    show += [sgs]

    count = 0
    words = []
    for index, element in enumerate(show):

        if element != 0:
            count += 1

        if element > 1:
            words.append(list(dict_segs.keys())[index])            
        else:
            words.append(list(dict_segs.keys())[index][:-1])
    print(show)
    print(count)
    concatenate = ''

    more_than_1 = False
    if count > 1:
        more_than_1 = True

    for index, element in enumerate(show):
        number = str(element)

        if element != 0:
            # import pdb; pdb.set_trace()
            if count > 2:
                concatenate += number + ' ' + words[index] + ', '
            elif count == 2:
                concatenate += number + ' ' + words[index]
            elif count == 1 and more_than_1:
                concatenate += ' and ' + number + ' ' + words[index]
            elif count == 1:
                concatenate = number + ' ' + words[index]

            count -= 1

    return concatenate


print(format_duration(62))    # returns "1 minute and 2 seconds"
print(format_duration(0))  # returns "1 hour, 1 minute and 2 seconds"
print(format_duration(86400*2))