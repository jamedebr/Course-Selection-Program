from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


class layout(BoxLayout):
    def __init__(self):
        super().__init__()
        self.button = Button(text='Press me')

        self.add_widget(self.button)

class MyApp(App):
    def build(self):
        layout = FloatLayout()

        label1 = Label(text="click here --->", size_hint=(0.3, 0.2), pos_hint={'center_x':0.3, 'center_y':0.5})
        label2 = Label(text="<-----right here!", size_hint=(0.3, 0.7), pos_hint={'center_x':0.7, 'center_y':0.5})
        button1 = Button(text='click me', size_hint=(None, None), pos_hint={'center_x':0.5, 'center_y':0.5})

        layout.add_widget(label1)
        layout.add_widget(label2)
        layout.add_widget(button1)
        return layout

if __name__ == "__main__":
    MyApp().run()
