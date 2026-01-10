name = "Gala"
year = 2020
text = f"Hola {name} tu edad es {2025 - year}"

text_2 = f"La suma dió como resultado {1 + 1}"

text_function = f"Hola {name.upper()}"

# print(text, text_2)
# print(text_function)

edad = 21
text_if = f"Hola {name}, eres {'mayor' if edad >= 18 else 'menor'} de edad"


bank_balance = 1230000000
text = f"Tu saldo en la cuenta bancaria es: {bank_balance:,}"
print(text)

stock_price = 1.603
text = f"El valor del stock es: {stock_price:.1f}"
print(text)

text = f"El valor del stock es: {stock_price:.2f}"
print(text)

user_id = 1
text = f"Su id es: {user_id:03d}"
print(text)

product = "laptop"
price = 1000

text = f"Producto: {product:<15} | Precio: {price:>10}"
print(f"{text}\n{text}")

from datetime import datetime

date = datetime(2025, 12, 17, 5, 34)
text = f"La fecha completa es {date: %A %d de %B de %Y a las %I:%M %p}"
print(text)
