from kivy.app import App
from plyer import gps
from kivy.clock import mainthread

# edit
class GPSApp(App):
    def on_start(self):
        # Configure and start GPS service once on app start
        try:
            gps.configure(on_location=self.on_location)
            gps.start()
        except NotImplementedError:
            print("GPS not supported on this platform")

    @mainthread
    def on_location(self, **kwargs):
        # This function runs every time the location updates
        # kwargs contains: lat, lon, speed, bearing, altitude, accuracy
        print(f"Latitude: {kwargs['lat']}, Longitude: {kwargs['lon']}")

    def on_stop(self):
        gps.stop()

if __name__ == '__main__':
    GPSApp().run()

# with open('accounts.txt', 'r') as file:
#     lines = file.readlines()
#     lines.sort(key=lambda lines: int(lines.split()[-1]), reverse=True)
# print(lines)

# user = ["abcd", "efgh"]
#
# if len(user) >= 3:
#     numlaps = user[2]
# else:
#     numlaps = "0"
#     user.append("0")
#
# print(user)
# <Home>:
#     GridLayout:
#         cols: 3
#
#         Label:
#             text: ''
#
#         GridLayout:
#             id: leaderboard
#             cols: 3
#             spacing: 10
#             padding: 10
#
#
#
#         Label:
#             text: ''
# from kivy.app import App
# from kivy.lang import Builder
# from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button
#
# # Create both screens. Please note the root.manager.current: this is how
# # you can control the ScreenManager from kv. Each screen has by default a
# # property manager that gives you the instance of the ScreenManager used.
#
#
# Builder.load_string("""
#
# <HomeScreen>:
#     FloatLayout:
#         Button:
#             text: 'Settings'
#             size_hint: 0.2, 0.1
#             pos_hint: {"x": 0.25, "y": 0.0}
#             on_press: root.manager.current = 'settings'
#
#         Button:
#             text: 'Quit'
#             size_hint: 0.2, 0.1
#             pos_hint: {"x": 0.55, "y": 0.0}
#             on_press: root.manager.current = 'quit'
#
#
#
# <SettingsScreen>:
#     FloatLayout:
#         Button:
#             text: 'This button has the settings'
#             size_hint: 0.2, 0.1
#             pos_hint: {"x": 0.25, "y": 0.0}
#
#         Button:
#             text: 'Back to home'
#             size_hint: 0.2, 0.1
#             pos_hint: {"x": 0.55, "y": 0.0}
#             on_press: root.manager.current = 'home'
#
# <QuitScreen>:
#     FloatLayout:
#         Button:
#             text: 'go back to home'
#             size_hint: 0.2, 0.1
#             pos_hint: {"x": 0.25, "y": 0.0}
#             on_press: root.manager.current = 'home'
#         Button:
#             text: 'confirm quit'
#             size_hint: 0.2, 0.1
#             pos_hint: {"x": 0.55, "y": 0.0}
#             on_press: TestApp().quit()
# """)
#
# # Declare both screens
# class HomeScreen(Screen):
#     pass
#
# class SettingsScreen(Screen):
#     pass
#
# class QuitScreen(Screen):
#     pass
#
# class TestApp(App):
#
#     def build(self):
#         # Create the screen manager
#         sm = ScreenManager()
#         sm.add_widget(HomeScreen(name='home'))
#         sm.add_widget(SettingsScreen(name='settings'))
#         sm.add_widget(QuitScreen(name='quit'))
#
#         return sm
#
# if __name__ == '__main__':
#     TestApp().run()