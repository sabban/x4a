from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.button import Button

import xbmcjsonapi.xbmcjsonapi
import x4a

default_connection_type='tcp'

Builder.load_file('Connection/Connection.kv')

class Connection(BoxLayout):
    def __init__(self, **kwargs):
        super(Connection, self).__init__(**kwargs)
        config = x4a.X4aApp.get_running_app().config
        self.host = config.get('General', 'host')
        self.username = config.get('HTTP', 'username')
        self.HTTP_password = config.get('HTTP', 'password')
        self.HTTP_port = config.get('HTTP', 'http_port')
        self.TCP_port = config.get('TCP', 'tcp_port')
        self.TCP_buffer_size = config.get('TCP', 'buffer_size')
        self.xbmc_instance = xbmcjsonapi.xbmcjsonapi.xbmcjsonapi( **{'port': self.TCP_port, 'host': self.host, 'TCP_buffer_size': self.TCP_buffer_size})
        self.VideoLibraryButton()
        self.AudioLibraryButton()

    def VideoLibraryButton(self):
        try:
            VideoLibrary = self.xbmc_instance.VideoLibrary()
        except:
            print "Error"
            
    def VideoLibrary_callback(self):
        print "Videolibrary"
        
    def AudioLibraryButton(self):
        try:
            AudioLibrary = self.xbmc_instance.AudioLibrary()
        except:
            print "Error Audio Library"

    def AudioLibrary_callback(self):
        print "Audiolibrary"
        
    def Root_callback(self):
        self.clear_widgets()
        self.add_widget(x4a.X4aRoot())
        
