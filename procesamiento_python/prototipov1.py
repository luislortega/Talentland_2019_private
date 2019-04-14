'''
@author: Monkey Coders

Este prototipo en Python con estandar MVC, filtra y procesa los datos para poder ser exportado a otras plataformas.

Condiciones:
2010 - Actualidad

Mineria de datos.
    poblacion, natalidad, mortalidad: https://www.inegi.org.mx/
    conapo: https://datos.gob.mx/busca/dataset/proyecciones-de-la-poblacion-de-mexico-y-de-las-entidades-federativas-2016-2050/resource/a31f9dbb-4f65-47da-ba44-50eb44a9ad25

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
            print("[x] Error en la conexion")

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
                    datos_entidad[1] = datos_entidad[1].replace("\n","")
                    datos.append(datos_entidad)
        
        print("[✔] Poblacion del 2010 minada. Fuente: INEGI")
        return datos
    
    # Extrae los datos minados de inegi sobre la natalidad 2011 - 2017
    def leer_natalidad_2011_2017(self, filename):
        natalidad_2011_2017 = []
        natalidad_ordenada = []

        with open(filename, 'r') as csvfile:
            csvFileReader = csv.reader(csvfile)
            for i, row in enumerate(csvfile):
                if i >= 4:
                    natalidad_2011_2017.append(row.split(";"))

        for i, elemento in enumerate(natalidad_2011_2017):
            ultimo_elemento = natalidad_2011_2017[i][8].replace("\n","")
            natalidad_ordenada.append({"2011": natalidad_2011_2017[i][2], "2012": natalidad_2011_2017[i][3], "2013": natalidad_2011_2017[i][4], "2014": natalidad_2011_2017[i][5], "2015": natalidad_2011_2017[i][6], "2016":natalidad_2011_2017[i][7], "2017": ultimo_elemento})
        
        print("[✔] Natalidad del 2011 - 2017 minada. Fuente: INEGI")
        return natalidad_ordenada

    # Extrae los datos minados de inegi sobre la mortalidad 2011 - 2017
    def leer_mortalidad_2011_2017(self, filename):
        mortalidad_2011_2017 = []
        mortalidad_ordenada = []
        
        with open(filename, 'r') as csvfile:
            csvFileReader = csv.reader(csvfile)
            for i, row in enumerate(csvfile):
                if i >= 4:
                    mortalidad_2011_2017.append(row.split(";"))
        
        for i, elemento in enumerate(mortalidad_2011_2017):
            ultimo_elemento = mortalidad_2011_2017[i][8].replace("\n","")
            mortalidad_ordenada.append({"2011": mortalidad_2011_2017[i][2], "2012": mortalidad_2011_2017[i][3], "2013": mortalidad_2011_2017[i][4], "2014": mortalidad_2011_2017[i][5], "2015": mortalidad_2011_2017[i][6], "2016":mortalidad_2011_2017[i][7], "2017": ultimo_elemento})
        
        print("[✔] Mortalidad del 2011 - 2017 minada. Fuente: INEGI")
        return mortalidad_ordenada

class ControladorDatos:
    # Guardamos la entidades y poblaciones del 2010
    def controlador_poblacion_2010(self, database, datos):
        entidades_federativas = []
        poblacion = []

        for elemento in datos:
            entidades_federativas.append(elemento[0])
            poblacion.append({'2010':elemento[1]})

        database.insertar_entidades_poblacion_2010(entidades_federativas, poblacion)
    # Obteno los resultados calculado desde el 2010 hasta el 2017 poblacion_2011 = poblacion_2010 + natalidad_2011 - mortalidad_2011 
    def controlador_poblacion_2010_2017(self, poblacion_2010, natalidad_2011_2017, mortalidad_2011_2017):
        
        lista_poblacion_2010 = []
        no_lista_poblacion = []

        #Obtengo solo el PIB 2010 de la entidad
        for elemento_2010 in poblacion_2010:
            lista_poblacion_2010.append(elemento_2010[1])
        
        for contador_ano in range(2011, 2018):
            lugar = 0
            for natalidad, mortalidad in zip(natalidad_2011_2017, mortalidad_2011_2017): 
                poblacion = int(lista_poblacion_2010[lugar]) + int(natalidad[str(contador_ano)]) - int(mortalidad[str(contador_ano)])       
                print("AÑO: "+ str(contador_ano)+" Posicion: " +str(lugar) +" Poblacion guardada:" +lista_poblacion_2010[lugar]+ " NATALIDAD: "+natalidad[str(contador_ano)]+ " MORTALIDAD: "+mortalidad[str(contador_ano)])
                print("Poblacion total "+str(poblacion))
                lista_poblacion_2010[lugar] = str(poblacion)
                lugar += 1
           # print("HERE is"+str(contador_ano))
        #for natalidad, mortalidad in zip(natalidad_2011_2017, mortalidad_2011_2017):
            #print()
        print("[DEV] Calculando la poblacion 2010 - 2017 con la recopilacion de datos")
    
if __name__ == "__main__":
    #Contenedores de informacion
    poblacion_2010 = []
    natalidad_2011_2017 = []
    mortalidad_2011_2017 = []
    poblacion_2010_2017 = []

    #Utilidades
    scanner = CsvScannerINEGI()
    database = ConexionDB()
    controlador = ControladorDatos()

    #Base de datos
    database.limpiar_tablas_postgres()
    database.crear_tablas_postgres()

    '''
        Poblacion 2010.
        Datos: @inegi
    '''
    poblacion_2010 = scanner.leer_poblacion_2010('inegi_data/pob_entidades/Poblacion_01.csv')
    '''
        Natalidad 2011 - 2017.
        Datos: @inegi
    '''
    natalidad_2011_2017 = scanner.leer_natalidad_2011_2017('inegi_data/pob_entidades/Natalidad_01.csv')
    '''
        Moratlidad 2011 - 2017.
        Datos: @inegi
    '''
    mortalidad_2011_2017 = scanner.leer_mortalidad_2011_2017('inegi_data/pob_entidades/Mortalidad_01.csv')

    #Logica
    poblacion_2010_2017 = controlador.controlador_poblacion_2010_2017(poblacion_2010, natalidad_2011_2017, mortalidad_2011_2017)

    #controladores
    controlador.controlador_poblacion_2010(database, poblacion_2010)


#print(natalidad_2011_2017)
    #test = {"t":1}
        #z = {**test, **natalidad_ordenada[0]}
        #test = {**test + **natalidad_ordenada}
        #print(natalidad_ordenada)