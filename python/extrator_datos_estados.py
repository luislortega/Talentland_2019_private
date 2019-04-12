## fecha desde 2003 hasta el 2017
import csv
import psycopg2
import json

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
        create_table_command = "CREATE TABLE pib_entidad_federativa(id serial PRIMARY KEY, nombre_entidad varchar(100), actividades_economicas JSON)"
        self.cursor.execute(create_table_command)
        print("Tabla creada")

    def insertar_dato(self, nombre, jsonData):
        #agrega la informacion
        print(nombre, jsonData)
        insert_command = "INSERT INTO pib_entidad_federativa(nombre_entidad, actividades_economicas) VALUES('"+nombre+"', '"+jsonData+"')"

        self.cursor.execute(insert_command)
        print("datos intertados")
# MAIN 
if __name__ == '__main__':
    data = []
    data_separado = []
    def leer_datos(filename):
        with open(filename, 'r') as csvfile:
            csvFileReader = csv.reader(csvfile)
            next(csvFileReader)
            for i, row in enumerate(csvfile):
                if i == 38:
                    break    
                data.append(row)
        return
    leer_datos('inegi_data/pib_estados/yucatan/pibe_entidad_yuc.csv')
    #Database
    conexion_bd = DatabaseConnection()
    #conexion_bd.crear_tablas()

    for i, item in enumerate(data):
        #print(item.split(","))
        data_separado.append(item.split(","))

    conexion_bd.insertar_dato("Yucatan", json.dumps(data_separado))
    