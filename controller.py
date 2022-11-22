import tkinter.messagebox

from UItkinter import UI
from modelo import Algordanza,Productos
import tkinter as tk

class Controller:
    def __init__(self,vista:UI,modelo:Algordanza):
        self.vista: UI = vista
        self.modelo: Algordanza= modelo
        self.info_temporal =[]
    def start(self):
        self.vista.create_principal_window(self)
    def create_window_user_register(self):
        self.vista.create_window_register(self)
    def getinforegister(self):
        try:
            cliente=self.vista.obtener_info_register()
            self.modelo.registrar_cliente(cliente[0],cliente[1],cliente[2],cliente[3])
        except Exception as error:
            tk.messagebox.showerror(str(error),str(error))
        else:
            tk.messagebox.showinfo("Se ingreso correctamente el cliente","No ocurrio ningún problema")
            self.modelo.guardar_info_clientes_excel()
            self.vista.volver_menu()
    def create_window_delete_user(self):
        self.vista.create_window_delete_user(self)
    def create_window_order(self):
        self.vista.create_window_order(self)
    def getinfodeleteuser(self):
        try:
            id=self.vista.obtener_info_delete_user()
            self.modelo.eliminar_cliente_por_id(int(id))
        except Exception as error:
            tk.messagebox.showerror(str(error),str(error))
        else:
            self.modelo.guardar_info_clientes_excel()
            tk.messagebox.showinfo("Se elimino correctamente el cliente", "No ocurrio ningún problema")
            self.vista.volver_menu_delete()
    def create_window_delete_order(self):
        self.vista.create_window_delete_order(self)

    def getinfodeleteorder(self):
        try:
            id=self.vista.get_info_delete_order()
            self.modelo.eliminar_pedido(int(id))
        except Exception as error:
            tk.messagebox.showerror(str(error),str(error) )
        else:
            self.modelo.guardar_info_clientes_excel()
            tk.messagebox.showinfo("Se elimino correctamente el pedido", "No ocurrio ningún problema")
            self.vista.volver_menu_delete_order()

    def getinfoorder(self):
        try:
            id =self.vista.obtener_info_order()[0]
            fecha= self.vista.obtener_info_order()[1]
            self.modelo.pasar_str_a_datetime(fecha)
            self.modelo.obtener_cliente_por_id(int(id))
        except Exception as error:
            tk.messagebox.showerror(str(error),str(error))
        else:
            self.vista.ventana_user_register.destroy()
            self.modelo.productos =self.modelo.crear_productos()
            self.info_temporal.append(id)
            self.info_temporal.append(fecha)
            self.vista.create_window_product(self)


    def diamante_corte_window(self):
        self.vista.create_window_entry_diamante_corte(self)
    def diamante_bruto_window(self):
        self.vista.create_window_entry_diamante_bruto(self)
    def get_info_diamante_corte(self):
        try:
            diamante_info=self.vista.obtener_info_diamante_corte()
            corte=diamante_info[0]
            tamano=diamante_info[1]
            grabado=diamante_info[2]
            origen=diamante_info[3]
            self.modelo.producto.agregar_diamante_con_corte_a_lista_productos(corte,tamano,grabado,origen)
        except Exception as error:
            tk.messagebox.showerror(str(error),str(error))
        else:
            print(self.modelo.producto.listadeDiamantes)
            self.vista.mostrar_menu_elegir_diamante()

    def get_info_diamante_bruto(self):
        try:
            diamante_info = self.vista.obtener_info_diamante_bruto()
            tamano = diamante_info[0]
            grabado = diamante_info[1]
            origen = diamante_info[2]
            self.modelo.producto.agregar_diamante_sin_corte_a_lista_productos(tamano,grabado,origen)
        except Exception as error:
            tk.messagebox.showerror(str(error), str(error))
        else:
            print(self.modelo.producto.listadeDiamantes)
            self.vista.mostrar_menu_elegir_diamante_bruto()

    def volver_eleccion_diamantes_principal(self):
        self.vista.volver_menu()
        self.modelo.productos=Productos()

    def registrar_pedido(self):
        try:
            if len(self.modelo.producto.listadeDiamantes) > 0:
                producto=self.modelo.producto
                id=self.info_temporal[0]
                fecha=self.info_temporal[1]
                self.modelo.registrar_pedido(id,fecha,producto)
            else:
                raise Exception("Ingresa al menos un diamante para poder ingresar el pedido")
        except Exception as error:
            tk.messagebox.showerror(str(error),str(error))
        else:
            self.modelo.guardar_info_clientes_excel()
            self.info_temporal=[]
            self.modelo.producto=Productos()
            self.vista.volver_menu()


















