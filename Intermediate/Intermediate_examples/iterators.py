from itertools import groupby, permutations, product, chain, combinations, groupby

# from more_itertools import powerset

nums = [1, 2, 3]
letters = ["a", "b"]

coord = list(product(nums, letters))

print(coord)
print("==================")
# Fin ejercicio 1

data = [1, 2, 3]


def powerset(iterable):
    "Subsequences of the iterable from shortest to longest."
    # powerset([1,2,3]) → () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


res = list(powerset(data))

print(res)

print("==================")

dat = [("A", 10), ("A", 20), ("B", 5), ("B", 15), ("A", 30)]

res = [k for k, g in groupby(dat)]
print(res)
