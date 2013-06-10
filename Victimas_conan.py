#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Victimas_conan.py
#       
#  Copyright 2013 Sergio Morlans <https://github.com/ikkipower/Victimasconan.git>
#       
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#       
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#       
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

import MySQLdb
# Establecemos la conexión
Conexion = MySQLdb.connect(host='localhost', user='conan',passwd='crom', db='DBdeConan')
# Creamos el cursor, pero especificando que sea de la subclase DictCursor
micursor = Conexion.cursor(MySQLdb.cursors.DictCursor);
# Insertamos un par de registros
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (1, \"Pepe\",\"Asesino\",\"Degollado\");"
micursor.execute(query)
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (2, \"Jose\",\"Jinete\",\"Estaca de madera\");"
micursor.execute(query)
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (3, \"Hodor\",\"Asesino\",\"Desmembramiento a espada\");"
micursor.execute(query)
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (4, \"Joffrey\",\"Jinete\",\"Estaca de madera\");"
micursor.execute(query)
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (5, \"Robb\",\"Soldado\",\"Decapitado\");"
micursor.execute(query)
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (6, \"Kitt\",\"Asesino\",\"Estaca de madera\");"
micursor.execute(query)
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (7, \"Ross\",\"Soldado\",\"Desmembramiento a espada\");"
micursor.execute(query)
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (8, \"Ned\",\"Asesino\",\"Estaca de madera\");"
micursor.execute(query)
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (9, \"Stannis\",\"Soldado\",\"Degollado\");"
micursor.execute(query)
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (10, \"Brandon\",\"Jinete\",\"DecapitadoPepe\");"
micursor.execute(query)
Conexion.commit()

idlist = [1,2,3,4,5,6,7,8,9,10]
listcond = ['S','s']
print listcond;
cond = True

while cond == True:
  print "Inserte un nuevo elemento:"
  ident = idlist[len(idlist)-1]+1;
  print ident
  idlist.append(ident)
  print idlist
  condname = True
  condprof = True
  condead = True 
	
  while condname == True:
    name = raw_input("Nombre: ")
    if name == "":
       condname = True
       print "[Error] No se puede dejar vacio el campo:"
    else:
       condname = False
  
    
  while condprof == True:
    prof = raw_input("Profesion: ")
    if prof == "":
       condprof = True
       print "[Error] No se puede dejar vacio el campo:"
    else:
       condprof = False  
    
  while condead == True:
    dead = raw_input("Muerte: ")
    if dead == "":
       condead = True
       print "[Error] No se puede dejar vacio el campo:"
    else:
       condead = False
	
  #control strings vacíos
  query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES ("+str(ident)+",\""+name+"\",\""+prof+"\",\""+dead+"\");"
  micursor.execute(query)	
  #condición para insertar mas de un registro
  print "Registro insertado!"
  conds = raw_input("Si desea insertar otro registro pulse [S/s]: ")
  print conds
  if (conds == "S" or conds == "s"):
     cond = True
  else:
     cond = False


# Ahora vamos a hacer un SELECT
query= "SELECT * FROM Victimas WHERE 1;"
micursor.execute(query)
Conexion.commit()
# Obtenemos el resultado con fetchall
registros= micursor.fetchall()

for registro in registros:
	# ... imprimimos el registro...
	#print str(registro["id"]) + ", Nombre: " + registro["Nombre"] + " es del tipo " + registro["Profesion"] + " y murio por " + registro["Muerte"]
    listrg = [str(registro["id"]),registro["Nombre"],registro["Profesion"],registro["Muerte"]]
    print "\t".join(listrg)
    
micursor.close () 
Conexion.close () 

