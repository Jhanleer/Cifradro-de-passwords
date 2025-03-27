import bcrypt
import json
import os

FILE_NAME= "passwords.json"

def load_data():
    """Carga las contraseñas almacenadas en el JSON"""
    if not os.path.exists(FILE_NAME): #Si el archivo no existe, devuelve un diccionario vacío 
        return {}
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_data(data):
    """Guarda las contrase;as en el JSON"""
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def hash_password(password):
    """Cifra la contraseña con bcrypt"""
    salt = bcrypt.gensalt() #Genera una sal para cifrar la contraseña
    #El gensalt() método genera una sal aleatoria para cifrar la contraseña.
    hashed = bcrypt.hashpw(password.encode(), salt) #Cifra la contraseña
    #El hashpw() método cifra una contraseña en texto plano y devuelve la contraseña cifrada.
    return hashed.decode() #Devuelve la contraseña cifrada como cadena

def verify_password(plain_password, hashed_password):
    """Verifica si una contraseña ingresada coincide con la almacenada"""
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode()) 
#el checkpw() método compara una contraseña en texto plano con una contraseña cifrada y devuelve 
# True si coinciden, de lo contrario, devuelve False.

def add_password(service, password):
    """Añade una nueva contraseña cifrada"""
    data = load_data()
    hashed = hash_password(password)
    data[service] = hashed
    save_data(data)
    print(f"Contraseña para {service} guardada con éxito.")

def get_password(service, plain_password):
    """Verifica si la contraseña ingresada es correcta"""
    data = load_data()
    if service in data and verify_password(plain_password, data[service]):
        print(f"La contraseña ingresada es correcta para {service}.")
    else:
        print("Contraseña incorrecta o servicio no encontrado.")
#El método encode() devuelve la cadena codificada en bytes. Si no se especifica un parámetro,
# la cadena codificada por defecto será utf-8.

# Ejemplo de uso
add_password("gmail", "wenosdiasquetalesta123.@")
get_password("gmail", "wenosdiasquetalesta123.@")  # Debería indicar que la contraseña es correcta
get_password("gmail", "otraClave")  # Debería decir que es incorrecta

add_password("hotmail", "Quepedowenoentiendonada.@#")
get_password("hotmail", "Quepedowenoentiendonada.@#")  # Debería indicar que la contraseña es correcta
get_password("hotmail", "otraClave") 

    