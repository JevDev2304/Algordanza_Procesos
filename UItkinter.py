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
        self.logo= None

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

        self.register_name_small = self.register_name.subsample(2)
        self.register_cell_small = self.register_cell.subsample(2)
        self.register_mail_small = self.register_mail.subsample(2)
        self.register_city_small = self.register_city.subsample(2)


        self.menu=tk.PhotoImage(file="imagenes/volver_menu_principal.png")
        self.fecha= tk.PhotoImage(file="imagenes/Fecha.png")
        self.diamante_bruto= tk.PhotoImage(file="imagenes/Diamante_Bruto.png")
        self.diamante_corte= tk.PhotoImage(file= "imagenes/Diamante_corte.png")
        self.carrito_productos= tk.PhotoImage(file ="imagenes/Carrito_Productos.png")

        self.ingresar_corte= tk.PhotoImage(file="imagenes/ingresar_corte.png")
        self.ingresar_corte_small=self.ingresar_corte.subsample(2)

        self.quilates= tk.PhotoImage(file="imagenes/Quilates.png")
        self.quilates_small= self.quilates.subsample(2)

        self.grabado= tk.PhotoImage(file= "imagenes/Grabado.png")
        self.grabado_small = self.grabado.subsample(2)
        self.origen= tk.PhotoImage(file="imagenes/origen.png")
        self.origen_small= self.origen.subsample(2)
        self.add_diamond= tk.PhotoImage(file="imagenes/Agregar_diamante.png")
        self.pedido_id = tk.PhotoImage(file= "imagenes/Id_pedido.png")



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


        self.principal_window.button_Register_order = tk.Button(self.principal_window.buttons_frame, borderwidth=0,image=self.order_register, background="white", command=controller.create_window_order)
        self.principal_window.button_Register_order.grid(row=0, column=2)
        self.principal_window.button_Register_order.grid(row=0, column=2)

        self.principal_window.button_Delete_order = tk.Button(self.principal_window.buttons_frame,borderwidth=0,image= self.order_delete, background="white", command=controller.create_window_delete_order)
        self.principal_window.button_excel_info = tk.Button(self.principal_window.buttons_frame, borderwidth=0, image=self.show_excel, background="white",command=self.visualizacion_excel_pdf )
        self.principal_window.button_excel_info.grid(row=0, column=3)




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

        self.label_name = tk.Label(self.ventana_user_register_buttons_frame,image=self.register_name_small,borderwidth=0, background="white")
        self.label_name.grid(row=0,column=1)
        self.entry_name = tk.Entry(self.ventana_user_register_buttons_frame, font=("Calibri bold", 25), fg="white", background="#023671",justify="center",bd=4, width=35, borderwidth=0,)
        self.entry_name.grid(row=0,column=2)

        self.label_cel = tk.Label(self.ventana_user_register_buttons_frame, image=self.register_cell_small, borderwidth=0,
                                   background="white")
        self.label_cel.grid(row=1, column=1)
        self.entry_cel = tk.Entry(self.ventana_user_register_buttons_frame, font=("Calibri bold", 25), fg="white",
                                   background="#023671", justify="center", bd=4, width=35, borderwidth=0, )
        self.entry_cel.grid(row=1, column=2)

        self.label_correo = tk.Label(self.ventana_user_register_buttons_frame, image=self.register_mail_small, borderwidth=0,
                                   background="white")
        self.label_correo.grid(row=2, column=1)
        self.entry_correo = tk.Entry(self.ventana_user_register_buttons_frame, font=("Calibri bold", 25), fg="white",
                                   background="#023671", justify="center", bd=4, width=35, borderwidth=0, )
        self.entry_correo.grid(row=2, column=2)

        self.label_ciudad = tk.Label(self.ventana_user_register_buttons_frame, image=self.register_city_small, borderwidth=0,
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
        self.ventana_user_delete_register.mainloop()

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
    def volver_menu_diamante_corte(self):
        self.ventana_diamond_ashes.destroy()
        self.principal_window.ventana_pr.iconify()
        self.principal_window.ventana.state("zoomed")


    def volver_menu_delete(self):
        self.ventana_user_delete_register.destroy()
        self.principal_window.ventana.iconify()
        self.principal_window.ventana.state("zoomed")
    def volver_menu_delete_order(self):
        self.ventana_order_delete_register.destroy()
        self.principal_window.ventana.iconify()
        self.principal_window.ventana.state("zoomed")


    def create_window_order(self, controller):
        self.principal_window.ventana.withdraw()
        self.ventana_user_register = tk.Toplevel()
        self.ventana_user_register.iconbitmap("imagenes/algordanza_imagen.ico")
        self.ventana_user_register.title("Algordanza Colombia")
        self.ventana_user_register.geometry("1080x900")
        self.ventana_user_register.resizable(True, True)
        self.ventana_user_register.title("Productos")
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
        tk.messagebox.showwarning("Visualizacion Excel","Puedes modificar el archivo, pero no sera guardado en el programa.\n\nLa función esta hecha para poder visualizar id e información general.\n\nIMPORTANTE:Cerrar excel antes de seguir usando el programa.")

        os.startfile("Editable.xlsx")

        self.principal_window.ventana.iconify()
        self.principal_window.ventana.state("zoomed")

    def create_window_product(self, controller):
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
                                                            text="                                              ", background="white")
        self.ventana_user_register_frame_empty_2 = tk.Label(self.ventana_user_register_title_frame,
                                                            text="                                              ", background="white")

        self.ventana_user_register_title_frame.grid(row=0, column=0)
        self.ventana_user_register_frame_empty_1.grid(row=0, column=0)
        self.ventana_user_register_frame_empty_2.grid(row=0, column=2)

        self.ventana_user_register_buttons_frame = tk.Frame(self.ventana_user_register)
        self.ventana_user_register_buttons_frame.config(background="white", borderwidth=0)
        self.ventana_user_register_buttons_frame.grid(row=1, column=0)
        self.ventana_user_register_frame_empty_3 = tk.Label(self.ventana_user_register_buttons_frame,
                                                            text="                                                       ", background="white")
        self.ventana_user_register_frame_empty_4 = tk.Label(self.ventana_user_register_buttons_frame,
                                                            text="                                                       ", background="white")
        self.ventana_user_register_frame_empty_3.grid(row=0, column=0)
        self.ventana_user_register_frame_empty_4.grid(row=0, column=3)

        self.ventana_user_register_title= tk.Label(self.ventana_user_register_title_frame)
        self.ventana_user_register_title.config(font=("Candara", 48), fg="white", image=self.logo, background="white")
        self.ventana_user_register_title.grid(row=0, column=1)

        self.button_diamante_bruto = tk.Button(self.ventana_user_register_buttons_frame,image=self.diamante_bruto,borderwidth=0, background="white", command=controller.diamante_bruto_window)
        self.button_diamante_bruto.grid(row=0,column=1)

        self.button_diamante_corte = tk.Button(self.ventana_user_register_buttons_frame, image=self.diamante_corte, borderwidth=0,
                                   background="white",command=controller.diamante_corte_window)
        self.button_diamante_corte.grid(row=0, column=2)

        self.button_back = tk.Button(self.ventana_user_register_buttons_frame, image=self.menu, borderwidth=0,
                                     background="white",command=controller.volver_eleccion_diamantes_principal)
        self.button_final_product = tk.Button(self.ventana_user_register_buttons_frame, image=self.carrito_productos, borderwidth=0,
                                               background="white", command=controller.registrar_pedido)
        self.button_back.grid(row=1, column=1)
        self.button_final_product.grid(row = 1, column = 2)

        self.ventana_user_register.mainloop()

    def create_window_entry_diamante_corte(self,controller):
        self.ventana_user_register.withdraw()

        self.ventana_diamond_ashes= tk.Toplevel()
        self.ventana_diamond_ashes.iconbitmap("imagenes/algordanza_imagen.ico")
        self.ventana_diamond_ashes.title("Algordanza Colombia")
        self.ventana_diamond_ashes.geometry("1080x900")
        self.ventana_diamond_ashes.resizable(True, True)
        self.ventana_diamond_ashes.title("Diamante Corte")
        self.ventana_diamond_ashes.config(background="white")
        self.ventana_diamond_ashes.maxsize(1080, 900)
        self.ventana_diamond_ashes.state("zoomed")

        self.ventana_diamond_ashes_title_frame = tk.Frame(self.ventana_diamond_ashes)
        self.ventana_diamond_ashes_title_frame.config(background="white")
        self.ventana_diamond_ashes_frame_empty_1 = tk.Label(self.ventana_diamond_ashes_title_frame,
                                                            text="                                              ",
                                                            background="white")
        self.ventana_diamond_ashes_register_frame_empty_2 = tk.Label(self.ventana_diamond_ashes_title_frame,
                                                            text="                                              ",
                                                            background="white")

        self.ventana_diamond_ashes_title_frame.grid(row=0, column=0)
        self.ventana_diamond_ashes_frame_empty_1.grid(row=0, column=0)
        self.ventana_diamond_ashes_register_frame_empty_2.grid(row=0, column=2)

        self.ventana_diamond_ashes_buttons_frame = tk.Frame(self.ventana_diamond_ashes)
        self.ventana_diamond_ashes_buttons_frame.config(background="white", borderwidth=0)
        self.ventana_diamond_ashes_buttons_frame.grid(row=1, column=0)
        self.ventana_diamond_ashes_frame_empty_3 = tk.Label(self.ventana_diamond_ashes_buttons_frame,
                                                            text="    ",
                                                            background="white")
        self.ventana_diamond_ashes_frame_empty_4 = tk.Label(self.ventana_diamond_ashes_buttons_frame,
                                                            text="                                                       ",
                                                            background="white")
        self.ventana_diamond_ashes_frame_empty_3.grid(row=0, column=0)
        self.ventana_diamond_ashes_frame_empty_4.grid(row=0, column=3)

        self.ventana_diamond_ashes_register_title = tk.Label(self.ventana_diamond_ashes_title_frame)
        self.ventana_diamond_ashes_register_title.config(font=("Candara", 48), fg="white", image=self.logo_pequeno, background="white")
        self.ventana_diamond_ashes_register_title.grid(row=0, column=1)

        self.label_corte = tk.Label(self.ventana_diamond_ashes_buttons_frame, image=self.ingresar_corte_small,
                                               borderwidth=0, background="white", )
        self.label_corte.grid(row=0, column=1)
        self.entry_corte= tk.Entry(self.ventana_diamond_ashes_buttons_frame,font=("Calibri bold", 25), fg="white",
                                   background="#023671", justify="center", bd=4, width=35, borderwidth=0 )
        self.entry_corte.grid(row=0,column=2)
        self.label_tamano= tk.Label(self.ventana_diamond_ashes_buttons_frame, image=self.quilates_small,
                                               borderwidth=0, background="white", )

        self.entry_tamano=tk.Entry(self.ventana_diamond_ashes_buttons_frame,font=("Calibri bold", 25), fg="white",
                                   background="#023671", justify="center", bd=4, width=35, borderwidth=0 )
        self.label_tamano.grid(row=1, column=1)
        self.entry_tamano.grid(row=1,column=2)
        self.label_grabado=tk.Label(self.ventana_diamond_ashes_buttons_frame, image=self.grabado_small,
                                               borderwidth=0, background="white" )

        self.entry_grabado=tk.Entry(self.ventana_diamond_ashes_buttons_frame,font=("Calibri bold", 25), fg="white",
                                   background="#023671", justify="center", bd=4, width=35, borderwidth=0 )
        self.label_grabado.grid(row=2,column=1)
        self.entry_grabado.grid(row=2, column=2)
        self.label_origen=tk.Label(self.ventana_diamond_ashes_buttons_frame, image=self.origen_small, borderwidth=0, background="white")
        self.entry_origen=tk.Entry(self.ventana_diamond_ashes_buttons_frame,font=("Calibri bold", 25), fg="white",
                                   background="#023671", justify="center", bd=4, width=35, borderwidth=0 )
        self.label_origen.grid(row=3,column=1)
        self.entry_origen.grid(row=3,column=2)





        self.button_back_diamond_ashes = tk.Button(self.ventana_diamond_ashes_buttons_frame, image=self.menu, borderwidth=0,
                                     background="white", command=self.mostrar_menu_diamante_corte)
        self.button_add_diamond = tk.Button(self.ventana_diamond_ashes_buttons_frame, image=self.add_diamond,
                                              borderwidth=0,
                                              background="white", command=controller.get_info_diamante_corte)
        self.button_back_diamond_ashes.grid(row=4, column=1)
        self.button_add_diamond.grid(row=4, column=2)

        self.ventana_diamond_ashes.mainloop()


    def create_window_entry_diamante_bruto(self,controller):
        self.ventana_user_register.withdraw()

        self.ventana_raw_diamond= tk.Toplevel()
        self.ventana_raw_diamond.iconbitmap("imagenes/algordanza_imagen.ico")
        self.ventana_raw_diamond.title("Algordanza Colombia")
        self.ventana_raw_diamond.geometry("1080x900")
        self.ventana_raw_diamond.resizable(True, True)
        self.ventana_raw_diamond.title("Diamante Corte")
        self.ventana_raw_diamond.config(background="white")
        self.ventana_raw_diamond.maxsize(1080, 900)
        self.ventana_raw_diamond.state("zoomed")

        self.ventana_raw_diamond_title_frame = tk.Frame(self.ventana_raw_diamond)
        self.ventana_raw_diamond_title_frame.config(background="white")
        self.ventana_raw_diamond_frame_empty_1 = tk.Label(self.ventana_raw_diamond_title_frame,
                                                            text="                                              ",
                                                            background="white")
        self.ventana_raw_diamond_frame_empty_2 = tk.Label(self.ventana_raw_diamond_title_frame,
                                                            text="                                              ",
                                                            background="white")

        self.ventana_raw_diamond_title_frame.grid(row=0, column=0)
        self.ventana_raw_diamond_frame_empty_1.grid(row=0, column=0)
        self.ventana_raw_diamond_frame_empty_2.grid(row=0, column=2)

        self.ventana_raw_diamond_buttons_frame = tk.Frame(self.ventana_raw_diamond)
        self.ventana_raw_diamond_buttons_frame.config(background="white", borderwidth=0)
        self.ventana_raw_diamond_buttons_frame.grid(row=1, column=0)
        self.ventana_raw_diamonds_frame_empty_3 = tk.Label(self.ventana_raw_diamond_buttons_frame,
                                                            text="    ",
                                                            background="white")
        self.ventana_raw_diamond_empty_4 = tk.Label(self.ventana_raw_diamond_buttons_frame,
                                                            text="                                                       ",
                                                            background="white")
        self.ventana_raw_diamonds_frame_empty_3.grid(row=0, column=0)
        self.ventana_raw_diamond_empty_4.grid(row=0, column=3)

        self.ventana_raw_diamond_title = tk.Label(self.ventana_raw_diamond_title_frame)
        self.ventana_raw_diamond_title.config(font=("Candara", 48), fg="white", image=self.logo_pequeno, background="white")
        self.ventana_raw_diamond_title.grid(row=0, column=1)


        self.label_raw_tamano= tk.Label(self.ventana_raw_diamond_buttons_frame, image=self.quilates_small,
                                               borderwidth=0, background="white", )

        self.entry_tamano_raw=tk.Entry(self.ventana_raw_diamond_buttons_frame,font=("Calibri bold", 25), fg="white",
                                   background="#023671", justify="center", bd=4, width=35, borderwidth=0 )
        self.label_raw_tamano.grid(row=1, column=1)
        self.entry_tamano_raw.grid(row=1,column=2)

        self.label_grabado_raw=tk.Label(self.ventana_raw_diamond_buttons_frame, image=self.grabado_small,
                                               borderwidth=0, background="white" )

        self.entry_grabado_raw=tk.Entry(self.ventana_raw_diamond_buttons_frame,font=("Calibri bold", 25), fg="white",
                                   background="#023671", justify="center", bd=4, width=35, borderwidth=0 )
        self.label_grabado_raw.grid(row=2,column=1)
        self.entry_grabado_raw.grid(row=2, column=2)
        self.label_origen_raw=tk.Label(self.ventana_raw_diamond_buttons_frame, image=self.origen_small, borderwidth=0, background="white")
        self.entry_origen_raw =tk.Entry(self.ventana_raw_diamond_buttons_frame,font=("Calibri bold", 25), fg="white",
                                   background="#023671", justify="center", bd=4, width=35, borderwidth=0 )
        self.label_origen_raw.grid(row=3,column=1)
        self.entry_origen_raw.grid(row=3,column=2)





        self.button_back_raw_diamond = tk.Button(self.ventana_raw_diamond_buttons_frame, image=self.menu, borderwidth=0,
                                     background="white", command=self.mostrar_menu_elegir_diamante_bruto)
        self.button_add_diamond_raw = tk.Button(self.ventana_raw_diamond_buttons_frame, image=self.add_diamond,
                                              borderwidth=0,
                                              background="white", command=controller.get_info_diamante_bruto)
        self.button_back_raw_diamond.grid(row=4, column=1)
        self.button_add_diamond_raw.grid(row=4, column=2)

        self.ventana_raw_diamond.mainloop()

    def obtener_info_diamante_corte(self):
        try:
            corte=self.entry_corte.get()
            tamano=self.entry_tamano.get()
            grabado=self.entry_grabado.get()
            origen=self.entry_origen.get()
            test_corte=corte.isalpha()
            test_tamano=float(tamano)
            test_grabado=((grabado.lower()=="no") or (grabado.lower()=="si"))
            test_origen=origen.isalpha()
            if test_corte is False:
                raise Exception ("Ingresa bien el corte")
            if (test_tamano<0) or (test_tamano>1):
                raise Exception("Ingresa bien el peso.\nLos quilates del Diamantes son de 0.2 hasta 1 quilate")
            if test_grabado is False:
                raise Exception("El valor de grabado de diamante esta mal ingresado, (ingresa Si o No)")
            if test_origen is False:
                raise Exception("El origen esta mal ingresado, ingresalo nuevamente")
        except ValueError:
            tk.messagebox.showinfo("Ingresa bien el tamaño del diamante (0.2-1)")
        except Exception as error:
            tk.messagebox.showinfo(str(error),str(error))
        else:
            return [corte,tamano,grabado,origen]

    def obtener_info_diamante_bruto(self):
        try:
            tamano = self.entry_tamano_raw.get()
            grabado = self.entry_grabado_raw.get()
            origen = self.entry_origen_raw.get()
            test_tamano = float(tamano)
            test_grabado = ((grabado.lower() == "no") or (grabado.lower() == "si"))
            test_origen = origen.isalpha()
            if (test_tamano < 0) or (test_tamano > 1):
                raise Exception("Ingresa bien el peso.\nLos quilates del Diamantes son de 0.2 hasta 1 quilate")
            if test_grabado is False:
                raise Exception("El valor de grabado de diamante esta mal ingresado, (ingresa Si o No)")
            if test_origen is False:
                raise Exception("El origen esta mal ingresado, ingresalo nuevamente")
        except ValueError:
            tk.messagebox.showinfo("Ingresa bien el tamaño del diamante (0.2-1)")
        except Exception as error:
            tk.messagebox.showinfo(str(error), str(error))
        else:
            return [ tamano, grabado, origen]


    def mostrar_menu_elegir_diamante(self):
        self.ventana_diamond_ashes.destroy()
        self.ventana_user_register.iconify()
        self.ventana_user_register.state("zoomed")
    def mostrar_menu_elegir_diamante_bruto(self):
        self.ventana_raw_diamond.destroy()
        self.ventana_user_register.iconify()
        self.ventana_user_register.state("zoomed")
    def mostrar_menu_diamante_corte(self):
        self.ventana_diamond_ashes.destroy()
        self.ventana_user_register.iconify()
        self.ventana_user_register.state("zoomed")



    def create_window_delete_order(self,controller):
        self.principal_window.ventana.withdraw()
        self.ventana_order_delete_register = tk.Toplevel()
        self.ventana_order_delete_register.iconbitmap("imagenes/algordanza_imagen.ico")
        self.ventana_order_delete_register.title("Algordanza Colombia")
        self.ventana_order_delete_register.geometry("1080x720")
        self.ventana_order_delete_register.resizable(True, True)
        self.ventana_order_delete_register.title("Cancelar Pedido")
        self.ventana_order_delete_register.config(background="white")
        self.ventana_order_delete_register.maxsize(1080, 900)
        self.ventana_order_delete_register.state("zoomed")

        self.ventana_order_delete_register_title_frame = tk.Frame(self.ventana_order_delete_register)
        self.ventana_order_delete_register_title_frame.config(background="white")
        self.ventana_order_delete_register_frame_empty_1 = tk.Label(self.ventana_order_delete_register_title_frame,
                                                            text="                                                                                                       ",
                                                            background="white")
        self.ventana_order_delete_register_frame_empty_2 = tk.Label(self.ventana_order_delete_register_title_frame,
                                                            text="                                                                                           ",
                                                            background="white")

        self.ventana_order_delete_register_title_frame.grid(row=0, column=0)
        self.ventana_order_delete_register_frame_empty_1.grid(row=0, column=0)
        self.ventana_order_delete_register_frame_empty_2.grid(row=0, column=2)

        self.ventana_order_buttons = tk.Frame(self.ventana_order_delete_register)
        self.ventana_order_buttons.config(background="white", borderwidth=0)
        self.ventana_order_buttons.grid(row=1, column=0)
        self.ventana_order_delete_register_frame_empty_3 = tk.Label(self.ventana_order_delete_register,
                                                            text="              ", background="white")
        self.ventana_order_delete_register_frame_empty_4 = tk.Label(self.ventana_order_delete_register,
                                                            text="                                                                        ",
                                                            background="white")
        self.ventana_order_delete_register_frame_empty_3.grid(row=0, column=0)
        self.ventana_order_delete_register_frame_empty_4.grid(row=1, column=3)

        self.ventana_order_delete_register_title = tk.Label(self.ventana_order_delete_register_title_frame)
        self.ventana_order_delete_register_title.config(font=("Candara", 48), fg="white", image=self.logo,
                                                background="white")
        self.ventana_order_delete_register_title.grid(row=0, column=1)
        self.label_id = tk.Label(self.ventana_order_buttons, image= self.pedido_id, background="white")
        self.label_id.grid(row=1, column=0)
        self.entry_id = tk.Entry(self.ventana_order_buttons, font=("Calibri bold", 25), fg="white",
                                     background="#023671", justify="center", bd=4, width=35, borderwidth=0, )
        self.entry_id.grid(row=1,column=1)

        self.button_back_delete = tk.Button(self.ventana_order_buttons, image=self.menu, borderwidth=0,
                                     background="white", command=self.volver_menu_delete_order)
        self.button_final_delete_register = tk.Button(self.ventana_order_buttons, image=self.user_delete,
                                               borderwidth=0, command=controller.getinfodeleteorder,
                                               background="white")
        self.button_back_delete.grid(row=4, column=0)
        self.button_final_delete_register.grid(row=4, column=1)
        self.ventana_order_delete_register.mainloop()

    def get_info_delete_order(self):
        try:
            id=self.entry_id.get()
            if id.isdigit() is False:
                raise Exception("El ID es un Número")
            test_id=int(id)
        except Exception as error:
            tk.messagebox.showinfo(str(error), str(error))
        else:
            return id



















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


