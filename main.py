import kivy
from kivy.app import App
from kivy.uix.label import Label

class SayHello(App):
    def build(self):
        return Label(text = "Say Hello")

if __name__ == "__main__":
    SayHello().run()