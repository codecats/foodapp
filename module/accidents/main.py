#import ast
import json
import os
import sys
from kivy import Config

from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from module.screen.main import Screens

Builder.load_file(os.path.dirname(os.path.realpath(__file__)) + '/accidents.kv')

class DetailWidget(BoxLayout):
    label_first = ObjectProperty(None)

    def __init__(self, accident_title=None, **kwargs):
        super(DetailWidget, self).__init__(**kwargs)
        self.label_first.text = accident_title


class AccidentsWidget(BoxLayout):
    layout = ObjectProperty(None)
    accident_btn = ObjectProperty(None)

    def _swith_view(self, instance_view):
        self.remove_widget(self.layout)
        self.add_widget(instance_view)
        Screens().history.append(self)

    def options(self, instance):
        self._swith_view(OptionsWidget())

    def callme(self, instance):
        self._swith_view(DetailWidget(instance.text))

    def __init__(self, **kwargs):
        super(AccidentsWidget, self).__init__(**kwargs)

        def on_resp(request, response):
            for key, val in response.items():
                button = Button(text=str(val), on_press=self.callme)
                #button.background_color = ast.literal_eval(Config.get('modules', 'color_picked'))
                #print ast.literal_eval(Config.get('modules', 'color_picked'))
                self.layout.add_widget(button)

        req = UrlRequest(
                    'http://echo.jsontest.com/gry/one/filmy/duo',
                    on_resp, method='post')

class OptionsWidget(BoxLayout):
    def on_color(self, instance):
        print instance

        Config.set('modules', 'color_picked', instance.color)
        Config.write()
        print instance.color
        for child in self.children:
            child.background_color = instance.color