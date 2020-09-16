from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase



        

class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if self.email.text == 'mikalkimmani@gmail.com' and self.password.text == '1236':
            sm.current = "main"
        else:
            invalid_login()
     
    
class TodaySales(Screen):
    opening_chicken = ObjectProperty(None)
    closing_chicken = ObjectProperty(None)
    chicken_price = ObjectProperty(None)
    
    def csales(self):
        sales = (int(self.opening_chicken.text) - int(self.closing_chicken.text))* int(self.chicken_price.text)
        print(sales)

       



class MainWindow(Screen):
    def computeBtn(self):
        sm.current = "today"

    def logOut(self):
        sm.current = "login"
  

class WindowManager(ScreenManager):
    pass 

def invalid_login():
    pop = Popup(title= 'Invalid login', 
                content = Label(text = 'Invalid email or password'),
                size_hint = (None, None), size =(400,400))
    pop.open()

  
kv = Builder.load_file("cred.kv")

sm = WindowManager()
    

screens = [LoginWindow(name = "login"), MainWindow(name = "main"), TodaySales(name = "today")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"

class MyApp(App):
    def build(self):
        return sm



if __name__ == "__main__":
    MyApp().run()