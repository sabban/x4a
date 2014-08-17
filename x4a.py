#!/usr/bin/python

# kivy import
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

import Connection.Connection

class X4aRoot(BoxLayout):
    def Connection_callback(self):
        self.clear_widgets()
        self.add_widget(Connection.Connection.Connection())

class X4aApp(App):
    def build_config(self, config):
        config.setdefaults('General', {'host': "localhost"})
        config.setdefaults('HTTP', {'username': "username"})
        config.setdefaults('HTTP', {'password': "password"})
        config.setdefaults('HTTP', {'http_port': 8080 })
        config.setdefaults('TCP', {'tcp_port': 9090 })
        config.setdefaults('TCP', {'buffer_size': 1024 })

    def build_settings(self, settings):
        settings.add_json_panel("Network settings", self.config, data='''
[
    {
        "type": "title",
        "title": "General"
    },
    {
        "type": "string",
        "title": "Host",
        "desc": "host of xbmc instance to connect to",
        "section": "General",
        "key": "host"
    },
    {
        "type": "title",
        "title": "HTTP"
    },
    {
        "type": "string",
        "title": "Username",
        "desc": "Username to logon to XBMC",
        "section": "HTTP",
        "key": "username"
    },
    {
        "type": "string",
        "title": "Password",
        "desc": "Password to logon to XBMC",
        "section": "HTTP",
        "key": "password"
    },
    {
        "type": "numeric",
        "title": "HTTP port",
        "desc": "HTTP port used",
        "section": "HTTP",
        "key": "http_port"
    },
    {
        "type": "title",
        "title": "TCP"
    },
    {
        "type": "numeric",
        "title": "TCP port",
        "desc": "TCP port used",
        "section": "TCP",
        "key": "tcp_port"
    },
    {
        "type": "numeric",
        "title": "buffer size",
        "desc": "TCP buffer size",
        "section": "TCP",
        "key": "buffer_size"
    }
]''')

if __name__ == '__main__':
    X4aApp().run()

