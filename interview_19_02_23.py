# number = int(input())
# if number == 2:
#    print("verified")
import random

new_list = list("qwerty")
print(len(new_list))

from random import randint

randomnum = random.randint(10, 100)
print(randomnum)

tmp = {"str2": "2"}
print(tmp)


class Temporary():
    def __init__(self):
        pass

    def __str__(self):
        pass


num_list = [i for i in range(0, 11, 4)]
print(num_list)


def one():
    print("!" * 100)
    copy_list = num_list[:]
    print(copy_list)

    copy_list.append(9)
    print(copy_list)

    copy_list.clear()
    print(copy_list)

# one()

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
