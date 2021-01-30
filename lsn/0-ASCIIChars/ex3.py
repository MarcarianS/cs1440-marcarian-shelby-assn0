def scoreWord(word):
    sum = 0
    # TODO: Score the word
    word = word.upper()
    wordList = list(word)
    wordLength = len(wordList)
    for i in range(0, wordLength):
        if 65 <= ord(wordList[i]) <= 90:
            sum += (ord(wordList[i]) - 65)
        else:
            sum += 0
        i += 1
    return sum

if __name__ == '__main__':
    provided = [
        "One",
        "oNE",
        "supercalifragilisticexpialidocious",
        "t",
        "aAaA",
        "Zap!",
        "Tr!ck3d y4!",
        "G0t it!"
    ]

    # For each word in the provided list, give the word to the function score word and print some fancy formatted output
    for word in provided:
        print(f"The score of {word} is: {scoreWord(word)}")
