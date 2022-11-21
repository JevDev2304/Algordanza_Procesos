import os
import time
import tkinter as tk
from tkinter import messagebox
from datetime import *
from os import *
from time import *



class UI:
    def __init__(self):
        self.principal_window = None
        self.logo=None

    def load_images(self):
        self.logo = tk.PhotoImage(file="imagenes/Algordanza_logo.png")
        self.logo = self.logo.subsample(2)
        self.logo_pequeno=self.logo.subsample(2)
        self.user_register= tk.PhotoImage(file="imagenes/Registrar Usuario.png")
        self.user_delete= tk.PhotoImage(file="imagenes/Eliminar Usuario.png")
        self.order_register= tk.PhotoImage(file="imagenes/Registrar Pedido.png")
        self.order_delete= tk.PhotoImage(file= "imagenes/Eliminar_Pedido.png")
        self.get_user_id= tk.PhotoImage(file= "imagenes/Obtener_id_Usuario.png")
        self.show_excel = tk.PhotoImage(file="imagenes/informacion_pedidos.png")

        self.register_name = tk.PhotoImage(file= "imagenes/Registrar_Nombre.png")
        self.register_cell = tk.PhotoImage(file="imagenes/Registrar_Celular.png")
        self.register_mail = tk.PhotoImage(file="imagenes/Registrar_Correo.png")
        self.register_city = tk.PhotoImage(file = "imagenes/Registrar_Ciudad.png")
        self.delete_user_id= tk.PhotoImage(file = "imagenes/Eliminar_id.png")

        self.menu=tk.PhotoImage(file="imagenes/volver_menu_principal.png")
        self.fecha= tk.PhotoImage(file="imagenes/Fecha.png")


    def create_principal_window(self,controller):
        self.principal_window = PrincipalWindow()
        self.load_images()
        self.principal_window.ventana.iconbitmap("imagenes/algordanza_imagen.ico")
        self.principal_window.ventana.title("Algordanza Colombia")
        self.principal_window.ventana.geometry("1080x720")
        self.principal_window.ventana.resizable(True, True)
        self.principal_window.ventana.title("Gestión de Pedidos de Algordanza Colombia ")
        self.principal_window.ventana.config(background="white")
        self.principal_window.ventana.maxsize(1280, 720)

        self.principal_window.title_frame = tk.Frame(self.principal_window.ventana)
        self.principal_window.title_frame.config(background="white")
        self.principal_window.frame_empty_1 = tk.Label(self.principal_window.title_frame,text="                            ", background="white")
        self.principal_window.frame_empty_2 = tk.Label(self.principal_window.title_frame, text= "                          ", background="white")

        self.principal_window.title_frame.grid(row=0, column=0)
        self.principal_window.frame_empty_1.grid(row=0, column=0)
        self.principal_window.frame_empty_2.grid(row=0, column= 2)

        self.principal_window.buttons_frame = tk.Frame(self.principal_window.ventana)
        self.principal_window.buttons_frame.config(background="white", borderwidth=0)
        self.principal_window.buttons_frame.grid(row=1, column=0)
        self.principal_window.frame_empty_3 = tk.Label(self.principal_window.buttons_frame,
                                                       text="                            ", background="white")
        self.principal_window.frame_empty_4 = tk.Label(self.principal_window.buttons_frame,
                                                       text="                          ", background="white")
        self.principal_window.frame_empty_3.grid(row=0, column=0)
        self.principal_window.frame_empty_4.grid(row=0, column=4)

        self.principal_window.title = tk.Label(self.principal_window.title_frame)
        self.principal_window.title.config(font=("Candara", 48), fg="white", image=self.logo,background="white")
        self.principal_window.title.grid(row=0, column=1)

        self.principal_window.button_Register = tk.Button(self.principal_window.buttons_frame, borderwidth=0, image=self.user_register, background="white",command=controller.create_window_user_register)
        self.principal_window.button_Register.grid(row=0,column=1)
        self.principal_window.button_Delete = tk.Button(self.principal_window.buttons_frame, borderwidth=0, image=self.user_delete, background="white", command=controller.create_window_delete_user)
        self.principal_window.button_Delete.grid(row =0, column=2)

        self.principal_window.button_Register_order = tk.Button(self.principal_window.buttons_frame, borderwidth=0,image=self.order_register, background="white", command=controller.create_window_order)
        self.principal_window.button_Register_order.grid(row=0, column=3)

        self.principal_window.button_Delete_order = tk.Button(self.principal_window.buttons_frame,borderwidth=0,image= self.order_delete, background="white")
        self.principal_window.button_Delete_order.grid(row=1,column=1)
        self.principal_window.button_get_id_user = tk.Button(self.principal_window.buttons_frame, borderwidth=0, image=self.get_user_id, background="white")
        self.principal_window.button_get_id_user.grid(row=1, column=2)
        self.principal_window.button_excel_info = tk.Button(self.principal_window.buttons_frame, borderwidth=0, image=self.show_excel, background="white",command=self.visualizacion_excel_pdf )
        self.principal_window.button_excel_info.grid(row=1, column=3)




        self.principal_window.ventana.mainloop()

    def create_window_register(self, controller):
        self.principal_window.ventana.withdraw()
        self.ventana_user_register = tk.Toplevel()
        self.ventana_user_register.iconbitmap("imagenes/algordanza_imagen.ico")
        self.ventana_user_register.title("Algordanza Colombia")
        self.ventana_user_register.geometry("1080x900")
        self.ventana_user_register.resizable(True, True)
        self.ventana_user_register.title("Registrar Cliente ")
        self.ventana_user_register.config(background="white")
        self.ventana_user_register.maxsize(1080, 900)
        self.ventana_user_register.state("zoomed")

        self.ventana_user_register_title_frame = tk.Frame(self.ventana_user_register)
        self.ventana_user_register_title_frame.config(background="white")
        self.ventana_user_register_frame_empty_1 = tk.Label(self.ventana_user_register_title_frame,
                                                            text="                                  ", background="white")
        self.ventana_user_register_frame_empty_2 = tk.Label(self.ventana_user_register_title_frame,
                                                            text="                                              ", background="white")

        self.ventana_user_register_title_frame.grid(row=0, column=0)
        self.ventana_user_register_frame_empty_1.grid(row=0, column=0)
        self.ventana_user_register_frame_empty_2.grid(row=0, column=2)

        self.ventana_user_register_buttons_frame = tk.Frame(self.ventana_user_register)
        self.ventana_user_register_buttons_frame.config(background="white", borderwidth=0)
        self.ventana_user_register_buttons_frame.grid(row=1, column=0)
        self.ventana_user_register_frame_empty_3 = tk.Label(self.ventana_user_register_buttons_frame,
                                                            text="                           ", background="white")
        self.ventana_user_register_frame_empty_4 = tk.Label(self.ventana_user_register_buttons_frame,
                                                            text="                                                       ", background="white")
        self.ventana_user_register_frame_empty_3.grid(row=0, column=0)
        self.ventana_user_register_frame_empty_4.grid(row=0, column=3)

        self.ventana_user_register_title= tk.Label(self.ventana_user_register_title_frame)
        self.ventana_user_register_title.config(font=("Candara", 48), fg="white", image=self.logo_pequeno, background="white")
        self.ventana_user_register_title.grid(row=0, column=1)

        self.label_name = tk.Label(self.ventana_user_register_buttons_frame,image=self.register_name,borderwidth=0, background="white")
        self.label_name.grid(row=0,column=1)
        self.entry_name = tk.Entry(self.ventana_user_register_buttons_frame, font=("Calibri bold", 25), fg="white", background="#023671",justify="center",bd=4, width=35, borderwidth=0,)
        self.entry_name.grid(row=0,column=2)

        self.label_cel = tk.Label(self.ventana_user_register_buttons_frame, image=self.register_cell, borderwidth=0,
                                   background="white")
        self.label_cel.grid(row=1, column=1)
        self.entry_cel = tk.Entry(self.ventana_user_register_buttons_frame, font=("Calibri bold", 25), fg="white",
                                   background="#023671", justify="center", bd=4, width=35, borderwidth=0, )
        self.entry_cel.grid(row=1, column=2)

        self.label_correo = tk.Label(self.ventana_user_register_buttons_frame, image=self.register_mail, borderwidth=0,
                                   background="white")
        self.label_correo.grid(row=2, column=1)
        self.entry_correo = tk.Entry(self.ventana_user_register_buttons_frame, font=("Calibri bold", 25), fg="white",
                                   background="#023671", justify="center", bd=4, width=35, borderwidth=0, )
        self.entry_correo.grid(row=2, column=2)

        self.label_ciudad = tk.Label(self.ventana_user_register_buttons_frame, image=self.register_city, borderwidth=0,
                                     background="white")
        self.label_ciudad.grid(row=3, column=1)
        self.entry_ciudad = tk.Entry(self.ventana_user_register_buttons_frame, font=("Calibri bold", 25), fg="white",
                                     background="#023671", justify="center", bd=4, width=35, borderwidth=0, )
        self.entry_ciudad.grid(row=3, column=2)

        self.button_back = tk.Button(self.ventana_user_register_buttons_frame, image=self.menu, borderwidth=0,
                                     background="white",command=self.volver_menu)
        self.button_final_register = tk.Button(self.ventana_user_register_buttons_frame, image=self.user_register, borderwidth=0,
                                               background="white", command=controller.getinforegister)
        self.button_back.grid(row=4, column=1)
        self.button_final_register.grid(row = 4, column = 2)

        self.ventana_user_register.mainloop()

    def create_window_delete_user(self,controller):
        self.principal_window.ventana.withdraw()
        self.ventana_user_delete_register = tk.Toplevel()
        self.ventana_user_delete_register.iconbitmap("imagenes/algordanza_imagen.ico")
        self.ventana_user_delete_register.title("Algordanza Colombia")
        self.ventana_user_delete_register.geometry("1080x720")
        self.ventana_user_delete_register.resizable(True, True)
        self.ventana_user_delete_register.title("Eliminar Cliente ")
        self.ventana_user_delete_register.config(background="white")
        self.ventana_user_delete_register.maxsize(1080, 900)
        self.ventana_user_delete_register.state("zoomed")

        self.ventana_user_delete_register_title_frame = tk.Frame(self.ventana_user_delete_register)
        self.ventana_user_delete_register_title_frame.config(background="white")
        self.ventana_user_delete_register_frame_empty_1 = tk.Label(self.ventana_user_delete_register_title_frame,
                                                            text=" ",
                                                            background="white")
        self.ventana_user_delete_register_frame_empty_2 = tk.Label(self.ventana_user_delete_register_title_frame,
                                                            text="                                                                                           ",
                                                            background="white")

        self.ventana_user_delete_register_title_frame.grid(row=0, column=0)
        self.ventana_user_delete_register_frame_empty_1.grid(row=0, column=0)
        self.ventana_user_delete_register_frame_empty_2.grid(row=0, column=2)

        self.ventana_user_delete_register_buttons_frame = tk.Frame(self.ventana_user_delete_register)
        self.ventana_user_delete_register_buttons_frame.config(background="white", borderwidth=0)
        self.ventana_user_delete_register_buttons_frame.grid(row=1, column=0)
        self.ventana_user_delete_register_frame_empty_3 = tk.Label(self.ventana_user_delete_register_buttons_frame,
                                                            text="", background="white")
        self.ventana_user_delete_register_frame_empty_4 = tk.Label(self.ventana_user_delete_register_buttons_frame,
                                                            text="                                                                                                                                                        ",
                                                            background="white")
        self.ventana_user_delete_register_frame_empty_3.grid(row=0, column=0)
        self.ventana_user_delete_register_frame_empty_4.grid(row=0, column=3)

        self.ventana_user_delete_register_title = tk.Label(self.ventana_user_delete_register_title_frame)
        self.ventana_user_delete_register_title.config(font=("Candara", 48), fg="white", image=self.logo,
                                                background="white")
        self.ventana_user_delete_register_title.grid(row=0, column=1)
        self.label_id = tk.Label(self.ventana_user_delete_register_buttons_frame, image= self.delete_user_id, background="white")
        self.label_id.grid(row=1, column=0)
        self.entry_id = tk.Entry(self.ventana_user_delete_register_buttons_frame, font=("Calibri bold", 25), fg="white",
                                     background="#023671", justify="center", bd=4, width=35, borderwidth=0, )
        self.entry_id.grid(row=1,column=1)

        self.button_back_delete = tk.Button(self.ventana_user_delete_register_buttons_frame, image=self.menu, borderwidth=0,
                                     background="white", command=self.volver_menu_delete)
        self.button_final_delete_register = tk.Button(self.ventana_user_delete_register_buttons_frame, image=self.user_delete,
                                               borderwidth=0, command=controller.getinfodeleteuser,
                                               background="white")
        self.button_back_delete.grid(row=4, column=0)
        self.button_final_delete_register.grid(row=4, column=1)

    def obtener_info_register(self):
        try:
            nombre= self.entry_name.get()
            nombre_sin_espacios=nombre.replace(" ","")
            cel = self.entry_cel.get()
            correo= self.entry_correo.get()
            ciudad = self.entry_ciudad.get()
            test_nombre_sin_espacios= nombre_sin_espacios.isalpha()
            test_cel=cel.isdigit()
            test_correo=("@" in correo)
            test_ciudad=ciudad.isalpha()
            if test_nombre_sin_espacios is False:
                raise Exception("No ingresaste bien el nombre")
            if test_cel is False:
                raise Exception("No ingresate bien el celular")
            if test_correo is False:
                raise Exception("No ingresaste bien el correo")
            if test_ciudad is False:
                raise Exception("No ingresaste bien la ciudad")
        except Exception as error:
            tk.messagebox.showinfo(str(error),str(error))
        else:
            return [nombre, cel, correo, ciudad]
    def obtener_info_delete_user(self):
        id=self.entry_id.get()
        try:
            if id.isdigit() is False:
                raise Exception("Id debe ser un número")
        except Exception as error:
            tk.messagebox.showinfo(str(error),str(error))
        else:
            return id






    def volver_menu(self):
        self.ventana_user_register.destroy()
        self.principal_window.ventana.iconify()
        self.principal_window.ventana.state("zoomed")

    def volver_menu_delete(self):
        self.ventana_user_delete_register.destroy()
        self.principal_window.ventana.iconify()
        self.principal_window.ventana.state("zoomed")

    def create_window_order(self, controller):
        self.principal_window.ventana.withdraw()
        self.ventana_user_register = tk.Toplevel()
        self.ventana_user_register.iconbitmap("imagenes/algordanza_imagen.ico")
        self.ventana_user_register.title("Algordanza Colombia")
        self.ventana_user_register.geometry("1080x900")
        self.ventana_user_register.resizable(True, True)
        self.ventana_user_register.title("Registrar Pedido")
        self.ventana_user_register.config(background="white")
        self.ventana_user_register.maxsize(1080, 900)
        self.ventana_user_register.state("zoomed")

        self.ventana_user_register_title_frame = tk.Frame(self.ventana_user_register)
        self.ventana_user_register_title_frame.config(background="white")
        self.ventana_user_register_frame_empty_1 = tk.Label(self.ventana_user_register_title_frame,
                                                            text="                                  ", background="white")
        self.ventana_user_register_frame_empty_2 = tk.Label(self.ventana_user_register_title_frame,
                                                            text="                                              ", background="white")

        self.ventana_user_register_title_frame.grid(row=0, column=0)
        self.ventana_user_register_frame_empty_1.grid(row=0, column=0)
        self.ventana_user_register_frame_empty_2.grid(row=0, column=2)

        self.ventana_user_register_buttons_frame = tk.Frame(self.ventana_user_register)
        self.ventana_user_register_buttons_frame.config(background="white", borderwidth=0)
        self.ventana_user_register_buttons_frame.grid(row=1, column=0)
        self.ventana_user_register_frame_empty_3 = tk.Label(self.ventana_user_register_buttons_frame,
                                                            text="                           ", background="white")
        self.ventana_user_register_frame_empty_4 = tk.Label(self.ventana_user_register_buttons_frame,
                                                            text="                                                       ", background="white")
        self.ventana_user_register_frame_empty_3.grid(row=0, column=0)
        self.ventana_user_register_frame_empty_4.grid(row=0, column=3)

        self.ventana_user_register_title= tk.Label(self.ventana_user_register_title_frame)
        self.ventana_user_register_title.config(font=("Candara", 48), fg="white", image=self.logo, background="white")
        self.ventana_user_register_title.grid(row=0, column=1)

        self.label_id = tk.Label(self.ventana_user_register_buttons_frame,image=self.delete_user_id,borderwidth=0, background="white")
        self.label_id.grid(row=0,column=1)
        self.entry_id = tk.Entry(self.ventana_user_register_buttons_frame, font=("Calibri bold", 25), fg="white", background="#023671",justify="center",bd=4, width=35, borderwidth=0,)
        self.entry_id.grid(row=0,column=2)

        self.label_fecha = tk.Label(self.ventana_user_register_buttons_frame, image=self.fecha, borderwidth=0,
                                   background="white")
        self.label_fecha.grid(row=1, column=1)
        self.entry_fecha = tk.Entry(self.ventana_user_register_buttons_frame, font=("Calibri bold", 25), fg="white",
                                   background="#023671", justify="center", bd=4, width=35, borderwidth=0, )
        self.entry_fecha.grid(row=1, column=2)


        self.button_back = tk.Button(self.ventana_user_register_buttons_frame, image=self.menu, borderwidth=0,
                                     background="white",command=self.volver_menu)
        self.button_final_order = tk.Button(self.ventana_user_register_buttons_frame, image=self.order_register, borderwidth=0,
                                               background="white", command=controller.getinfoorder)
        self.button_back.grid(row=4, column=1)
        self.button_final_order.grid(row = 4, column = 2)

        self.ventana_user_register.mainloop()

    def obtener_info_order(self):
        try:
            id=self.entry_id.get()
            fecha=self.entry_fecha.get()
            if id.isdigit() is False:
                raise Exception("El ID es un número")
            if len(fecha)<10:
                raise Exception("Fecha mal ingresada")
        except Exception as error:
            tk.messagebox.showinfo(str(error),str(error))
        else:
            return [id, fecha]

    def visualizacion_excel_pdf(self):
        self.principal_window.ventana.withdraw()
        tk.messagebox.showwarning("No modificar el excel." ,"1) Para que el Programa funcione sin problemas, NO MODIFICAR EL ARCHIVO.\n\n 2) CERRAR EL ARCHIVO cuando hayas terminado la revisión.")

        os.startfile("Base_Datos.xlsx")

        self.principal_window.ventana.iconify()
        self.principal_window.ventana.state("zoomed")














class PrincipalWindow:
    def __init__(self):
        self.ventana_user_register = None
        self.ventana = tk.Tk()
        self.title_frame=None
        self.frame_empty_1=None
        self.frame_empty_2=None
        self.frame_empty_3=None
        self.frame_empty_4=None
        self.buttons_frame=None
        self.title= None
        self.button_Register=None
        self.button_Delete=None
        self.button_Register_order=None
        self.button_Delete_order = None
        self.button_get_id_user = None
        self.button_excel_info = None

    def create_window_register(self,controller):
        self.ventana.withdraw()
        self.ventana_user_register= tk.Toplevel()
        self.ventana_user_register.iconbitmap("imagenes/algordanza_imagen.ico")
        self.ventana_user_register.title("Algordanza Colombia")
        self.ventana_user_register.geometry("1080x720")
        self.ventana_user_register.resizable(True, True)
        self.ventana_user_register.title("Registrar Cliente ")
        self.ventana_user_register.config(background="white")
        self.ventana_user_register.maxsize(1280, 720)

        self.ventana_user_register_title_frame = tk.Frame(self.ventana_user_register)
        self.ventana_user_register_title_frame.config(background="white")
        self.ventana_user_register_frame_empty_1 = tk.Label(self.ventana_user_register,
                                                       text="                            ", background="white")
        self.ventana_user_register_frame_empty_2 = tk.Label(self.ventana_user_register_title_frame,
                                                       text="                          ", background="white")

        self.ventana_user_register_title_frame.grid(row=0, column=0)
        self.ventana_user_register_frame_empty_1.grid(row=0, column=0)
        self.ventana_user_register_frame_empty_2.grid(row=0, column=2)

        self.ventana_user_register_buttons_frame = tk.Frame(self.ventana_user_register)
        self.ventana_user_register_buttons_frame.config(background="white", borderwidth=0)
        self.ventana_user_register_buttons_frame.grid(row=1, column=0)
        self.ventana_user_register_frame_empty_3 = tk.Label(self.ventana_user_register_buttons_frame,
                                                       text="                            ", background="white")
        self.ventana_user_register.frame_empty_4 = tk.Label(self.ventana_user_register_buttons_frame,
                                                       text="                          ", background="white")
        self.ventana_user_register_frame_empty_3.grid(row=0, column=0)
        self.ventana_user_register.frame_empty_4.grid(row=0, column=4)


