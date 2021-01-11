def spin_words(sentence):
    return ' '.join([element[::-1] if len(element) >= 5 else element
                     for element in sentence.split()])
    # newlist = []
    # for element in sentence.split():
    #     if len(element) >= 5:
    #         newlist.append(element[::-1])
    #     else:
    #         newlist.append(element)

    # return ' '.join(newlist)


print(spin_words("carlos es un amor"))

# return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])