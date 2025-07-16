from conexionDB import cur, connect

# creación de las tablas

cur.execute(""" 
    
            CREATE TABLE usuarios(
                alias VARCHAR(50) PRIMARY KEY NOT NULL,
                nombre VARCHAR(50) NOT NULL
            );

    """)

cur.execute(
    """
            CREATE TABLE mensajes(
                id_mensaje SERIAL PRIMARY KEY,
                userRemitente VARCHAR(50) NOT NULL,
                userDestinatario VARCHAR(50) NOT NULL,
                mensaje VARCHAR(1000),
                FOREIGN KEY (userRemitente) REFERENCES usuarios(alias) ON DELETE CASCADE,
                FOREIGN KEY (userDestinatario) REFERENCES usuarios(alias) ON DELETE CASCADE,
                fechaEnvio TIMESTAMP 
            );
    
    """)

cur.execute("""
            
            CREATE TABLE contactos(
                id_contacto SERIAL PRIMARY KEY,
                usuario VARCHAR(50) NOT NULL,
                contacto VARCHAR(50) NOT NULL,
                FOREIGN KEY (usuario) REFERENCES usuarios(alias) ON DELETE CASCADE,
                FOREIGN KEY (contacto) REFERENCES usuarios(alias)ON DELETE CASCADE,
                UNIQUE(usuario,contacto)
            );   
               
    """)

# confirmar acciones y registrarlo en la base de datos 
connect.commit() 

