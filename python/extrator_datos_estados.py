## fecha desde 2003 hasta el 2017
import csv
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
        create_table_command = "CREATE TABLE pib_entidad_federativa(id serial PRIMARY KEY, nombre_entidad varchar(100), actividades_economicas JSON)"
        self.cursor.execute(create_table_command)
        print("Tabla creada")

    def insertar_dato(self, pib):
        array_pib = []
        suma_pib = 0
        ano_base = 1993
        for x in range(0, 25):
            for i in range(0, 4):
                suma_pib += float(pib[i][x])
            #agrega la informacion
            insert_command = "INSERT INTO pib_mexico(ano, data) VALUES('"+ str(ano_base) + "', '"+ str(suma_pib) +"')"
            self.cursor.execute(insert_command)
            ano_base += 1 # Siguiente año
            array_pib.append(int(suma_pib))
            suma_pib = 0 # Reseteo de la suma
        return array_pib
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

    conexion_bd.crear_tablas()

    for i, item in enumerate(data):
        print(i)
        print(item)