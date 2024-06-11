import threading
def print_hello(num):
    print('You are an employee', num)

t1 = threading.Thread(target = print_hello, args = (10,)) # args need to be iterable
t1.start()
t1.join()
print('End')

# Miltithreading with Two Threads
def print_one():
    for i in range(2):
        print(1)
def print_two():
    for i in range(2):
        print(2)
if __name__=='__main__':
    # create threads
    t1 = threading.Thread(target = print_one)
    t2 = threading.Thread(target = print_two)
# start threads
t1.start()
t2.start()
# wait unntil threads are completly executed
t1.join()
t2.join()
# both threads completly executed
print('Completed!')