from kivy.app import App, platform
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from module import utils

from kivy.config import Config
from module.accidents.main import AccidentsWidget
from module.screen.main import Screens

Config.set('kivy', 'window_icon', 'data/download.png')


class FoodWidget(BoxLayout):
    layout = ObjectProperty(None)
    def go_back(self):
        if Screens().history:
            self.layout.clear_widgets()
            last = Screens().history.pop()
            class_type = type(last)
            self.layout.add_widget(class_type())


    def __init__(self, **kwargs):
        super(FoodWidget, self).__init__(**kwargs)
        Factory.register('AccidentsWidget', module='food.module.accidents.main')
        self.layout.add_widget(Factory.AccidentsWidget())

class FoodApp(App):
    screens = []
    manager = ObjectProperty()

    def on_pause(self):
        return True

    def post_build_init(self, *args):
        if platform() == 'android':
            import android
            android.map_key(android.KEYCODE_BACK, 1001)

        win = Window
        win.bind(on_keyboard=self.my_key_handler)

    def my_key_handler(self, window, keycode1, keycode2, text, modifiers):
        if keycode1 in [27, 1001]:
            self.manager.go_back()
            return True
        return False

    def build(self):
        mainWidget = FoodWidget()
        self.manager = mainWidget
        self.bind(on_start=self.post_build_init)
        return mainWidget

if __name__ == '__main__':
    FoodApp().run()
