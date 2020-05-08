#!/user/bin/python3
def complex_delete(a_dictionary, value):
    tmp = []
    for e in a_dictionary.keys():
        if a_dictionary[e] == value:
            tmp.append(e)
    for i in tmp:
        del a_dictionary[i]
    return a_dictionary
