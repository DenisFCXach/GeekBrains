import itertools

a = (i for i in itertools.count(int(input())) if i <= 1e6)
array = [1, 2, 3, 4]
b = (v for i, v in enumerate(itertools.cycle(array)) if i <= 1e5)

