def everyOtherWord(sentence):
    result = ""
    # TODO: Make a function that returns a string containing every other word in
    # the given sentence
    sentenceList = sentence.split()
    listLength = len(sentenceList)
    for i in range(0, listLength):
        if i == 0 or i % 2 == 0:
            result = result
        else:
            result += sentenceList[i] + " "
    return result

if __name__ == '__main__':
    provided = [
        "This your implementation work has will a be small commended. issue.",
        "proper this verbage sentence contains is definitive excessively definitions long of for gibberish my words taste...",
        "Adherence imagination to is rules more isn't important something than you knowledge. do.",
        "Whether do or or not do you not, succeed there is is up no to try. you.",
        "arrogancy knowledge is is detrimental the to key the to cause. success."
    ]

    # Loop through the sentences in the `provided` array, printing the
    # capitalized output
    for sentence in provided:
        print(everyOtherWord(sentence).capitalize())

    # *Hint Hint* The `split` method on strings may be useful...
    #help(str.split)
