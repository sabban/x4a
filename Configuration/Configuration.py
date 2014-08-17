from kivy.config import ConfigParser
from kivy.uix.settings import Settings
#import ConfigParser
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.lang import Builder

import x4a


config = ConfigParser()
config.read('myconfig.ini')

Configuration = Settings()
Configuration.add_json_panel('My custom panel', config, 'configuration.json')


        
# class Configuration(GridLayout):  
#     def save(self):
# #        config = Config.ConfigParser()
#         if "default" not in Config.sections():
#             Config.addsection("default")
#         if "tcp" not in Config.sections():
#             Config.addsection("tcp")
#         if "http" not in Config.sections():
#             Config.addsection("http")
#         Config.set("default","host",f_host)
#         Config.set("http","username",f_username)
#         Config.set("http","password",f_password)
#         Config.set("http","port",f_http_port)
#         Config.set("tcp","port",f_tcp_port)

#         self.clear_widgets()
#         self.add_widget(xr4a.Xr4aRoot())



