from kivy.app import App
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from module import utils

from kivy.config import Config
Config.set('kivy', 'window_icon', 'data/download.png')

class FoodWidget(BoxLayout):

    layout = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(FoodWidget, self).__init__(**kwargs)
        def callme(instance):
            #test module imported here
            utils.Util()
            def on_resp(request, response):
                print response
                for key, val in enumerate(response):
                    self.layout.add_widget(Button(text=str(val)))
                instance.text = str(response[u'validate'])
            req = UrlRequest(
                        'http://validate.jsontest.com/?json=%7B%22key%22:%22value%22%7D',
                        on_resp, method='post')
        pong = Button(text='Tomasz App')
        pong.bind(on_press=callme)

        self.layout.add_widget(pong)


class FoodApp(App):
    def build(self):

        return FoodWidget()


if __name__ == '__main__':
    FoodApp().run()
