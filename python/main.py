# Modificaciones a futuro
# - cambiar la precision de los datos proporcionados por la INEGI

import csv
import json
import psycopg2
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

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

    pib = []
    array_pib = []
    ## Fechas
    ano_base = 1993
    array_anos = []

    for x in range(0, 25):
        array_anos.append(ano_base)
        ano_base += 1

    def leer_pib_total(filename):
	    with open(filename, 'r') as csvfile:
		    csvFileReader = csv.reader(csvfile)
		    next(csvFileReader) 
		    for row in csvFileReader:
			    pib.append(row)
	    return

    # REPARA ESTOOOO
    def predict_price(dates, prices, x):
	    dates = np.reshape(dates,(len(dates), 1)) # convertir en una matriz de n x 1
	    svr_lin = SVR(kernel= 'linear')
	    svr_poly = SVR(kernel= 'poly', degree= 2)
	    svr_rbf = SVR(kernel= 'rbf',  gamma= 0.1) 
	    svr_rbf.fit(dates, prices)
	    svr_lin.fit(dates, prices)
	    svr_poly.fit(dates, prices)

	    plt.scatter(dates, prices, color= 'black', label= 'Data') # plotting the initial datapoints 
	    plt.plot(dates, svr_rbf.predict(dates), color= 'red', label= 'RBF model') # plotting the line made by the RBF kernel
	    plt.plot(dates,svr_lin.predict(dates), color= 'green', label= 'Modelo lineal') # plotting the line made by linear kernel
	    plt.plot(dates,svr_poly.predict(dates), color= 'blue', label= 'Modelo polinomial') # plotting the line made by polynomial kernel
	    plt.xlabel('Date')
	    plt.ylabel('Price')
	    plt.title('Support Vector Regression')
	    plt.legend()
	    plt.show()

	    return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]

    #Leer PIB de todos los años en todo mexico    
    leer_pib_total('inegi_data/pib_mexico/data.csv') 
    conexion_bd = DatabaseConnection()
    #conexion_bd.crear_tablas()
    array_pib = conexion_bd.insertar_dato(pib)

    predict_price(array_anos, array_pib, 25)

    #Mostrar graficos
    plt.plot(array_anos, array_pib)
    plt.scatter(array_anos, array_pib, color= 'black', label= 'Data') # plotting the initial datapoints 
    #Texto
    plt.ylabel("Millones de pesos")
    plt.xlabel("Años")
    plt.title("Producto interno bruto de Mexico")
    plt.show()

