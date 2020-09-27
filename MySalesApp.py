from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
# load the build  files

Builder.load_file("login.kv")
Builder.load_file("sales.kv")
Builder.load_file("sales2.kv")
Builder.load_file("sales3.kv")


class MainWindow(Screen):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)

    def computeBtn(self):
        ScreenManager().current = "sales"

    def logOut(self):
        ScreenManager().current = "login"

class ScreenManager(ScreenManager):
    pass

class MySalesApp(App):
    def build(self):
        return Builder.load_file('MySales.kv')


if __name__ == "__main__":
    MySalesApp().run()