string = """El tamaño del Diamante es 0.3
El grabado del Diamante es True
El origen del diamante es Cabello
El corte del diamante es Princesa

El tamaño del Diamante es 0.4
El grabado del Diamante es True
El origen del diamante es Cenizas

El tamaño del Diamante es 0.7
El grabado del Diamante es False
El origen del diamante es Cabello

El tamaño del Diamante es 0.8
El grabado del Diamante es False
El origen del diamante es Cabello
El corte del diamante es Esmeralda

"""
lista = string.split("\n")
acumulador = ""
lista_diamantes = []
del lista[-1]
for x in lista:
    acumulador += x
    if x == "":
        print(acumulador)
        lista_diamantes.append(acumulador)
        acumulador = ""

print(lista_diamantes)
lista_diamante_corte = []
lista_diamante_bruto = []
for str_diamante in lista_diamantes:
    if len(str_diamante) > 100:
        lista_diamante_corte.append(str_diamante)
    else:
        lista_diamante_bruto.append(str_diamante)
print(lista_diamante_bruto)
print(lista_diamante_corte)
lista_diamante_bruto_split_el = []
lista_diamante_corte_split_el = []
for diamante_bruto_str in lista_diamante_bruto:
    lista_diamante_bruto_split_el.append(diamante_bruto_str.split("El"))
for diamante_corte_str in lista_diamante_corte:
    lista_diamante_corte_split_el.append(diamante_corte_str.split("El"))
print(lista_diamante_bruto_split_el)
print(lista_diamante_corte_split_el)

