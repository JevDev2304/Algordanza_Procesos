from modelo import *





INICIO = """
Bienvenido al programa para la gestión de clientes de Algordanza Colombia
*************************************************************************

Marque 0: Si desea cerrar el programa.
Marque 1: Si desea registrar cliente.
Marque 2: Si desea eliminar cliente por id.
Marque 3: Si desea obtener el id de un cliente por nombre.
Marque 4: Si desea registrar un pedido.
Marque 5: Si desea ver el historial de pedidos.
Marque 6: Si desea cancelar pedido.


*************************************************************************
"""
def ui():
    algordanza = Algordanza()
    algordanza.cargar_info_excel_clientes()
    opcion = 99
    while opcion != 0:
        print(INICIO)
        opcion = int(input(f" Elija una opción:"))
        if opcion == 1:
            nombre = str(input("Ingrese el nombre del cliente: "))
            celular = str(input("Ingrese el celular del cliente: "))
            correo = str(input("Ingrese el correo del cliente: "))
            ciudad = str(input("Ingrese la ciudad del cliente: "))
            algordanza.registrar_cliente(nombre, celular, correo, ciudad)
        elif opcion == 2:
            id = int(input("Cual es el id del cliente: "))
            algordanza.eliminar_cliente_por_id(id)
        elif opcion == 3:
            nombre = str(input("Cual es el nombre del cliente: "))
            algordanza.obtener_id_cliente(nombre)

        elif opcion == 4:
            id = int(input("Cual es el id del cliente: "))
            fecha = str(input("Cual es la fecha de registro del pedido: "))
            algordanza.registrar_pedido(id, fecha)
        elif opcion == 5:
            for pedido in algordanza.diccionariodepedidos.values():
                print(f"\n\nEl nombre del cliente es {pedido.cliente}")
                print(f"La fecha del pedido es {pedido.fecha}\n")
                for diamante in pedido.productos.listadeDiamantes:
                    print(f"->{diamante}\n")
    algordanza.guardar_info_clientes_excel()





