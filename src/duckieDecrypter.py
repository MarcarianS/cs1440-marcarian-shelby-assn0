import sys
# TODO:
# import the os module to get access to os.access and os.R_OK
import os

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
    charNumberLower = charCode.replace("_", "")
    if charNumberLower == "":
        return None
    else:
        charNumberLower = int(charNumberLower)
        if 0 <= charNumberLower <= 25:
            return chr(charNumberLower + 97)
        else:
            return None


def convertToUpper(charCode):
    '''
Convert the given character code to a single plain-text uppercase character.
Returns a single character.
    '''
    charNumberUpper = charCode.replace("^", "")
    if charNumberUpper == "":
        return None
    else:
        charNumberUpper = int(charNumberUpper)
        if 0 <= charNumberUpper <= 25:
            return chr(charNumberUpper + 65)
        else:
            return None


def convertToSpecialChar(charCode):
    '''
Convert the given character code to a single plain-text special character.
Returns a single character.
    '''
    charCode = charCode.replace("+", "")
    if charCode == "":
        return None
    else:
        if charCode.startswith("A"):
            charNumberOnlyA = charCode.replace("A", "")
            if charNumberOnlyA == "":
                return None
            else:
                charNumberOnlyA = int(charNumberOnlyA)
                if 0 <= charNumberOnlyA <= 32:
                    return chr(charNumberOnlyA + 32)
                else:
                    return None
        elif charCode.startswith("B"):
            charNumberOnlyB = charCode.replace("B", "")
            if charNumberOnlyB == "":
                return None
            else:
                charNumberOnlyB = int(charNumberOnlyB)
                if 0 <= charNumberOnlyB <= 5:
                    return chr(charNumberOnlyB + 91)
                else:
                    return None
        elif charCode.startswith("C"):
            charNumberOnlyC = charCode.replace("C", "")
            if charNumberOnlyC == "":
                return None
            else:
                charNumberOnlyC = int(charNumberOnlyC)
                if 0 <= charNumberOnlyC <= 3:
                    return chr(charNumberOnlyC + 123)
                else:
                    return None
        else:
            return None


def getFile():
    '''
Prompt the user for the text file. Verify the file's existence.
Open the file and return the opened file object if the input is valid.
    '''
    textFile = input("Please select a text file to parse: ")
    if os.access(textFile, os.R_OK):
        fileObj = (open(textFile))
        return fileObj
    else:
        sendError("Uh oh! I can't find your file ):")


# def checkFlags(flag):
#     '''
# Check the flag given, ensuring it is valid, and returning some information
# dictating which character type the flag denotes.
#     '''
#
#     # if flag == '^': ...
#     pass


def decryptCharacter(character):
    '''
Decrypts a single DuckieCrypt character. Returns a single character
    '''
    if character.startswith("^"):
        return convertToUpper(character)
    elif character.startswith("_"):
        return convertToLower(character)
    elif character.startswith("+"):
        return convertToSpecialChar(character)
    else:
        return None

def decryptLine(line):
    '''
Decrypt a single line of DuckieCrypt. Returns a built string
    '''

    output = ""
    duckieCodes = line.split(" ")
    for duckieCode in duckieCodes:
        translatedCharacter = decryptCharacter(duckieCode)
        if translatedCharacter == None:
            output += ""
        else:
            output += translatedCharacter
    return output

# DEV NOTES:
# I'm not sure what to do next... Maybe I should consult doc/Plan.md?
if __name__ == '__main__':
    file = getFile()
    for line in file.readlines():
        print(decryptLine(line))
    file.close()
