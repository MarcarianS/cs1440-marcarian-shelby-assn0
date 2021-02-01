def findWords(sentence):
    wordsToReturn = []
    # TODO: Return the words in `sentence` that are five characters or less
    # for word in sentence...
    newSentence = sentence.split()
    for word in newSentence:
        wordLength = len(word)
        if wordLength <= 5:
            wordsToReturn.append(word)
    return wordsToReturn


if __name__ == '__main__':
    provided = [
        "Craftsman Keep Reveal personal it harmful engine short friendly killer honest season and camera strange hiccup horseshoe sphere charismatic ceiling sweet formation substitute daughter perfect",
        "Keep reject",
        "",
        "Do or do not, there is no try.",
        "TechnicallyI'mOneWordOnly",
        "One two skip a few, 99 100!",
    ]

    resultList = []
    for string in provided:
        resultList += findWords(string)

    for result in resultList:
        print(result)
