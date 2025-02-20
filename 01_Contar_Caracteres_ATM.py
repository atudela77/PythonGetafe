entrada = 'hola'
abecedario = 'abcdefghijklmnñopqrstuvwxyz'
especiales = 'áéíóúü'
corregidas = 'aeiouu'
texto = "Inició su carrera como redactora en la revista Sintonía en la década de 1930 bajo el seudónimo de Mitzy. " \
        "Incursionó como cancionista en una serie de programas radiofónicos hasta que sus dotes para la comedia la " \
        "llevaron a participar como actriz y formar un dúo cómico con Juan Carlos Thorry. Su popularidad fue en aumento" \
        "y Manuel Romero la incorporó como actriz protagónica y guionista en la película Mujeres que trabajan (1938). " \
        "Entre 1939 y 1940, encabezó una trilogía dirigida por Romero que incluyó los filmes Divorcio en Montevideo, " \
        "Casamiento en Buenos Aires y Luna de miel en Río."    
for i in range(len(especiales)):
    texto.replace(especiales[i], corregidas[i])
diccionario = {letra: texto.lower().count(letra.lower()) for letra in abecedario}
print(diccionario)
print(texto)
