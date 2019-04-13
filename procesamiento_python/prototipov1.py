'''
Condiciones:
PROTOTIPO FUNCIONAL ENTRE 2010 - ACTUALIDAD

Tipos de crecimiento y como obtenerlo.

Crecimiento poblacional:
    1. Extraer la poblacion total por entidad federativa
    2. Extraer la natalidad total por entidad federativa
    3. Extraer la mortalidad total por entidad federativa
    4. Calcular la natalidad 2010 hasta la actualidad (Angie)
    5. Calcular la mortalidad 2010 hasta el actualidad (Angie)
    6. Con los datos de mortalidad y natalidad calcular la poblacion total hasta 2018
    7. Sacar la prediccion de la poblacion 2019

Crecimiento economico:
    

'''
import csv
import psycopg2

class ConexionDB:
    def __init__(self):
        try:
            self.connection = psycopg2.connect("dbname='grupomodelo' user='postgres' host='localhost' password='1298Luis'")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            print("Backend running at port 8080 👽")
        except:
            print("Error en la conexion")

    def crear_tablas_postgres(self):
        create_table_command = "CREATE TABLE entidad_federativa(id serial PRIMARY KEY, nombre_entidad varchar(100), actividades_economicas JSON, poblacion JSON, natalidad JSON, mortalidad JSON)"
        self.cursor.execute(create_table_command)
        create_table_command = "CREATE TABLE pib_mexico(id serial PRIMARY KEY, ano int, data float)"
        self.cursor.execute(create_table_command)

    def limpiar_tablas_postgres(self):
        drop_table_command = "DROP TABLE entidad_federativa"
        self.cursor.execute(drop_table_command)
        drop_table_command = "DROP TABLE pib_mexico"
        self.cursor.execute(drop_table_command)

    def insertar_poblacion_entidades_2010(self):
        print("Do something")
        
    def insertar_pib_minado_INEGI(self):
        print("Do something")

    def insertar_pib_entidades_federativas_minado_INEGI(self):
        print("Do something")

class CsvScannerINEGI:
    def leer_poblacion_2010(self, filename):
        datos = []
        with open(filename, 'r') as csvfile:
            csvFileReader = csv.reader(csvfile)
            for i, row in enumerate(csvfile):
                datos.append(row)
        return datos

if __name__ == "__main__":
    dev = True #Para crear las tablas.

    poblacion_2010 = []

    sc = CsvScannerINEGI()
    db = ConexionDB()

    db.limpiar_tablas_postgres()
    db.crear_tablas_postgres()

    '''
        Poblacion 2010.
        Datos: @inegi
    '''
    poblacion_2010 = sc.leer_poblacion_2010('inegi_data/pob_entidades/Poblacion_01.csv')
    poblacion_2010 = poblacion_2010[4:]


    print(poblacion_2010)