auto = {
    "marca" : "Renault",
    "modelo" : "Clio",
    "año" : 2025 
}

print(auto)
print(auto["marca"])
print(auto.get("marca"))

print(auto.keys())
print(auto.values())

if "marca" in auto:
    print("marca is in dict")


#Replace values:
auto["año"] = 2024
print(auto["año"])

#Add keys
auto["color"] = "red"
print(auto)

#Another way of modifying and adding items:
auto.update({"año" : 2023})
auto.update({"puertas":4})

print(auto)
 
auto.pop("puertas")
print(auto)

auto.popitem()
print(auto)

# auto.clear()
# print(auto)

for k in auto:      #keys
    print(k)

for v in auto.values():     #values
    print(v)

for k,v in auto.items():    #key, value
    print(k,v)  

#Nested Dictionaries

familia = {
    "hijo1": {
        "nombre" : "Juan",
        "edad" : 3
    },
    "hijo2": {
        "nombre" : "Fidencio",
        "edad" : 14
    },
    "hijo3": {
        "nombre" : "Mara",
        "edad" : 10
    },
}

print(familia["hijo1"]["nombre"])