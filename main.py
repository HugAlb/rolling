from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.core.window import Window
import random

GUI = Builder.load_file("app.kv")

class MeuAplicativo(App):
    def build(self):
        Window.size = (530,550)
        Window.resizable = False
        return GUI
    
    def d4(self):
        resultado = random.randint(1, 4)
        resultado = str(resultado)
        self.root.ids["resultado"].text = resultado
    
    def d6(self):
        resultado = random.randint(1, 6)
        resultado = str(resultado)
        self.root.ids["resultado"].text = resultado
        
    def d8(self):
        resultado = random.randint(1, 8)
        resultado = str(resultado)
        self.root.ids["resultado"].text = resultado
        
    def d10(self):
        resultado = random.randint(1, 10)
        resultado = str(resultado)
        self.root.ids["resultado"].text = resultado
        
    def d12(self):
        resultado = random.randint(1, 12)
        resultado = str(resultado)
        self.root.ids["resultado"].text = resultado
        
    def d20(self):
        resultado = random.randint(1, 20)
        resultado = str(resultado)
        self.root.ids["resultado"].text = resultado

MeuAplicativo().run()