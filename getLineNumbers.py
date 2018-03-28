# Prompt the user for the filename
fileName = input("Please enter the file name: ")
openFile = open(fileName, 'r')
fileList = []

# Input in the lines of text into a list
for line in openFile:
    fileList.append(line)

# Program then enters loop, prints number of lines in a file
# Line #'s range from 1 to end, 0 quits program, if not 0 print lines
userInput = ''
while userInput != 0:
    print("The number of lines in the file is " + str(len(fileList)))
    userInput = int(input("Please enter a line number  you wish to see; press '0' to quit: "))
    
    # The input '0' quits the program
    if userInput == 0:
        continue
    
    # Line numbers range from '1' to last line of file
    userInput -= 1
    print(fileList[userInput])

print("Have a nice day!")