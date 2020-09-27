from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

class Sales2(Screen):
    necks_price = 220
    liver_price = 220
    legs_price = 100

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
        necks_sales = (float(self.opening_necks.text) + float(self.added_necks.text) - float(
            self.closing_necks.text)) * self.necks_price
        print("Necks: " + str(necks_sales))
        return necks_sales

    def livsales(self):
        liver_sales = (float(self.opening_liver.text) + float(self.added_liver.text) - float(
            self.closing_liver.text)) * self.liver_price
        print("Liver: " + str(liver_sales))

    def legsales(self):
        legs_sales = (float(self.opening_legs.text) + float(self.added_legs.text) - float(
            self.closing_legs.text)) * self.legs_price
        print("Legs: " + str(legs_sales))
