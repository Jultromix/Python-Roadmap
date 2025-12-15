# Loops

# while loop
i= 1

# while i <= 10:
#     i += 1
#     if i == 5:
#         break
#     print(i)

# while i <= 10:
#     i += 1
#     if i == 5:
#         continue
#     print(i)
# else:
#     print("the condition got false")
    

# For loop
word = "cafe"

for letter in word:
    print(letter)

colors = ["red", "blue", "brown"]
flavors = ["spicy", "sweet", "sour"]

for color in colors:
    if color == "blue":
        continue
    print(color)
else:
    print("for loop ended")
print("----------------------------")

for i in range(0,10,2):
    print(i)
print("----------------------------")

for color in colors:
    for flavor in flavors:
        print(color, flavor)