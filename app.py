from fastapi import FastAPI
from typing import Optional
from baseDatos.conexionDB import connect,cur
from fastapi.responses import JSONResponse
import json
from datetime import datetime
from fastapi import status
from psycopg2 import DatabaseError

app = FastAPI()
        
@app.get('/')
def funciona():
    return{"hola"}

@app.get ('/mensajeria/contactos')
def get_contactos_user(mialias: Optional[str] = None):
    
    cur.execute(f"""
                
                SELECT u.alias, u.nombre FROM contactos AS c, usuarios AS u
                WHERE c.usuario = '{mialias}' AND  c.contacto = u.alias;
                
                """)
    
    rows = cur.fetchall()
    return JSONResponse(content=json.loads(json.dumps(rows, indent=4, ensure_ascii=False)))
    
@app.api_route('/mensajeria/enviar',methods=["GET","POST"])
def post_enviar_mensaje(usuario : Optional[str] = None, contacto : Optional[str] = None, mensaje : Optional[str] = None):
    
    if not all([usuario,contacto,mensaje]):
        return JSONResponse(content={"error": "Faltan campos obligatorios"}, status_code=400)
    
    try:
        cur.execute("""
            INSERT INTO mensajes (userRemitente, userDestinatario, mensaje, fechaEnvio)
            VALUES (%s, %s, %s, %s)
            RETURNING id_mensaje, userRemitente, userDestinatario, fechaEnvio, mensaje;
        """, (usuario, contacto, mensaje, datetime.now()))

        nuevo_mensaje = cur.fetchone()
        connect.commit()

        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "mensaje": "Mensaje enviado correctamente.",
                "data": {
                    "id_mensaje": nuevo_mensaje[0],
                    "userRemitente": nuevo_mensaje[1],
                    "userDestinatario": nuevo_mensaje[2],
                    "fechaEnvio": nuevo_mensaje[3].isoformat(),
                    "contenido": nuevo_mensaje[4]
                }
            }
        )

    except DatabaseError as e:
        connect.rollback()  # 🚨 Importante
        return JSONResponse(
            status_code=500,
            content={"error": "Error en la base de datos", "detalle": str(e)}
        )
    

@app.get('/mensajeria/recibidos')
def mensajes_recibidos(mialias : Optional[str] = None):
    
    cur.execute(f""" 
                SELECT m.userremitente, m.mensaje, m.fechaenvio FROM usuarios AS u, mensajes AS m
                WHERE u.alias = '{mialias}'AND u.alias =  m.userdestinatario
                """)
    
    rows = cur.fetchall()
    return rows
    
