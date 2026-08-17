def sumar(numeros):
    if not numeros:
        return 0
    partes = numeros.split(",")[:2] 
    return sum(int(n) for n in partes)