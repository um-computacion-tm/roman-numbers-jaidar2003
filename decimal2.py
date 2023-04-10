def decimal_a_romano(decimal):
    valores = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    simbolos = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    resultado = ""
    i = 0
    while decimal > 0:
        for _ in range(decimal // valores[i]):
            resultado += simbolos[i]
            decimal -= valores[i]
        i += 1
    return resultado

numero_decimal = 1068
numero_romano = decimal_a_romano(numero_decimal)
print(numero_romano)