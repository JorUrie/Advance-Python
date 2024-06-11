import random
print('Random Number 1 => ', random.random())
print('Random Number 2 => ', random.random())
print(random.randrange(3, 9))
print(random.randint(3, 9))
# shuffles a list
list = [10, 6, 4, 11, 1]
random.shuffle(list)
print('Printing shuffled list', list)
# Random with a different probability
numberList = [151, 251, 351, 451, 551]
print(random.choices(numberList, weights = (10, 20, 30, 40, 50), k = 5))
