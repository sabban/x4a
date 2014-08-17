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
        self.orientation = "vertical"
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
        self.VideoLibraryButton = Button(text='Video Library', on_press=self.callback_VideoLibrary())
        try:
            VideoLibrary = self.xbmc_instance.VideoLibrary()
            self.add_widget(self.VideoLibraryButton)
        except:
            print "Error"

    def callback_VideoLibrary(self):
        print "Videolibrary"
        
    def AudioLibraryButton(self):
        self.AudioLibraryButton = Button(text='Audio Library', on_press=self.callback_AudioLibrary())
        try:
            AudioLibrary = xbmc_instance.AudioLibrary()
            self.add_widget(self.AudioLibraryButton)
        except:
            print "Error Audio Library"

    def callback_AudioLibrary(self):
        print "Audiolibrary"
        
    def Root_callback(self):
        self.clear_widgets()
        self.add_widget(x4a.X4aRoot())
        
