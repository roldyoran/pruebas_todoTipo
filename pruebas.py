mi_lista = [1, 3, 5, 7, 9]

# Imprimir el primer valor
primer_valor = mi_lista[0]
print(f"Primer valor: {primer_valor}, No tiene un valor anterior")

# Iterar sobre el resto de la lista
for i in range(1, len(mi_lista)):
    valor_actual = mi_lista[i]
    valor_anterior = mi_lista[i - 1]
    
    # Imprimir los valores actuales y anteriores
    print(f"Valor actual: {valor_actual}, Valor anterior: {valor_anterior}")

