from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import os
Builder.load_file(os.path.dirname(os.path.realpath(__file__)) + '/accidents.kv')

class AccidentsWidget(BoxLayout):
    layout = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(AccidentsWidget, self).__init__(**kwargs)

        def callme(instance):
            def on_resp(request, response):
                print response
                for key, val in response.items():
                    self.layout.add_widget(Button(text=str(val)))
                instance.text = str(response.itervalues())
            req = UrlRequest(
                        'http://echo.jsontest.com/gry/one/filmy/duo',
                        on_resp, method='post')
        pong = Button(text='Accident')
        pong.bind(on_press=callme)
        self.layout.add_widget(pong)
