def scoreWord(word):
    sum = 0
    # TODO: Score the word
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
