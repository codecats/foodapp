from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import os
Builder.load_file(os.path.dirname(os.path.realpath(__file__)) + '/accidents.kv')

class DetailWidget(BoxLayout):
    label_first = ObjectProperty(None)

    def __init__(self, accident_title=None, **kwargs):
        super(DetailWidget, self).__init__(**kwargs)
        self.label_first.text = accident_title

class AccidentsWidget(BoxLayout):
    layout = ObjectProperty(None)
    accident_btn = ObjectProperty(None)

    def callme(self, instance):
        instance.text = 'aa'
        self.remove_widget(self.layout)
        self.add_widget(DetailWidget(instance.text))

    def __init__(self, **kwargs):
        super(AccidentsWidget, self).__init__(**kwargs)

        def on_resp(request, response):
            for key, val in response.items():
                self.layout.add_widget(Button(text=str(val)))

        req = UrlRequest(
                    'http://echo.jsontest.com/gry/one/filmy/duo',
                    on_resp, method='post')

