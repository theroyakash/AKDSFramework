import random

def generatorIntegers(min_, max_, size):
    return [random.randint(min_, max_) for _ in range(size)]