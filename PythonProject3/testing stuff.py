from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.


Builder.load_string("""

<HomeScreen>:
    FloatLayout:
        Button:
            text: 'Settings'
            size_hint: 0.2, 0.1
            pos_hint: {"x": 0.25, "y": 0.0}
            on_press: root.manager.current = 'settings'
            
        Button:
            text: 'Quit'
            size_hint: 0.2, 0.1
            pos_hint: {"x": 0.55, "y": 0.0}
            on_press: root.manager.current = 'quit'
            


<SettingsScreen>:
    FloatLayout:
        Button:
            text: 'This button has the settings'
            size_hint: 0.2, 0.1
            pos_hint: {"x": 0.25, "y": 0.0}
        
        Button:
            text: 'Back to home'
            size_hint: 0.2, 0.1
            pos_hint: {"x": 0.55, "y": 0.0}
            on_press: root.manager.current = 'home'
            
<QuitScreen>:
    FloatLayout:
        Button:
            text: 'go back to home'
            size_hint: 0.2, 0.1
            pos_hint: {"x": 0.25, "y": 0.0}
            on_press: root.manager.current = 'home'
        Button:
            text: 'confirm quit'
            size_hint: 0.2, 0.1
            pos_hint: {"x": 0.55, "y": 0.0}
            on_press: TestApp().quit()
""")

# Declare both screens
class HomeScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class QuitScreen(Screen):
    pass

class TestApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(QuitScreen(name='quit'))

        return sm

if __name__ == '__main__':
    TestApp().run()