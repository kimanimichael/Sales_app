from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label



choma_price = 150
necks_price = 220
liver_price = 220
legs_price = 100
gizzards_price = 360
sausages_price = 30
smokies_price = 20



        

class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if self.email.text == 'm' and self.password.text == '1':
            sm.current = "main"
        else:
            invalid_login()
     
    
class TodaySales(Screen):
    opening_chicken = ObjectProperty(None)
    added_chicken = ObjectProperty(None)
    closing_chicken = ObjectProperty(None)
    chicken_price = ObjectProperty(None)
    chomas_cut = ObjectProperty(None)
    opening_choma = ObjectProperty(None)
    closing_choma = ObjectProperty(None)
    kuku_out = ObjectProperty(None)
    
    

    def csales(self):
        chicken_sales = (float(self.opening_chicken.text) +float(self.added_chicken.text) - float(self.closing_chicken.text)- float(self.chomas_cut.text)- float(self.kuku_out.text))* float(self.chicken_price.text)
        print("Chicken: " + str(chicken_sales))
    def choma(self):
        choma_sales = (float(self.opening_choma.text) + float(self.chomas_cut.text)*4 - float(self.closing_choma.text))*choma_price
        print("Choma: " + str(choma_sales))    
        

    


    
    
    

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
    
    def nsales(self):
        necks_sales = (float(self.opening_necks.text) +float(self.added_necks.text) - float(self.closing_necks.text))* necks_price
        print("Necks: " + str(necks_sales))

    def livsales(self):
        liver_sales = (float(self.opening_liver.text) +float(self.added_liver.text) - float(self.closing_liver.text))* liver_price
        print("Liver: " + str(liver_sales))

    def legsales(self):
        legs_sales = (float(self.opening_legs.text) +float(self.added_legs.text) - float(self.closing_legs.text))*legs_price
        print("Legs: " + str(legs_sales))




class ThirdScreen(Screen):
    opening_gizzards = ObjectProperty(None)
    added_gizzards = ObjectProperty(None)
    closing_gizzards = ObjectProperty(None)
    opening_sausages = ObjectProperty(None)
    added_sausages = ObjectProperty(None)
    closing_sausages = ObjectProperty(None)
    opening_smokies = ObjectProperty(None)
    added_smokies = ObjectProperty(None)
    closing_smokies = ObjectProperty(None)

    def gizzardsales(self):
        gizzard_sales = (float(self.opening_gizzards.text) +float(self.added_gizzards.text) - float(self.closing_gizzards.text))* gizzards_price
        print("Gizzards: " + str(gizzard_sales))

    def sausagesales(self):
        sausage_sales = (float(self.opening_sausages.text) +float(self.added_sausages.text) - float(self.closing_sausages.text))* sausages_price
        print("Liver: " + str(sausage_sales)) 

    def smokiesales(self):
        smokie_sales = (float(self.opening_smokies.text) +float(self.added_smokies.text) - float(self.closing_smokies.text))* smokies_price
        print("Liver: " + str(smokie_sales))



       



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

k = TodaySales()
#k.csales()
    

  
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