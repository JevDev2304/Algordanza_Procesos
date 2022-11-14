def pasar_str_productos_a_dict(string):
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


    lista_diamante_corte = []
    lista_diamante_bruto = []
    for str_diamante in lista_diamantes:
        if len(str_diamante) > 100:
            lista_diamante_corte.append(str_diamante)
        else:
            lista_diamante_bruto.append(str_diamante)

    lista_diamante_bruto_split_el = []
    lista_diamante_corte_split_el = []
    for diamante_bruto_str in lista_diamante_bruto:
        lista_diamante_bruto_split_el.append(diamante_bruto_str.split("El"))
    for diamante_corte_str in lista_diamante_corte:
        lista_diamante_corte_split_el.append(diamante_corte_str.split("El"))
    for lista_diamante in lista_diamante_bruto_split_el:
        del lista_diamante[0]
    for lista_diamante in lista_diamante_corte_split_el:
        del lista_diamante[0]
    for lista_diamante in lista_diamante_corte_split_el:
        lista_diamante[0] = lista_diamante[0].replace(" tamaño del Diamante es ","")
        lista_diamante[1] = lista_diamante[1].replace(" grabado del Diamante es ","")
        lista_diamante[2] = lista_diamante[2].replace(" origen del diamante es ","")
        lista_diamante[3] = lista_diamante[3].replace(" corte del diamante es ","")
    for lista_diamante in lista_diamante_bruto_split_el:
        lista_diamante[0] = lista_diamante[0].replace(" tamaño del Diamante es ","")
        lista_diamante[1] = lista_diamante[1].replace(" grabado del Diamante es ","")
        lista_diamante[2] = lista_diamante[2].replace(" origen del diamante es ","")
    print(lista_diamante_corte_split_el)
    print(lista_diamante_bruto_split_el)
    diccionario={"Diamantes_Bruto":lista_diamante_bruto_split_el,"diamante_corte":lista_diamante_corte_split_el}
    return diccionario



