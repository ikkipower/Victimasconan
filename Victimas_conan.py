#!/usr/python
# -*- coding: utf-8 -*-
import MySQLdb
# Establecemos la conexión
Conexion = MySQLdb.connect(host='localhost', user='conan',passwd='crom', db='DBdeConan')
# Creamos el cursor, pero especificando que sea de la subclase DictCursor
micursor = Conexion.cursor(MySQLdb.cursors.DictCursor);
# Insertamos un par de registros
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (1, \"Ejercito de Zombies\",\"Muertos Vivientes\",\"Desmembramiento a espada\");"
micursor.execute(query)
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (2, \"Vampiro feo\",\"Muertos Vivientes\",\"Estaca de madera\");"
micursor.execute(query)
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (3, \"Ejercito de Zombies\",\"Muertos Vivientes\",\"Desmembramiento a espada\");"
micursor.execute(query)
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (4, \"Vampiro feo\",\"Muertos Vivientes\",\"Estaca de madera\");"
micursor.execute(query)
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (5, \"Ejercito de Zombies\",\"Muertos Vivientes\",\"Desmembramiento a espada\");"
micursor.execute(query)
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (6, \"Vampiro feo\",\"Muertos Vivientes\",\"Estaca de madera\");"
micursor.execute(query)
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (7, \"Ejercito de Zombies\",\"Muertos Vivientes\",\"Desmembramiento a espada\");"
micursor.execute(query)
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (8, \"Vampiro feo\",\"Muertos Vivientes\",\"Estaca de madera\");"
micursor.execute(query)
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (9, \"Ejercito de Zombies\",\"Muertos Vivientes\",\"Desmembramiento a espada\");"
micursor.execute(query)
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (10, \"Vampiro feo\",\"Muertos Vivientes\",\"Estaca de madera\");"
micursor.execute(query)
