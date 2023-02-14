from pprint import pprint


def splitIntoGroupsOf(grounpSize, theList):
    result = []
    for i in range(0, len(theList), grounpSize):
        result.append(theList[i:i + grounpSize])
    return result


res = splitIntoGroupsOf(8, list(range(70)))
pprint(res)
