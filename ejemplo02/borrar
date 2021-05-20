from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from generador2 import data_json

import json
import requests


# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///datos_json.db')


Session = sessionmaker(bind=engine)
session = Session()

# se crean objetos de tipo Pesona

# leer el archivo de datos

personasR = requests.get("https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json")

prueba = personasR.json()


   
for d in prueba:
    ##print(d)
    ##print(len(d.keys()))
    p = data_json(cldr= (d['CLDR display name']), capital= (d['Capital']), continent= (d['Continent']), \
            dial= (d['Dial']), geoname= (d['Geoname ID']), itu= (d['ITU']), languages= (d['Languages']), is_independent= (d['is_independent']) )
    session.add(p)

# confirmar transacciones

session.commit()



## Crear una entidad con los siguientes atributos:
##	* Nombre de pais
##	* Capital
##	* Continente
##	* Dial
##	* Geoname ID
##	* ITU
##	* Lenguajes
##	* Si es independiente