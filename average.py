# Prompt the user for the filename
fileName = input("Please enter the file name: ")
openFile = open(fileName, 'r')

count, total = 0, 0

for number in openFile:
    total += int(number)
    count += 1

intAverage = total // count
actualAverage = total / count

print("The integer average is: " + str(intAverage))
print("The actual average is:  " + str(actualAverage))