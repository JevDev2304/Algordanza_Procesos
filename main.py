from UItkinter import *
from controller import *


if __name__ == '__main__':

    interfaz = UI()
    modelo= Algordanza()
    modelo.cargar_info_excel_clientes()
    controller = Controller(interfaz,modelo)

    controller.start()
    modelo.guardar_info_clientes_excel()




