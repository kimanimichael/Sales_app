from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

class Sales3(Screen):
    gizzards_price = 360
    sausages_price = 30
    smokies_price = 20

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
        gizzard_sales = ( float(self.opening_gizzards.text) + float(self.added_gizzards.text) -
                          float(self.closing_gizzards.text)) * self.gizzards_price
        print("Gizzards: " + str(gizzard_sales))

    def sausagesales(self):
        sausage_sales = (float(self.opening_sausages.text) + float(self.added_sausages.text) -
                         float(self.closing_sausages.text)) * self.sausages_price
        print("Sausages: " + str(sausage_sales))

    def smokiesales(self):
        smokie_sales = (float(self.opening_smokies.text) + float(self.added_smokies.text) -
                        float(self.closing_smokies.text))* self.smokies_price
        print("Smokies: " + str(smokie_sales))
