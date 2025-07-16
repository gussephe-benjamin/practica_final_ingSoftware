from conexionDB import cur, connect

cur.execute(""" 
    DROP TABLE IF EXISTS mensajes CASCADE;
""")

cur.execute(""" 
    DROP TABLE IF EXISTS contactos CASCADE;
""")

cur.execute(""" 
    DROP TABLE IF EXISTS usuarios CASCADE;
""")

connect.commit()