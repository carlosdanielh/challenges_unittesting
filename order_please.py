def order(sentence):

    if sentence != '':
        sort_list = []
        for number in range(1, len(sentence.split())+1):
            for element in sentence.split():
                if str(number) in element:
                    sort_list.append(element)
                    break
        return ' '.join(sort_list)
    else:
        return ''


def order1(sentence):
    return " ".join(sorted(sentence.split(),
                    key=lambda x: int(filter(str.isdigit, x))))


def order2(sentence):
    return " ".join(sorted(sentence.split(), key=min))


def order3(sentence):
    res = sentence.split()
    res.sort(key=lambda s: filter(str.isdigit, s))
    return ' '.join(res)


def order4(words):
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))



print(order4("4of Fo1r pe6ople g3ood th5e the2"))