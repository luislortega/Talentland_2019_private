'''
@author: Monkey Coders

Este prototipo en Python filtra y procesa los datos para poder ser exportado a otras plataformas.

Condiciones:
2010 - Actualidad

Informacion obtenida desde la base de datos de INEGI.
    url: https://www.inegi.org.mx/

Crecimiento poblacional:
    1. Extraer la poblacion total por entidad federativa
    2. Extraer la natalidad total por entidad federativa
    3. Extraer la mortalidad total por entidad federativa
    4. Calcular la natalidad 2010 hasta la actualidad (Angie)
    5. Calcular la mortalidad 2010 hasta el actualidad (Angie)
    6. Con los datos de mortalidad y natalidad calcular la poblacion total hasta 2018   
    7. Sacar la prediccion de la poblacion 2019

Crecimiento economico:
    En proceso...
'''
import csv
import psycopg2
import json

class ConexionDB:
    def __init__(self):
        try:
            self.connection = psycopg2.connect("dbname='grupomodelo' user='postgres' host='localhost' password='1298Luis'")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            print("[✔] Base de datos conectada")
        except:
            print("Error en la conexion")

    def crear_tablas_postgres(self):
        create_table_command = "CREATE TABLE entidad_federativa(id serial PRIMARY KEY, nombre_entidad varchar(100), lat varchar, long varchar, actividades_economicas JSON, poblacion JSON, natalidad JSON, mortalidad JSON)"
        self.cursor.execute(create_table_command)
        create_table_command = "CREATE TABLE pib_mexico(id serial PRIMARY KEY, ano int, data float)"
        self.cursor.execute(create_table_command)
        print("[✔] Tablas creadas")

    def limpiar_tablas_postgres(self):
        drop_table_command = "DROP TABLE entidad_federativa"
        self.cursor.execute(drop_table_command)
        drop_table_command = "DROP TABLE pib_mexico"
        self.cursor.execute(drop_table_command)
        print("[✔] Limpieza en las tablas")

    def insertar_entidades_poblacion_2010(self, entidades, poblacion):
        for i, elemento in enumerate(entidades):
            insert_command = "INSERT INTO entidad_federativa(nombre_entidad, poblacion) VALUES('"+elemento+"', '"+json.dumps(poblacion[i])+"')"
            self.cursor.execute(insert_command)
        print("[✔] Indetidades federativas insertadas con su poblacion en 2010")
    
        
class CsvScannerINEGI:
    # Extrae los datos minados de inegi sobre la poblacion 2010
    def leer_poblacion_2010(self, filename):
        datos = []
        with open(filename, 'r') as csvfile:
            csvFileReader = csv.reader(csvfile)
            for i, row in enumerate(csvfile):
                if i >= 4:
                    datos_entidad = row.split(";")
                    datos_entidad.pop(1)
                    datos_entidad[0] = datos_entidad[0].replace('"',"")
                    datos_entidad[1] = datos_entidad[1].replace('"',"")
                    datos_entidad[1] = datos_entidad[1].replace('\n',"")
                    datos.append(datos_entidad)
        return datos
    
    # Extrae los datos minados de inegi sobre la natalidad 2011 - 2017
    def leer_natalidad_2011_2017(self, filename):
        print("[DEV] Lectura de la natalidad 2010 hasta 2017")
        natalidad_2011_2017 = []

        with open(filename, 'r') as csvfile:
            csvFileReader = csv.reader(csvfile)

            for i, row in enumerate(csvfile):
                if i >= 4:
                    natalidad_2011_2017.append(row.split(";"))

        natalidad_2011_2017 = natalidad_2011_2017[0:len(natalidad_2011_2017)-1]
        
        for i, elemento in enumerate(natalidad_2011_2017):
            for j, datos in enumerate(elemento):
                print(i,datos)                      
        return

class ControladorDatos:
    # Guardamos la entidades y poblaciones del 2010
    def controlador_poblacion_2010(self, database, datos):
        entidades_federativas = []
        poblacion = []

        for elemento in datos:
            entidades_federativas.append(elemento[0])
            poblacion.append({'2010':elemento[1]})

        database.insertar_entidades_poblacion_2010(entidades_federativas, poblacion)

if __name__ == "__main__":
    poblacion_2010 = []
    natalidad_2011_2017 = []
    mortalidad_2011_2017 = []

    scanner = CsvScannerINEGI()
    database = ConexionDB()
    controlador = ControladorDatos()

    database.limpiar_tablas_postgres()
    database.crear_tablas_postgres()

    '''
        Poblacion 2010.
        Datos: @inegi
    '''
    poblacion_2010 = scanner.leer_poblacion_2010('inegi_data/pob_entidades/Poblacion_01.csv')
    controlador.controlador_poblacion_2010(database, poblacion_2010)
    '''
        Natalidad 2011 - 2017
        Datos: @inegi
    '''
    natalidad_2011_2017 = scanner.leer_natalidad_2011_2017('inegi_data/pob_entidades/Natalidad_01.csv')
    '''
        Moratlidad 2011 - 2017
        Datos: @inegi
    '''