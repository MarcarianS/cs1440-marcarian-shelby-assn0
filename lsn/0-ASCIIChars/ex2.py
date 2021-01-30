def listOfASCIIInts(charList):
    list = []
    # TODO: convert a list of characters into a list of ints based on the
    #   characters ASCII values
    listLength = len(charList)
    for i in range(0, listLength):
        list.append(ord(charList[i]))
        i += 1
    return list


if __name__ == '__main__':
    provided = ["A", "B", "c", "1", "-", "_", "~", " ", "z", "Y", "x"]
    provided2 = "Will you pass this test too?"

    print(listOfASCIIInts(provided))
    print(listOfASCIIInts(provided2))
