# Hackathon
La generación de grandes ciudades en México supone un gran impulsor económico que representa una mejora en el bienestar de las personas, pues al haber una mayor concentración de personas en un mismo lugar se produce un mayor encuentro entre la oferta y la demanda del mercado. De este modo, la aglomeración de personas en un mismo lugar provoca “economías de escalas” provocando que el costo medio por persona de determinados servicios se reduzca en función del aumento de la población.
 
Cada vez más gente emigra de sus pueblos natales en busca de alguna gran ciudad donde desarrollarse de manera personal y profesional. Existen ciudades receptoras naturales de población que habita en zonas aledañas a poblaciones pequeñas, que se desplazan al centro urbano más cercano, tal vez por el desgaste de sus condiciones personales.

De 2006-2011 62% del PIB de México se generó en 32 ciudades. Sin embargo, México no mide la actividad económica a nivel ciudades de manera constante y oportuna. El INEGI reporta anualmente el Producto Interno Bruto de las Entidades Federativas (PIBE) con 12 meses de rezago y pública la actividad económica trimestral en las entidades a través del Indicador Trimestral de Actividad Económica Estatal (ITAEE).

Lo anterior ha llevado a que se hayan hecho esfuerzos para crear nuevas formas de medir la actividad económica de las ciudades usando métodos de ciencia de datos. Instituciones como el Instituto Mexicano para la Competitividad (IMCO) crearon la Medición de la Actividad Económica con Grandes Datos (MAGDA) utilizando imágenes satelitales para medir la luminosidad de ciudades y la información transaccional de la Comisión Nacional Bancaria de Valores (CNVB)
## Entregables:
1. Construir un modelo estadístico que explique el crecimiento económico a nivel entidad federativa en México. Dicho modelo deberá estar construido con datos públicos abiertos y el código, repositorio y metodología deberán ser claramente explicados y entregados para su evaluación. Se deberá demostrar que el modelo tiene una precisión alta comparándola con datos públicos de crecimiento económico por entidad federativa publicados por fuentes oficiales como el Producto Interno Bruto de las Entidades Federativas (PIBE) y el Indicador Trimestral de Actividad Económica Estatal (ITAEE). Se deberá proveer la precisión obtenida contra dichos indicadores (métricas).

2. Una vez construido el modelo estadístico y teniendo los datos de crecimiento económico por entidad federativa, se deberá hacer un análisis factorial en el que se explique detalladamente cuáles son los factores que explican el crecimiento económico. En dicho análisis se debe incluir una comparación entre las entidades federativas que más crecieron durante el periodo de análisis y las que menos crecieron. Se deberán explicar casos especiales y se podrá hacer un análisis a nivel zonas metropolitanas.

3. Finalmente, una vez terminado el modelo estadístico se deberá responder a la pregunta: ¿Qué puede hacer una compañía como Grupo Modelo para estimular el crecimiento económico en las entidades federativas de México?

## Elementos a evaluar
* Respuesta a las 3 fases del problema
* Accuracy
* False Discovery Rate
* Rigor matemático
* Calidad de código

Para la solución final (Webapp, etc.):

* Escalabilidad de la aplicación
* No delay en el cálculo

## Apis
Lista de APIS abiertas:
https://datos.gob.mx/blog/catalogo-apidatosgobmx?category=api-cdn&tag=nula

Banco estadistico:
https://www.inegi.org.mx/servicios/widgets_indicadores.html

Estudio sobre el PIB y como calcularlo:
https://blocs.xtec.cat/economiaiesbaixmontseny/unitat-7-macroeconomia/7-7/

PIB por entidad federativa:
https://www.inegi.org.mx/programas/pibent/2013/default.html#Datos_abiertos

Visualizaciones graficas:
1. https://www.investing.com/webmaster-tools/

2. https://es.tradingview.com/

Predicciones:
1. https://www.youtube.com/watch?v=SSu00IRRraY

BitMex API:
https://www.youtube.com/watch?v=X3OYHu1tQkA

## Idea
Nuestra idea para tener un calculo del producto interno bruto es sencillo, para calcular el PIB se tienen en cuenta 4 variables.
1. Consumo

Información que mide la evolución del gasto realizado por los hogares en bienes y servicios de consumo, tanto de origen nacional como importado, permitiendo con ello dar seguimiento de forma mensual al componente más significativo del producto, por el lado de la demanda.

http://www.beta.inegi.org.mx/temas/imcp/

2. Inversion
3. Gasto publico
4. Exportaciones netas

## Datos que se pueden usar
* el Producto Interno Bruto de las Entidades Federativas (PIBE
* Indicador Trimestral de Actividad Económica Estatal (ITAEE).
* información transaccional de la Comisión Nacional Bancaria de Valores (CNVB)