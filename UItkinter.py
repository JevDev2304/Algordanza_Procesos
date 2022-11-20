import tkinter as tk
from tkinter import messagebox
from datetime import *



class UI:
    def __init__(self):
        self.principal_window = None
        self.logo=None

    def load_images(self):
        self.logo = tk.PhotoImage(file="imagenes/Algordanza_logo.png")
        self.logo = self.logo.subsample(2)
        self.user_register= tk.PhotoImage(file="imagenes/Registrar Usuario.png")
        self.user_delete= tk.PhotoImage(file="imagenes/Eliminar Usuario.png")
        self.order_register= tk.PhotoImage(file="imagenes/Registrar Pedido.png")
        self.order_delete= tk.PhotoImage(file= "imagenes/Eliminar_Pedido.png")
        self.get_user_id= tk.PhotoImage(file= "imagenes/Obtener_id_Usuario.png")
        self.show_excel = tk.PhotoImage(file="imagenes/informacion_pedidos.png")

        self.register_name = tk.PhotoImage(file= "imagenes/Registrar_Nombre.png")
        self.register_cell = tk.PhotoImage(file="imagenes/Registrar_Celular.png")


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
        self.principal_window.button_Delete = tk.Button(self.principal_window.buttons_frame, borderwidth=0, image=self.user_delete, background="white")
        self.principal_window.button_Delete.grid(row =0, column=2)

        self.principal_window.button_Register_order = tk.Button(self.principal_window.buttons_frame, borderwidth=0,image=self.order_register, background="white")
        self.principal_window.button_Register_order.grid(row=0, column=3)

        self.principal_window.button_Delete_order = tk.Button(self.principal_window.buttons_frame,borderwidth=0,image= self.order_delete, background="white")
        self.principal_window.button_Delete_order.grid(row=1,column=1)
        self.principal_window.button_get_id_user = tk.Button(self.principal_window.buttons_frame, borderwidth=0, image=self.get_user_id, background="white")
        self.principal_window.button_get_id_user.grid(row=1, column=2)
        self.principal_window.button_excel_info = tk.Button(self.principal_window.buttons_frame, borderwidth=0, image=self.show_excel, background="white")
        self.principal_window.button_excel_info.grid(row=1, column=3)




        self.principal_window.ventana.mainloop()

    def create_window_register(self, controller):
        self.principal_window.ventana.withdraw()
        self.ventana_user_register = tk.Toplevel()
        self.ventana_user_register.iconbitmap("imagenes/algordanza_imagen.ico")
        self.ventana_user_register.title("Algordanza Colombia")
        self.ventana_user_register.geometry("1080x720")
        self.ventana_user_register.resizable(True, True)
        self.ventana_user_register.title("Registrar Cliente ")
        self.ventana_user_register.config(background="white")
        self.ventana_user_register.maxsize(1280, 720)

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

        self.label_name = tk.Label(self.ventana_user_register_buttons_frame,image=self.register_name,borderwidth=0, background="white")
        self.label_name.grid(row=0,column=1)
        self.entry_name = tk.Entry(self.ventana_user_register_buttons_frame, font=("Calibri bold", 25), fg="white", background="#023671",justify="center",bd=4, width=35, borderwidth=0,)
        self.entry_name.grid(row=0,column=2)

        self.label_cel = tk.Label(self.ventana_user_register_buttons_frame, image=self.register_cell, borderwidth=0,
                                   background="white")
        self.label_cel.grid(row=0, column=1)
        self.entry_cel = tk.Entry(self.ventana_user_register_buttons_frame, font=("Calibri bold", 25), fg="white",
                                   background="#023671", justify="center", bd=4, width=35, borderwidth=0, )
        self.entry_cel.grid(row=1, column=2)

        self.ventana_user_register.mainloop()


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


