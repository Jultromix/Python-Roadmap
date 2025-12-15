#           0       1       2       3
colors = ["red", "brown", "blue", "green"]

print(colors)
print(type(colors))

print(colors[2])

colors[2] = "grey"

print(colors[2])
print(colors)

print(colors[1:3])

if "grey" in colors:
    print("grey is in colors")
print("----------------------")

vehicles = ["air plane", "boat", "car"]
vehicles.append("bike")
print(vehicles)
print("----------------------")

vehicles.insert(1, "train")
print(vehicles)
print("----------------------")

vehicles.remove("boat")
print(vehicles)
print("----------------------")

vehicles.pop(1)
print(vehicles)
print("----------------------")

vehicles.sort()
print(vehicles)
print("----------------------")

vehicles.reverse()
print(vehicles)


collection_1 = [1,2,3]
collection_2 = [4,5,6]

collection_3 = collection_1 + collection_2
print(collection_3)

collection_1.extend(collection_2)
print(collection_1)