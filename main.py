from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
import random

GUI = Builder.load_file("app.kv")

class MeuAplicativo(App):
    def build(self):
        return GUI
    
    def d4(self):
        resultado = random.randint(1, 4)
        print(resultado)
    
    def d6(self):
        resultado = random.randint(1, 6)
        print(resultado)
        
    def d8(self):
        resultado = random.randint(1, 8)
        print(resultado)
        
    def d10(self):
        resultado = random.randint(1, 10)
        print(resultado)
        
    def d12(self):
        resultado = random.randint(1, 12)
        print(resultado)
        
    def d20(self):
        resultado = random.randint(1, 20)
        print(resultado)

MeuAplicativo().run()