def sumar(numeros):
    if not numeros:
        return 0
    
    numeros_limpios = numeros.replace("\n", ",")
    partes = numeros_limpios.split(",")
    return sum(int(n) for n in partes)