import csv

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
        # AQUI ELIMINAR EL ULTIMO ELEMENTO DE LA LISTA
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
        # AQUI ELIMINAR EL ULTIMO ELEMENTO DE LA LISTA
        for i, elemento in enumerate(mortalidad_2011_2017):
            ultimo_elemento = mortalidad_2011_2017[i][8].replace("\n","")
            mortalidad_ordenada.append({"2011": mortalidad_2011_2017[i][2], "2012": mortalidad_2011_2017[i][3], "2013": mortalidad_2011_2017[i][4], "2014": mortalidad_2011_2017[i][5], "2015": mortalidad_2011_2017[i][6], "2016":mortalidad_2011_2017[i][7], "2017": ultimo_elemento})
        
        print("[✔] Mortalidad del 2011 - 2017 minada. Fuente: INEGI")
        return mortalidad_ordenada

    # Extrae los datos minados de CONAPO, sobre la mortalidad 2011 - 2017
    def leer_poblacion_2018(self, filename):
        poblacion_2018 = []
        poblacion_2019 = []
        poblacion_2018_2019 = []

        with open(filename, 'r') as csvfile:
            csvFileReader = csv.reader(csvfile)
            for row in csvfile:
                if(row.split(",")[1] == '2018' and row.split(",")[2] != 'República Mexicana'):
                    poblacion_2018.append(row.split(",")[6])
                if(row.split(",")[1] == '2019' and row.split(",")[2] != 'República Mexicana'):
                    poblacion_2019.append(row.split(",")[6])

        poblacion_2018_2019 = [poblacion_2018, poblacion_2019]
        print("[✔] Poblacion 2018-2019 minados. Fuente: CONAPO")
        return poblacion_2018_2019
        
    def leer_patentes_2015_2018(self, filename):
        print("[DEV] Patentes por entidad federativa 2015 - 2018. Fuente: IMPI")