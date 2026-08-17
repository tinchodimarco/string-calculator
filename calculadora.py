def sumar(numeros):
    if not numeros:
        return 0
    
    partes = numeros.split(",")
    return sum(int(n) for n in partes)