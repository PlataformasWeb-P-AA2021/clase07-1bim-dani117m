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
lecturaclub = open("./data/datos_clubs.txt","r")

datosClub = list(lecturaclub)

clubdatos = []

for d in datosClub:
    d = d.replace('\n','')    
    clubdatos = d.split(';')
    
    p = Club(nombre=clubdatos[0], deporte=clubdatos[1], anio=int(clubdatos[2]))
    
    session.add(p)
    print(clubdatos)        
# Se crean objeto de tipo Jugador
lecturajugadores = open("./data/datos_jugadores.txt","r")

datosjugador = list(lecturajugadores)

jugadordatos = []

for d in datosjugador:
    d = d.replace('\n','')    
    datosjugador = d.split(';')

    p = Jugador(equipo= sesion.query(equipo).filter_by(nombre=datosjugador[0]).one(),\
            posicion=datosjugador[1], numero=datosjugador[2],\
            nombre=datosjugador[3])
    session.add(p)
    
    print(datosjugador)     



# se confirma las transacciones
session.commit()
lecturaclub.close()
lecturajugadores.close()