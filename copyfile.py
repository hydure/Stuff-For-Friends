filename1 = input("Enter the name of the first text file: ")
filename2 = input("Enter the name of the second text file: ")

file1 = open(filename1, "r")
file2 = open(filename2, "w")

for line in file1:
    file2.write(line)

file1.close()
file2.close()