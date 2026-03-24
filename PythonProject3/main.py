from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(Button, GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='Password'))
        self.password = TextInput(password=False, multiline=False)
        self.add_widget(self.password)
        self.text = 'hi'

        self.bind(on_press=self.switch)

    def switch(self, item):
        if self.password == 'ABCD' and self.username == 'cyan':
            myapp.screen_manager.current = 'Second'

class SecondPage(Button):
    def __init__(self):
        super().__init__()
        self.text = 'hi there'
        self.bind(on_press=self.switch)

    def switch(self, item):
        myapp.screen_manager.current = 'First'

class MyApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.LoginScreen = LoginScreen()
        screen = Screen(name='First')
        screen.add_widget(self.LoginScreen)
        self.screen_manager.add_widget(screen)

        self.secondpage = SecondPage()
        screen = Screen(name='Second')
        screen.add_widget(self.secondpage)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

myapp = MyApp()
myapp.run()

# if __name__ == '__main__':
#     MyApp().run()
