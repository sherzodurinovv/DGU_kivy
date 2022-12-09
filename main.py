import kivy
from kivy.app import App
kivy.require('1.9.0')
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
import misol as ms

class MainApp(App):
    def build(self):
        self.title="Mobil ilova"
        layout1=BoxLayout(orientation="vertical",spacing=10,padding=10)
        self.l1=Label(text="Ilovamizga xush kelibsiz")
        layout1.add_widget(self.l1)
        # self.t1=TextInput(hint_text="Ismingizni kiriting")
        # layout1.add_widget(self.t1)
        layout2=BoxLayout(orientation="horizontal",spacing=10,padding=40)
        layout1.add_widget(layout2)
        self.b1 = Button(background_color="green",background_normal="residburgerstest.jpg")
        layout2.add_widget(self.b1)
        self.b1.bind(on_press=self.f1)
        self.b2 = Button(background_color="green",background_normal="uvwpburgerstest.jpg")
        layout2.add_widget(self.b2)
        self.b2.bind(on_press=self.f2)
        self.b3=Button(background_color="green",background_normal="uvwpeithertest.jpg")
        layout2.add_widget(self.b3)
        self.b4=Button(background_color="red",background_normal="tozalash.jpg")
        layout2.add_widget(self.b4)
        self.b4.bind(on_press=self.f4)
        self.b3.bind(on_press=self.f3)

        return layout1


    def f1(self,instance):
        self.l1.text=str(ms.resid_burgers_test())

    def f2(self,instance):
         self.l1.text=str(ms.uvwp_burgers_test())

    def f3(self,instance):
         self.l1.text=str(ms.uvwp_ethier_test())

    def f4(self,instance):
        self.l1.text="Ilovamizga xush kelibsiz"



if __name__=="__main__":
    MainApp().run()