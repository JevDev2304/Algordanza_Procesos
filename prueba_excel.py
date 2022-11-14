import pandas as pd
from openpyxl import Workbook
from ui import *


from openpyxl.styles import Font
import time

df = pd.read_excel(r"prueba_escritura.xlsx", index_col="Id")
filas = df.shape[0]
columnas = df.shape[1]
diccionario = df.to_dict()
print(diccionario)
diccionario_id_nombre = diccionario["Nombre"]
lista_de_nombres = diccionario_id_nombre.values()
print(lista_de_nombres)
lista_de_id = diccionario_id_nombre.keys()
print(lista_de_id)
print(filas)
print(columnas)
ui = ui()

diccionario_clave_fecha_valor_pedidos = informacion[0]
print(diccionario_clave_fecha_valor_pedidos.values())
lista_clientes = informacion[1]
print(lista_clientes)
book = Workbook()
sheet = book.active
sheet["A1"]="Nombre"
sheet["B1"]="Id"
sheet["C1"]="Correo"
sheet["D1"]="Ciudad"
sheet["E1"]="Celular"
contador=1
for cliente in lista_clientes:
    contador += 1
    sheet[f"A{contador}"]=cliente.nombre
    sheet[f"B{contador}"] = cliente.id
    sheet[f"C{contador}"] = cliente.correo
    sheet[f"D{contador}"] = cliente.ciudad
    sheet[f"E{contador}"] = cliente.celular


book.save("prueba_escritura.xlsx")
