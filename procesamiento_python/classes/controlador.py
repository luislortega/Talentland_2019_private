class ControladorDatos:
    # Guardamos la entidades y poblaciones del 2010
    def controlador_poblacion_2010(self, database, datos):
        entidades_federativas = []
        poblacion = []

        for elemento in datos:
            entidades_federativas.append(elemento[0])
            poblacion.append({'2010':elemento[1]})
        
        print("[✔] datos del 2010 procesados")
        database.insertar_entidades_poblacion_2010(entidades_federativas, poblacion)
    # Obteno los resultados calculado desde el 2010 hasta el 2017 poblacion_2011 = poblacion_2010 + natalidad_2011 - mortalidad_2011 
    def controlador_poblacion_2010_2017(self, database, poblacion_2010, natalidad_2011_2017, mortalidad_2011_2017):
        lista_poblacion_2010 = []
        no_lista_poblacion = []
        lista_final = []

        for elemento_2010 in poblacion_2010:
            lista_final.append({"2010": elemento_2010[1]})
            lista_poblacion_2010.append(elemento_2010[1])
        
        for contador_ano in range(2011, 2018):
            entidad_federativa = 0
            for natalidad, mortalidad in zip(natalidad_2011_2017, mortalidad_2011_2017): 
                poblacion = int(lista_poblacion_2010[entidad_federativa]) + int(natalidad[str(contador_ano)]) - int(mortalidad[str(contador_ano)])       
                no_lista_poblacion.append({str(contador_ano):str(poblacion)})
                lista_poblacion_2010[entidad_federativa] = str(poblacion)
                entidad_federativa += 1

        for x in range(0, 32):
            lista_final[x] = {**lista_final[x], **no_lista_poblacion[x],**no_lista_poblacion[x+32], **no_lista_poblacion[x+64], **no_lista_poblacion[x+96], **no_lista_poblacion[x+128], **no_lista_poblacion[x+160], **no_lista_poblacion[x+192]}
        
        print("[✔] Calculos matematicos para obtener la poblacion hasta el 2017 Pt = Pi + Nt - Mt")
        database.insertar_poblacion_2010_2017(lista_final)
    