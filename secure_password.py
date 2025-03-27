import random
import string

def generate_password(length):
    if length<8:
        raise ValueError("La longitud mínima debe ser 4 caracteres.")
   
    letters= string.ascii_letters
    digits=string.digits
    symbols=string.punctuation
    password= [random.choice(letters), random.choice(digits), random.choice(symbols)]

    all_chars = letters + digits + symbols
    password += random.choices(all_chars, k=length - 3)

    # Mezclar la contraseña para que no siga un patrón
    random.shuffle(password)

    return ''.join(password)

# Pedir longitud al usuario
try:
    length = int(input("Enter the length of the password: "))
    print("Generated password:", generate_password(length))
except ValueError as e:
    print("Error:", e)
