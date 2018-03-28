# Prompt the user for the filename
fileName = input("Please enter the file name: ")
openFile = open(fileName, 'r')
fileDict = {}

# Add the unique words in a file to the list
# and count their respective frequencies
for line in openFile:
    line = line.strip().split()
    for word in line:
        word = word.replace(',', '').replace('.', '').lower()
        if word not in fileDict:
            fileDict[word] = 1
        else:
            fileDict[word] += 1

# Prints the unique words and their frequencies in alphabetical order
for word, frequency in sorted(fileDict.items(), key=lambda x: x[0]):
    print(word + ": " + str(frequency))