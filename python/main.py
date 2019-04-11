# Modificaciones a futuro
# - cambiar la precision de los datos proporcionados por la INEGI

import csv
import json
import psycopg2

# DATABASE CONNECTION
class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = psycopg2.connect("dbname='grupomodelo' user='postgres' host='localhost' password='1298Luis'")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            print("Conectado a la base de datos.")
        except:
            print("Error en la conexion")
    def crear_tablas(self):
        create_table_command = "CREATE TABLE pib_mexico(id serial PRIMARY KEY, ano int, data float)"
        self.cursor.execute(create_table_command)
        print("Tabla creada")

    def insertar_dato(self, pib):

        suma_pib = 0
        ano_base = 1993
        for x in range(0, 25):
            for i in range(0, 4):
                suma_pib += float(pib[i][x])
            
            #agrega la informacion
            insert_command = "INSERT INTO pib_mexico(ano, data) VALUES('"+ str(ano_base) + "', '"+ str(suma_pib) +"')"
            self.cursor.execute(insert_command)

            ano_base += 1 # Siguiente año
            suma_pib = 0 # Reseteo de la suma
# MAIN 
if __name__ == '__main__':

    pib = []

    def leer_pib_total(filename):
	    with open(filename, 'r') as csvfile:
		    csvFileReader = csv.reader(csvfile)
		    next(csvFileReader) 
		    for row in csvFileReader:
			    pib.append(row)
	    return
        
    #Leer PIB de todos los años en todo mexico    
    leer_pib_total('data.csv') 
    conexion_bd = DatabaseConnection()
    #conexion_bd.crear_tablas()
    conexion_bd.insertar_dato(pib)