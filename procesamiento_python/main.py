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
from classes.conexionDB import ConexionDB
from classes.csvScanner import CsvScannerINEGI
from classes.controlador import ControladorDatos

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