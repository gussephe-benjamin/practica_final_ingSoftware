from conexionDB import cur

# Impresión de datos de cada DB

cur.execute('SELECT * FROM usuarios;')

data = cur.fetchall()

for entry in data:
    print(entry)
print(" ")

cur.execute('SELECT * FROM contactos;')

data = cur.fetchall()

for entry in data:
    print(entry)
print(" ")

cur.execute('SELECT * FROM mensajes;')

data = cur.fetchall()

for entry in data:
    print(entry)
print(" ")