import sys
# TODO:
# import the os module to get access to os.access and os.R_OK

def sendError(string=""):
    '''
Exits the program after displaying `string` as an error message. If no string
input is provided, the default message is "Error! An error was encountered, so
the program is quitting."
    '''
    # Dear Future Dev,
    # The code below is fine. Your work is not needed on `sendError`.
    # You are more than welcome to edit the string literal, especially to make
    # an angrier (but still polite) quack.
    if string == "":
        string = "Error! An error was encountered, so the program is quitting."
    print(f"""\
!!!QUACK!!!
================================================================================
{string}
================================================================================
!!!QUACK!!!
""")
    sys.exit(1)


def convertToLower(charCode):
    '''
Convert the given character code to a single plain-text lowercase character.
Returns a single character.
    '''
    pass


def convertToUpper(charCode):
    '''
Convert the given character code to a single plain-text uppercase character.
Returns a single character.
    '''
    pass


def convertToSpecialChar(charCode):
    '''
Convert the given character code to a single plain-text special character.
Returns a single character.
    '''
    pass


def getFile():
    '''
Prompt the user for the text file. Verify the file's existence.
Open the file and return the opened file object if the input is valid.
    '''
    textFile = input("Please select a text file to parse: ")
    # return file


def checkFlags(flag):
    '''
Check the flag given, ensuring it is valid, and returning some information
dictating which character type the flag denotes.
    '''

    # if flag == '^': ...
    pass


def decryptCharacter(character):
    '''
Decrypts a single DuckieCrypt character. Returns a single character
    '''
    pass


def decryptLine(line):
    '''
Decrypt a single line of DuckieCrypt. Returns a built string
    '''

    output = ""
    # ...
    return output

# DEV NOTES:
# I'm not sure what to do next... Maybe I should consult doc/Plan.md?
if __name__ == '__main__':
    file = getFile()
    for line in file.readlines():
        print(decryptLine(line))
    file.close()
