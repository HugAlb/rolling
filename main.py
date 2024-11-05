#importa o app, builder (GUI)
#Cria a aplicação
#Cria a função

from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load_file("app.kv")

class MeuAplicativo(App):
    def build(self):
        return GUI

MeuAplicativo().run()