from typing import Text
##from typing_extensions import Required
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# se crea un objetos de tipo Club 
lecturaclub = open("./data/datos_clubs.txt","r", encoding="utf-8")
lecturajugadores = open("./data/datos_jugadores.txt","r",encoding="utf-8")

jugadordatos=list(lecturajugadores)
datosClub = list(lecturaclub)


clubdatos = []

for d in datosClub:
    d = d.replace('\n','')    
    clubdatos = d.split(';')
    
    p = Club(nombre=clubdatos[0], deporte=clubdatos[1], fundacion=int(clubdatos[2]))
    
    session.add(p)
    print(clubdatos)        
# Se crean objeto de tipo Jugador
jugadores = []

for d in jugadordatos:
    d = d.replace('\n','')    
    jugadores = d.split(';')
    p = Jugador( nombre = jugadores[3],\
            dorsal = int(jugadores[2]),\
            posicion = jugadores[1],\
            club = session.query(Club).filter_by(nombre=jugadores[0]).one())
    session.add(p)
    print(jugadores)     



# se confirma las transacciones
session.commit()
lecturaclub.close()
lecturajugadores.close()