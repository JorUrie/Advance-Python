myFile = open('days.txt', 'r')
'''It reads the given no. of bytes (N) as a string. If no value is given, 
then it reads the file till the end.'''
# We can now manipulate our file
myFile.read()
# readline() reads one entire line from the file
'''readlines() method will return all the lines in a file in the format of a list 
where each element is a line in the file.'''
file_input = open('read.txt', 'r')
data = file_input.readline()
print(data)
'''file_input.readlines() returns a list of the lines in the file, where each item of
the list represents a single line.'''
list = file_input.readlines(20) # in bytes
print(list)
# Write function
file_input = open('read.txt', 'w')
file_input.write('Python is amazing')
# Append function
file_input = open('read.txt', 'a')
file_input.write(' Python is amazing')
'''It reads the given no. of bytes (N) as a string. 
If no value is given, then it reads the file till the end.'''
file_input = open('readC.txt', 'r')
data = file_input.readline()
print(data)
file_input.close()