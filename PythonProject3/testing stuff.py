

# cp1 = [0.1234, 0.3456]
# cp2 = [1.1234, 0.3456]
# cp3 = [1.1234, 1.3456]
# cp4 = [0.1234, 1.3456]

# checkpoint1 = False
# checkpoint2 = False
# checkpoint3 = False
# checkpoint4 = False


#location = getlocation()
# if location[0] > cp1[0] and location[1] > cp1[1]: <--includes outside    or   doesn't include outside-->   if abs(location[0]-cp1[0]) < 0.1 and abs(location[1]-cp1[1]) < 0.1:
#     print("cp1 reached")
#     checkpoint1 = True

# if checkpoint1 == True and checkpoint2 == True and checkpoint3 == True and checkpoint4 == True:
#   laps += 1
#   checkpoint1 = False
#   checkpoint2 = False
#   checkpoint3 = False
#   checkpoint4 = False





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