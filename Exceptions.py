a = 5
b  = 0
try:
    print('Result of Division: ', a/b)
except ZeroDivisionError as iE:
    print('Cannot be divided by zero')

# We need to see the error first
#print(language)
try:
    print(language)
except NameError as e:
    print('Some error occurred')

# No Exceptions
language = 'Python'
try:
    print(language)
except NameError as e:
    print('Some error occurred')

# Syntax: Finally block always executes after normal termination of try block of after try block terminates due to some exception
try:
    print(ourVariable)
except Exception:
    print('ourVariable is not defined')
finally:
    print('Output is printed successfully')

# Exceptions are raised when errors occur at runtime
# We can also choose when the raise exceptions in our code
def print_five_items(data):
    if len(data) != 5:
        raise ValueError('The argument must have five elements')
    for item in data:
        print(item)
# Executed
print_five_items([5, 2])