# -*- coding: utf-8 -*-
"""Algordanza.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-OjQBU2L7wL-26asQd0jC0OoBmnB4VAe
"""

from datetime import datetime
import pandas as pd
from openpyxl import Workbook


class Diamante:
    TAMANOS = {0.2: "0.2", 0.3: "0,3", 0.4: "0,4", 0.5: "0,5", 0.6: "0,6", 0.7: "0,7", 0.8: "0,8", 0.9: "0,9", 1: "1"}
    ORIGEN = ["Mascota", "Cabello", "Cenizas"]

    def __init__(self, tamano: int, grabado_laser: bool, origen: str):
        self.tamano = tamano
        self.grabado = grabado_laser
        self.origen = origen

    def __str__(self):
        return (
            f"El tamaño del Diamante es {self.tamano}\nEl grabado del Diamante es {self.grabado}\nEl origen del "
            f"diamante es {self.origen}")


class DiamanteCorte(Diamante):
    CORTES: list = ["Brillante", "Esmeralda", "Asscher", "Princesa", "Radiante", "Corazon"]

    def __init__(self, corte: str, tamano, grabado_laser, origen):
        super().__init__(tamano, grabado_laser, origen)
        self.corte = corte

    def __str__(self):
        return (
            f"El tamaño del Diamante es {self.tamano}\nEl grabado del Diamante es {self.grabado}\nEl origen del "
            f"diamante es {self.origen}\nEl corte del diamante es {self.corte}")


class Cliente:
    def __str__(self):
        return self.nombre

    id = 0

    def __init__(self, nombre: str, celular: str, correo: str, ciudad: str):
        Cliente.id += 1
        self.id = Cliente.id
        self.nombre = nombre
        self.celular = celular
        self.correo = correo
        self.ciudad = ciudad
        self.direccion = None


class Productos:

    def __init__(self):
        self.listadeDiamantes = []

    def __str__(self):
        return str(self.listadeDiamantes)

    def agregar_productos_a_lista(self):
        condicional_ciclo = int(input(
            "Ingrese 1 si desea ingresar Diamante\nIngrese 0 si no desea ingresar más Diamantes\nIngrese la respuesta: "))
        while condicional_ciclo == 1:
            tiene_corte = int(input(
                "Ingrese 1 si el diamante tiene corte\nIngrese 0 si el diamante no tiene corte\nIngrese la Respuesta: "))
            if tiene_corte == 1:
                corte = str(input("Cual es el corte del Diamante?"))
                tamano = str(input("Cual es el tamaño del Diamante?"))
                grabado_laser = bool(input("Tiene grabado el Diamante?"))
                origen = str(input("Cual es el origen del Diamante?"))
                self.agregar_diamante_con_corte_a_lista_productos(corte, tamano, grabado_laser, origen)
                condicional_ciclo = int(input(
                    "Ingrese 1 si desea ingresar Diamante\nIngrese 0 si no desea ingresar más Diamantes\nIngrese la "
                    "respuesta: "))
            elif tiene_corte == 0:
                tamano = str(input("Cual es el tamaño del Diamante?"))
                grabado_laser = bool(input("Tiene grabado el Diamante?"))
                origen = str(input("Cual es el origen del Diamante?"))
                self.agregar_diamante_sin_corte_a_lista_productos(tamano, grabado_laser, origen)
                condicional_ciclo = int(input(
                    "Ingrese 1 si desea ingresar Diamante\nIngrese 0 si no desea ingresar más Diamantes\nIngrese la respuesta: "))

    def agregar_diamante_sin_corte_a_lista_productos(self, tamano, grabado, origen):
        diamante = Diamante(tamano, grabado, origen)
        self.listadeDiamantes.append(diamante)

    def agregar_diamante_con_corte_a_lista_productos(self, corte, tamano, grabado_laser, origen):
        diamante_con_corte = DiamanteCorte(corte, tamano, grabado_laser, origen)
        self.listadeDiamantes.append(diamante_con_corte)


class Pedido:
    id = 0

    def __init__(self, cliente: Cliente, fecha: datetime.date, productos: Productos):
        Pedido.id += 1
        self.id = Pedido.id
        self.cliente = cliente
        self.fecha = fecha
        self.productos = productos
        self.activo: bool = True

    def __str__(self):
        return (
            f"El id del pedido es {self.id}\nEl nombre del cliente es {self.cliente}\nLa fecha del pedido es {self.fecha}\nLa lista del productos es {self.productos}\nEl estado del pedido es {self.activo}")


class Algordanza:
    def __init__(self):
        self.diccionariodepedidos: dict[Pedido] = {}
        self.listadeclientes: list[Cliente] = []

    def registrar_cliente(self, nombre: str, celular: str, correo: str, ciudad: str):
        cliente = Cliente(nombre, celular, correo, ciudad)
        self.listadeclientes.append(cliente)

    def obtener_id_cliente(self, nombre):
        lista_clientes_nr = []
        for cliente in self.listadeclientes:
            if cliente.nombre == nombre:
                lista_clientes_nr.append(cliente)
        print(f"El nombre del cliente es {nombre}\n\n")
        for cliente_repetido in lista_clientes_nr:
            print(
                f"La ciudad del cliente es {cliente_repetido.ciudad}\nEl correo del cliente es {cliente_repetido.correo}\nEl id del cliente es {cliente_repetido.id}\n\n")

    def obtener_cliente_por_id(self, id: int):
        cliente_retornar=None
        for cliente in self.listadeclientes:
            if cliente.id == id:
                cliente_retornar = cliente
                print(cliente_retornar)
        return cliente_retornar

    def eliminar_cliente_por_id(self, id):
        for cliente in self.listadeclientes:
            if cliente.id == id:
                print(f"Elimine a {cliente.nombre}.")
                self.listadeclientes.remove(cliente)

    def pasar_str_a_datetime(self, fecha):
        fecha_string = datetime.strptime(fecha, "%d/%m/%Y")
        return fecha_string

    def registrar_pedido(self, id_cliente: str, fecha: str):
        cliente = self.obtener_cliente_por_id(int(id_cliente))
        fecha_datetime = self.pasar_str_a_datetime(fecha)
        productos = Productos()
        productos.agregar_productos_a_lista()
        pedido = Pedido(cliente, fecha_datetime, productos)
        self.diccionariodepedidos[pedido.fecha] = pedido
    def guardar_info_clientes_excel(self):
        lista_info_clientes=self.listadeclientes
        book = Workbook()
        sheet = book.active
        sheet["A1"] = "Nombre"
        sheet["B1"] = "Id"
        sheet["C1"] = "Correo"
        sheet["D1"] = "Ciudad"
        sheet["E1"] = "Celular"
        contador = 1
        for cliente in lista_info_clientes:
            contador += 1
            sheet[f"A{contador}"] = cliente.nombre
            sheet[f"B{contador}"] = cliente.id
            sheet[f"C{contador}"] = cliente.correo
            sheet[f"D{contador}"] = cliente.ciudad
            sheet[f"E{contador}"] = cliente.celular

        diccionario_pedidos = self.diccionariodepedidos
        sheet2 = book.create_sheet("Pedidos")
        sheet2["A1"] = "Id_cliente"
        sheet2["B1"] = "Id_Pedido"
        sheet2["C1"] = "Productos"
        sheet2["D1"] = "Fecha"
        lista_id_pedidos = []
        lista_id_clientes = []
        lista_productos = []
        lista_productos_str = []
        lista_fechas = []
        for pedido in list(diccionario_pedidos.values()):
            lista_id_pedidos.append(pedido.id)
            lista_id_clientes.append(pedido.cliente.id)
            lista_productos.append(pedido.productos)
        for fecha in list(diccionario_pedidos.keys()):
            lista_fechas.append(str(fecha))
        for producto in lista_productos:
            str_lista = ""
            for diamante in producto.listadeDiamantes:
                str_lista += f"{str(diamante)}\n"
            lista_productos_str.append(str_lista)

        contador_id_cliente = 1
        contador_id_pedidos = 1
        contador_fechas = 1
        contador_productos = 1

        for id_cliente in lista_id_clientes:
            contador_id_cliente += 1
            sheet2[f"A{contador_id_cliente}"] = id_cliente
        for id_pedido in lista_id_pedidos:
            contador_id_pedidos += 1
            sheet2[f"B{contador_id_pedidos}"] = id_pedido
        for producto_str in lista_productos_str:
            print(producto_str)
            contador_productos += 1
            sheet2[f"C{contador_productos}"] = producto_str
        for fecha in lista_fechas:
            contador_fechas += 1
            sheet2[f"D{contador_fechas}"] = fecha
        book.save("prueba_escritura.xlsx")
        book.close()
















    def cargar_info_excel_clientes(self):
        df = pd.read_excel(r"prueba_escritura.xlsx", index_col="Id")
        diccionario = df.to_dict()
        print(diccionario)
        diccionario_id_nombre=diccionario["Nombre"]
        diccionario_id_correo = diccionario["Correo"]
        diccionario_id_ciudad = diccionario["Ciudad"]
        diccionario_id_celular= diccionario["Celular"]
        lista_de_nombres=list(diccionario_id_nombre.values())
        lista_de_id=list(diccionario_id_nombre.keys())
        lista_de_correo=list(diccionario_id_correo.values())
        lista_de_ciudad=list(diccionario_id_ciudad.values())
        lista_de_celular=list(diccionario_id_celular.values())
        for i in range (len(lista_de_nombres)):
            self.registrar_cliente(lista_de_nombres[i],lista_de_celular[i],lista_de_correo[i],lista_de_ciudad[i])












