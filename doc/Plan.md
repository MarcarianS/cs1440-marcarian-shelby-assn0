*Replace the bold text with your own content*

*Adapted from https://htdp.org/2020-5-6/Book/part_preface.html*

# 0.  From Problem Analysis to Data Definitions

The program will ask a user for a relative file path as input and open the file.
The program will take the contents of the file and convert them from DuckieCrypt characters into a readable message.
invalid characters will be ignored.

getFile will take a file path and return file object.
decryptLine takes a line from the file object and returns a built string.
decryptCharacter takes a Duckie character from decryptLine and returns a character.
checkFlags returns a call for a method based on the flag given.
convertToCharacter returns single character (printable but non-alphabetical.)
convertToUpper returns and uppercase, alphabetical character.
convertToLower returns a lowercase, alphabetical character.
sendError returns a string

# 1.  System Analysis

Main Menu:
	User is given one option: Select a text file to parse.
From here, the program runs through its course to parse the given text file.
If the file does not exist, the program will exit.

getFile()
**Input:
-input for this funtion will come as a file path directly from the user.
	Examples:
		./data/text2.txt
		text1
-Function will check if the path exists. If invalid path is passed to the function, sendError() is called.
**Internal Data:
-Relative path given will be checked against the os.access command.
-If valid, the file will be converted into a file object
**Output:
-When given valid input, return file object.
-When given invalid input, call sendError and exit program.
**Function Stub
def getFile()
	ask user for file path
	determine if the file exists
	if file exists, open and return the file.
	if file not found, call sendError()

decryptLine()
**Input:
-Takes a string from the file object as it is read through.
	Examples:
		"" (blank line)
		"(valid duckie characters go here)"
		"(invalid duckie characters go here)"
**Internal Data: -Breaks up the string by whitespace 
-gives the Duckie Character to the funtion 
decryptCharacter() to translate. -adds the translated 
character to string "output" 
**Output:
-Returns the concatenated string "output"
**Function Stub:
def decryptLine(line):
	define output as a blank string
	break line into list of duckie characters
	for character in list call decryptCharacter(character)
	add translated character to output
	return output

decryptCharacter()
**input:
-takes a string from decryptLine()
	Examples:
		"_4"
		"+A0"
		"Hi!"
**Internal Data:
-splits the string into its separate character
-calls checkFlags() on the first character 
-If checkflags returns None, return None
-if checkFlags returns ^,_, or +, send the remaining characters to the appropriate converter (special, upper, or lower)
**Output:
Returns single character if given valid duckie character
Returns nothing if given invalid duckie character
**Function Stub:
def decryptCharacter(character)
	split character into individual characters
	call checkFlags on 0th entry to determine what kind of character it is
	if it's valid input, 
		remove 0th entry
		join list back to string
		call appropriate converter
		return single translated character
	if it's invalid input, return nothing


checkFlags()
**Input:
-single character
	Examples:
		"^"
		"h"
		""
**Internal Data: Use if statements to check if the 
character is a valid flag (^,_, or +) if not, return 
False. if it is valid, return True 
**Output: 
-Returns True or False 
**Function Stub:
def checkFlags(flag)
	if flag == ^, _ or + (use startswith.str)
		return True
	else return False

convertTo(Lower,Upper,Special)()
**Input:
-Takes a string (duckie character without the flag)
	Examples:
		"A"
		"30"
		"44"
		"A1"
**Internal Data:
-Depending on whether the code sends the characters to upper, lower, or special, use an ASCII table to translate it.
-For upper:
	take the number, add 65, take the char, return the character.
-For lower: 
	Take the number, add 97, take the char, return the character. 
-For Special:
	Based on the leading letter (a, b, or c) add 32, 91, or 123 and take the char to return.
**Output:
returns a single character.
**Function Stub:
def convertToUpper(charCode)
	if charCode is between 0 and 26
		return chr(charCode + 65)
	else
		sendError

def convertToLower(charCode)
	if charCode is between 0 and 26
		return chr(charCode + 97)
	else
		sendError

def convertToSpecialChar(charCode)
	if startswith.A
		return chr(charCode + 32)
	elif startswith.B
		return chr(charCode + 91)
	elif startswith.C
		return chr(charCode + 123)
	else	
		sendError

# 2.  Functional Examples

The "main menu" will be very simple:
	"Please select a file to parse: "
-If the path given is not valid, an error message will be printed and the program will be exited with code 1.
	You gave an invalid path ):
-Valid paths are determined using os.access
-If valid input is given, the program will begin to parse through the file given.
-Once the path is opened, the file will be read line by line, each line separated into its characters separateed by whitespace.
-The program will look first for a character flag on each group of characters separated by whitespace. If no valid flag is found, the program will ignore that group of characters.
-If the flag is found, it is removed from the string, and used to determine if the characters should be translated into an uppercase, loser case, or special character.
-The group of characters is sent to be translated according to their flag. If the number associated with the characters is out of the duckiedecrypter range, the character will be ignored as if it had an invalid flag.
-The groups of characters will each evaluate to a single character, returned to a string, and when the entire file has been parsed, printed to the user.

getFile()
I will know the file is valid if a file gets returned.
I can check these by running /data/msq0.txt which I know to be valid.
I will know It's not valid if sendError gets called.
I can check this by running a blank path or something like "hello", which I know not to be valid paths. If the program crashes instead of exit(1), I know I need to revisit this.
psuedo code:
textfile = input("gimme a file path: "
if os.access(textfile, os.R_OK)
	fileObj = open(textfile)
	return fileObj
else
	sendError()

decryptLine(line)
Since this is a conga line of functions, it will get difficult to see where the problem comes from.
Since there is no direct input anywhere else in the program, I cannot test different values here.
psuedo code:
output = ""
duckies = line.split()
for duckie in duckies
	character = decryptcharacter(duckie)
	if character == None
		output += None
	else output += character
	return output


dectryptCharacter(char)
Not too much to test here, if there's input issues it'll have to catch somewhere before or after me!
psuedo code:
if char.startswith(^, 0, 0)
	remove(char[0])
	return converToUpper(char)
elif char.starts(_, 0, 0)
	remove(char[0])
	return converToLower(char)
elif char.starts(+, 0,0)
	remove(char[0])
	return convertToSpecialCharacter(char)
else return None

checkFlags(flag)
Sorry, I didn't think this was useful when writing out the psuedo code the first time. 
To check flags, see decryptCharacter()

convertToSpecialChar(charCode)
Not much to test, but if the charCode is not a duckie character return nothing

pseudocode:
if char starts(A, 0, 0)
	charNumberOnly = char.replace ("A", "")
	char = int(char)
	if 0 <= char <= 32
		return chr(char + 32)
	else return None
if char starts(B, 0, 0)
        charNumberOnly = char.replace ("B", "")
        char = int(char)
        if 0 <= char <= 5
                return chr(char + 91)
        else return None
if char starts(C, 0, 0)
        charNumberOnly = char.replace ("C", "")
        char = int(char)
        if 0 <= char <= 3
                return chr(char + 123)
        else return None

convertToUpper(charCode)
codeNumber = charCode.replace ("^", "")
codeNumber = int(codeNumber)
if 0<= codeNumber <= 25
	return chr(codeNumber + 65)
else
	return None

convertToLower(charCode)
codeNumber = charCode.replace ("_", "")
codeNumber = int(codeNumber)
if 0<= codeNumber <= 25
        return chr(codeNumber + 97)
else
        return None

# 3.  Function Template

Very similar to #2 contents

# 4.  Implementation

see DuckieCrypter.py 

# 5.  Testing

Run "python duckieDecrypter.py with CWD ./src"
First:
	Enter a path you know doesn't exist
	I entered "../data/msg"
	It successfully told me that it couldn't find my file
Second:
	Enter a path you know exists
	I entered "../data/msg0.txt"
	Discovered that I was trying to concatenate None to a string
	I ran into a few other errors, but they were all simple syntax errors.
	After fixing the errors, I got the desired output:
	
	"Welcome to DuckieCorp! We sure are glad to have you working with us. In your
	tenure here, we hope you will learn many new techniques to enhance your computer

	science and problem solving skills. We're excited to get started!
	- DuckieCorp Management"
Third:
	Run your professors convenient test cases in /test
	Found an error with invalid characters that had no number after the letter. Made sure if the duckie code was a blank string that None was returned.
	This made the code look blocky, but it seems that adding a function to accomplish this would still require as many for loops. Since the program is still only 160 lines, I let it be for my own sanity's sake.
