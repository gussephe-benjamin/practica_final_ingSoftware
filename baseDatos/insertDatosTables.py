from conexionDB import cur, connect
from datetime import datetime

# agregar datos predeterminados 

usuarios = [
    ('fede', 'Rico'),
    ('luna23', 'Lucía Torres'),
    ('darko', 'Carlos Moreno'),
    ('sunnyJ', 'Jimena Salazar'),
    ('zeta_', 'Mateo Zúñiga'),
    ('nova12', 'Diana Campos'),
    ('leonardo_', 'Leonardo Paredes'),
    ('skywalker', 'Ana Fernández'),
    ('echo_7', 'Esteban Ruiz'),
    ('michi99', 'Gabriela Medina')
]

lista_contactos = [
    ("fede", "luna23"),
    ("fede", "darko"),
    ("luna23", "fede"),
    ("darko", "nova12"),
    ("nova12", "leonardo_"),
    ("leonardo_", "skywalker"),
    ("skywalker", "echo_7"),
    ("echo_7", "michi99"),
    ("michi99", "sunnyJ"),
    ("sunnyJ", "zeta_"),
    ("zeta_", "fede"),
    ("fede", "skywalker"),
    ("luna23", "leonardo_"),
    ("darko", "sunnyJ")
]

mensajes = [
    "¡Hola! ¿Cómo has estado?",
    "¿Te gustaría juntarnos a estudiar esta semana?",
    "Solo pasaba a saludar 😄",
    "¿Ya viste la última práctica de clase?",
    "Gracias por la ayuda del otro día!",
    "¿Tienes tiempo para revisar un código?",
    "¡Mucho éxito en el examen final!",
    "¿Te animas a hacer el proyecto juntos?",
    "No entiendo la parte de normalización 😅, ¿me ayudas?",
    "Avísame si necesitas los apuntes de la clase."
    "¿Tienes tiempo para revisar un código?",
    "¡Mucho éxito en el examen final!",
    "¿Te animas a hacer el proyecto juntos?",
    "No entiendo la parte de normalización 😅, ¿me ayudas?",
    "Avísame si necesitas los apuntes de la clase",
]

# Insertar datos en la DB usuarios

for a, b in usuarios:
    cur.execute("INSERT INTO usuarios (alias, nombre) VALUES (%s, %s);", (a,b))

# Insertar datos en la DB contactos
for a, b in lista_contactos:
    cur.execute("INSERT INTO contactos (usuario, contacto) VALUES (%s, %s);", (a,b))

# Insertar datos en la tabla de mensajes

i = 0
for usuario, contacto in lista_contactos:  # lista_contactos es una lista de tuplas (remitente, destinatario)
    cur.execute("""
        INSERT INTO mensajes (userRemitente, userDestinatario, mensaje, fechaEnvio)
        VALUES (%s, %s, %s, %s);
    """, (usuario, contacto, mensajes[i], datetime.now()))
    i = i + 1

connect.commit() 

