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
    chomas_cut = ObjectProperty(None)
    opening_choma = ObjectProperty(None)
    closing_choma = ObjectProperty(None)
    opening_gizzards = ObjectProperty(None)
    added_gizzards = ObjectProperty(None)
    closing_gizzards = ObjectProperty(None)
    
    
    def csales(self):
        sales = (int(self.opening_chicken.text) - int(self.closing_chicken.text))* int(self.chicken_price.text)
        print(sales)

class SecondScreen(Screen):
    opening_necks = ObjectProperty(None)
    added_necks = ObjectProperty(None)
    closing_necks = ObjectProperty(None)
    opening_liver = ObjectProperty(None)
    added_liver = ObjectProperty(None)
    closing_liver = ObjectProperty(None)
    opening_legs = ObjectProperty(None)
    added_legs = ObjectProperty(None)
    closing_legs = ObjectProperty(None)
    


class ThirdScreen(Screen):
    opening_sausages = ObjectProperty(None)
    added_sausages = ObjectProperty(None)
    closing_sausages = ObjectProperty(None)
    opening_smokies = ObjectProperty(None)
    added_smokies = ObjectProperty(None)
    closing_smokies = ObjectProperty(None)





       



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
    

screens = [LoginWindow(name = "login"), MainWindow(name = "main"), TodaySales(name = "today"), SecondScreen(name= "second"), ThirdScreen(name="third")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"

class MyApp(App):
    def build(self):
        return sm



if __name__ == "__main__":
    MyApp().run()