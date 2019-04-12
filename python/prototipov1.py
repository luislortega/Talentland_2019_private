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

if __name__ == "__main__":
    print("Do something")