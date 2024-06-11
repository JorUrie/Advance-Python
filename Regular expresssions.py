# Regular Expression is a sequence of character(s) mainly used to find and replace patterns in a string or file
import re
string = 'Hello my name is Lyon'
print(re.findall(r'Lyon', string))

# To find all the number characters in a string we can use an identifer '/d'
string = 'Hello I live on lane 8 wich is near street 42'
print(re.findall(r'\d', string))
# We can use a modifer '+' to get numbers of any length from the string
print(re.findall(r'\d+', string))

if re.search('awesome', 'Is not this an awesome view?'):
    print('You are awesome')

# This method helps to split strings by the occurrences of a given pattern
result = re.split(r's', 'Awesome')
print(result)