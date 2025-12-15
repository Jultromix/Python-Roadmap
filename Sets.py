fruits = {"apple", "pinapple", "strawberry","apple"}
print(type(fruits))

print(fruits, len(fruits))

for item in fruits:
    print(item)

print("apple" in fruits)
print("orange" in fruits)

fruits.add("orange")
print(fruits)

set_2 = {"cherry", "grape"}

fruits.update(set_2)
print(fruits)

fruits.remove("cherry")
print(fruits)

fruits.discard("grape")
print(fruits)

fruits.pop()
print(fruits)

fruits.clear()
print(fruits)

print("-------------------------")

a = {"a","b","c"}
b = {"c","d","e"}

union_set = a.union(b)
print(union_set)

intersect_set = a.intersection(b)
print(intersect_set)

difference_set = a.difference(b)
print(difference_set)