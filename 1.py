#!/bin/python3.7
# Merge a dictionary and a list into 1 and pretty print it.

Dict = {'rope': 2, 'torch': 1, 'gold coin': 1, 'dagger': 1, 'arrow': 1}
List = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def displayPrettyDict(dict):
    print("Merged Dictionary:")
    totalItems = 0
    for a, b in dict.items():
        print (str(a) + " " + str(b))
        totalItems += b
    print("Total number of items: " + str(totalItems))


def addListToDict(dict, list):
    for x in list:
        if x in dict.keys():
            dict[x] += 1
        else:
            dict[x] = 1
    return dict


Dict = addListToDict(Dict, List)
displayPrettyDict(Dict)
