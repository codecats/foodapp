from kivy.app import App
from kivy.factory import Factory
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from module import utils

from kivy.config import Config
from module.accidents.main import AccidentsWidget

Config.set('kivy', 'window_icon', 'data/download.png')

class FoodWidget(BoxLayout):

    layout = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(FoodWidget, self).__init__(**kwargs)
        Factory.register('AccidentsWidget', module='food.module.accidents.main')

        self.layout.add_widget(Factory.AccidentsWidget())



class FoodApp(App):
    def on_pause(self):
        return True
    
    def build(self):

        return FoodWidget()


if __name__ == '__main__':
    FoodApp().run()
