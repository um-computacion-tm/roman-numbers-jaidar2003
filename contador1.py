def contar_palabras(frase):
  
    palabras = frase.split()
    conteo = {}

    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    
    return conteo

frase = "Hola mundo hola Python"
resultado = contar_palabras(frase)
#aidar

