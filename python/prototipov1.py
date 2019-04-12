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

class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = psycopg2.connect("dbname='grupomodelo' user='postgres' host='localhost' password='1298Luis'")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            print("Conectado a la base de datos.")
        except:
            print("Error en la conexion")

    def crear_tablas_postgres(self):
        #Entidades federativas
        create_table_command = "CREATE TABLE pib_entidad_federativa(id serial PRIMARY KEY, nombre_entidad varchar(100), actividades_economicas JSON)"
        self.cursor.execute(create_table_command)
        #Pib total en México
        create_table_command = "CREATE TABLE pib_mexico(id serial PRIMARY KEY, ano int, data float)"
        self.cursor.execute(create_table_command)
        print("Tablas creadas")

    def insertar_pib_minado_INEGI(self):
        print("Do something")

    def insertar_pib_entidades_federativas_minado_INEGI(self):
        print("Do something")

class CsvScannerINEGI:

    def leer_datos(self, filename):
        with open(filename, 'r') as csvfile:
            csvFileReader = csv.reader(csvfile)
            next(csvFileReader)
            for i, row in enumerate(csvfile):
                print(row)
        return

if __name__ == "__main__":
    sc = CsvScannerINEGI()
    sc.leer_datos('inegi_data/pob_entidades/poblacion_inegi.csv')
    print("Do something")
