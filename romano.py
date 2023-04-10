def romano_a_decimal(romano):
    valores = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }
    resultado = 0
    previo = 0
    for letra in romano:
        valor = valores[letra]
        resultado += valor
        if valor > previo:
            resultado -= 2 * previo
        previo = valor
    return resultado

numero_romano = "IX"
numero_decimal = romano_a_decimal(numero_romano)
print(numero_decimal)