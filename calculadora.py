def sumar(numeros):
    if not numeros:
        return 0

    delimitador = ","
    
    if numeros.startswith("//"):
        encabezado, numeros = numeros.split("\n", 1)
        delimitador = encabezado[2:]  

    numeros_limpios = numeros.replace("\n", ",").replace(delimitador, ",")
    partes = numeros_limpios.split(",")
    
    return sum(int(n) for n in partes)