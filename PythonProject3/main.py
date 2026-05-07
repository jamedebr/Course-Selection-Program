from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock

# with open('accounts.txt', 'r') as file:
#     lines = file.readlines()
#     lines.sort(key=lambda lines: int(lines.split()[-1]))
#

class Login(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submitButton(self):
        with open("accounts.txt", "r") as file:
            accounts = file.read()
            if self.email.text not in accounts and '@woodland.on.ca' in self.email.text:
                with open("accounts.txt", "a") as file:
                    file.write('\n'+self.email.text + " " + self.password.text + " " + "0")
                self.manager.current = 'home'
            else:
                self.manager.current = 'login'

    def toSignInButton(self):
        self.manager.current = 'signin'

class SignIn(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def signInButton(self):
        with open('accounts.txt', 'r') as file:
            content = file.read()
            if self.email.text+' '+self.password.text in content:
                self.manager.current = 'home'
            else:
                self.manager.current = 'signin'
    def toLogin(self):
        self.manager.current = 'login'


class Home(Screen):
    def on_enter(self):
        print("on_enter has run")
        grid = self.ids.leaderboard
        grid.clear_widgets()

        userstats = self.ids.userstats

        with open('accounts.txt', 'r') as file:
            lines = file.readlines()
            lines.sort(key=lambda lines: int(lines.split()[-1]), reverse=True)
            rankcounter = 0
            for item in lines:
                rankcounter += 1
                user = item.split(' ')
                numlaps = user[2]
                if rankcounter < 6:

                    rank = Label(text = f"{rankcounter}")
                    grid.add_widget(rank)

                    username = user[0]
                    username = username.replace('@woodland.on.ca', '')
                    username = Label(text = username)
                    grid.add_widget(username)

                    numlaps = Label(text=numlaps)
                    grid.add_widget(numlaps)

                Login = self.manager.get_screen('login')
                email_value = Login.ids.email.text

                if email_value == "":
                    SignIn = self.manager.get_screen('signin')
                    email_value = SignIn.ids.email.text

                if email_value in user:
                    userstats_rank = Label(text=f"{rankcounter}")
                    userstats.add_widget(userstats_rank)

                    userstats_username = user[0]
                    userstats_username = userstats_username.replace('@woodland.on.ca', '')
                    userstats_username = Label(text=userstats_username)
                    userstats.add_widget(userstats_username)

                    userstats_numlaps = Label(text=f"{user[2]}")
                    userstats.add_widget(userstats_numlaps)




class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Login(name='login'))
        sm.add_widget(SignIn(name='signin'))
        sm.add_widget(Home(name='home'))

        sm.current = 'login'
        return sm

if __name__ == '__main__':
    MyApp().run()

