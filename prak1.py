def increment(x):
    return x + 3

numbers = [3, 7, 9, 11, 15]

result = map(increment, numbers)
print(list(result)) 