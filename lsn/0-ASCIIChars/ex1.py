def listOfChars(intList):
    list = []
    # TODO: Append to characters to `list`
    return list


if __name__ == '__main__':
    provided = [
        65,
        32,
        115,
        104,
        111,
        114,
        116,
        32,
        115,
        101,
        110,
        116,
        101,
        110,
        99,
        101,
        46
    ]

    result = listOfChars(provided)

    # The following block of code turns the list `result` into a string `resultStr`
    # Do not modify!
    resultStr = ""
    for char in result:
        resultStr += char
    print(resultStr)
