"""2025-11-30
This is a training file to cover variable creation and some standards
about how to declare them"""

# First block of lines is meant to show single declaration of variabels
x = "text"
print(x)

variant = "formato predeterminado"
variant_snake = "snake format"
_variant_3 = "snake format variant"
VARIANT = "Upper case"
variantCamel = "Camel format"
VariantPascal = "Pascal format" 


# Second block of lines is meant to show single declaration of variables
x,y,z = '1','2',"3"
print(x,y,z)

a = b = c = 1
print(a,b,c)
print("logic state " + a)

# The third blocl of lines aims to show the different datatypes to be stored

    # Data type 1) Strings
text_type_1 = 'text'
text_type_2 = "text"
text_type_3 = """text"""

print(text_type_1)
print(text_type_2)
print(text_type_3)

    # Data type 2) Integers
integer_var = 1
print(integer_var)

    # Data type 3) Decimals
float_var = 1.1
print(float_var)

    # Data type 4) Complex
complex_var = 1 + 3j
print(complex_var)

    # Data type 5) Lists
list_var = [0,1,2,3,4,5]
print(list_var)

    # Data type 6) Tuples
tuple_var = (0,1,2,3,4,5)
print(tuple_var)

    # Data type 7) Dictionaries
dictionary_var = {
    "name" : "Julio",
    "Age" : 20,
    "Country" : "Mexico" 
}
print(dictionary_var)

# Data type 8) Sets
set_var = {1,2,3,3,3,4}     # What about using sets to filter outputs
print(set_var)

# Data type 9) Boolean

boolean_var = True
print(boolean_var)
