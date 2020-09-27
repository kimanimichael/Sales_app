from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

class Sales(Screen):
    opening_chicken = ObjectProperty(None)
    added_chicken = ObjectProperty(None)
    closing_chicken = ObjectProperty(None)
    chicken_price = ObjectProperty(None)
    chomas_cut = ObjectProperty(None)
    opening_choma = ObjectProperty(None)
    closing_choma = ObjectProperty(None)
    kuku_out = ObjectProperty(None)

    def csales(self):
        chicken_sales = (float(self.opening_chicken.text) + float(self.added_chicken.text) -
                         float(self.closing_chicken.text) - float(self.chomas_cut.text)-
                         float(self.kuku_out.text)) * float(self.chicken_price.text)
        print("Chicken: " + str(chicken_sales))
        return float(chicken_sales)

    def choma(self):
        choma_sales = (float(self.opening_choma.text) + float(self.chomas_cut.text) * 4 -
                       float(self.closing_choma.text)) * float(self.choma_price.text)
        print("Choma: " + str(choma_sales))
        return float(choma_sales)
