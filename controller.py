import tkinter.messagebox

from UItkinter import UI
from modelo import Algordanza
import tkinter as tk
from tkinter import messagebox
class Controller:
    def __init__(self,vista:UI,modelo:Algordanza):
        self.vista: UI = vista
        self.modelo: Algordanza= modelo
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
            tk.messagebox.showinfo("Se elimino correctamente el cliente", "No ocurrio ningún problema")
            self.vista.volver_menu_delete()
    def getinfoorder(self):
        pass
        # try:
        #     id =self.vista.obtener_info_order()[0]
        #     fecha= self.vista.obtener_info_order()[1]
        #     fecha=self.modelo.pasar_str_a_datetime(fecha)







