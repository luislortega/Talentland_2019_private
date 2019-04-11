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
    ## Fechas
    ano_base = 1993
    array_anos = []
        for x in range(0, 25):
            array_anos.append(ano_base)
            ano_base += 1

    def leer_pib_total(filename):
	    with open(filename, 'r') as csvfile: ## problem
		    csvFileReader = csv.reader(csvfile)
		    next(csvFileReader) 
		    for row in csvFileReader:
			    pib.append(row)
	    return

    def predict_price(dates, prices, x):
	    dates = np.reshape(dates,(len(dates), 1)) # converting to matrix of n X 1

	    svr_lin = SVR(kernel= 'linear', C= 1e3)
	    svr_poly = SVR(kernel= 'poly', C= 1e3, degree= 2)
	    svr_rbf = SVR(kernel= 'rbf', C= 1e3, gamma= 0.1) # defining the support vector regression models
	    svr_rbf.fit(dates, prices) # fitting the data points in the models
	    svr_lin.fit(dates, prices)
	    svr_poly.fit(dates, prices)

	    plt.scatter(dates, prices, color= 'black', label= 'Data') # plotting the initial datapoints 
	    plt.plot(dates, svr_rbf.predict(dates), color= 'red', label= 'RBF model') # plotting the line made by the RBF kernel
	    plt.plot(dates,svr_lin.predict(dates), color= 'green', label= 'Linear model') # plotting the line made by linear kernel
	    plt.plot(dates,svr_poly.predict(dates), color= 'blue', label= 'Polynomial model') # plotting the line made by polynomial kernel
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
    conexion_bd.insertar_dato(pib)

    ##AGREGAR REGRESION LINEAR 
    #predict_price