from UItkinter import UI
from modelo import Algordanza
class Controller:
    def __init__(self,vista:UI):
        self.vista: UI = vista
    def start(self):
        self.vista.create_principal_window(self)
    def create_window_user_register(self):
        self.vista.create_window_register(self)
