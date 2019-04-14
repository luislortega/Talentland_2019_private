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
        lista_final = []

        #Obtengo solo el PIB 2010 de la entidad
        for elemento_2010 in poblacion_2010:
            lista_final.append({"2010": elemento_2010[1]})
            lista_poblacion_2010.append(elemento_2010[1])
        
        for contador_ano in range(2011, 2018):
            entidad_federativa = 0
            for natalidad, mortalidad in zip(natalidad_2011_2017, mortalidad_2011_2017): 
                poblacion = int(lista_poblacion_2010[entidad_federativa]) + int(natalidad[str(contador_ano)]) - int(mortalidad[str(contador_ano)])       
                print("AÑO: "+ str(contador_ano)+" Posicion: " +str(entidad_federativa) +" Poblacion guardada:" +lista_poblacion_2010[entidad_federativa]+ " NATALIDAD: "+natalidad[str(contador_ano)]+ " MORTALIDAD: "+mortalidad[str(contador_ano)])
                print("Poblacion total "+str(poblacion))
                no_lista_poblacion.append({str(contador_ano):str(poblacion)})
                lista_poblacion_2010[entidad_federativa] = str(poblacion)
                entidad_federativa += 1
        
        test = {"t":1}
        test2 = {"1":2}
        z = {**test, **test2}
        #test = {**test + **natalidad_ordenada}
        print(z)
        # RECORRIDO 
        for x in range(0, 32):
            #lista_final[x] = {**lista_final[x], {"2011": "test"}} 
            z = {"2011": "test"} 
            y = {**lista_final[x], **z}
            #print(lista_final[x])
            print(no_lista_poblacion[x+32])

        #print(lista_final)
        print("[DEV] Calculando la poblacion 2010 - 2017 con la recopilacion de datos")
    