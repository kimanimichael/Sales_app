from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.popup import Popup


class Login(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def login(self):
        if self.email.text == '' and self.password.text == '':
            ScreenManager().current = "mainWindow"
        else:
            self.invalid_login()

    def invalid_login(self):
        pop = Popup(title='Invalid login',
                    content=Label(text='Invalid email or password'),
                    size_hint=(None, None), size=(400, 400))
        pop.open()