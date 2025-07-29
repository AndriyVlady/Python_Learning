from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.label = Label(text="Привет, Андрей!", font_size=32)
        self.button = Button(text="Нажми меня", size_hint=(1, 0.3), font_size=24)
        self.button.bind(on_press=self.on_button_press)

        layout.add_widget(self.label)
        layout.add_widget(self.button)

        return layout

    def on_button_press(self, instance):
        self.label.text = "Ты нажал кнопку!"

if __name__ == "__main__":
    MyApp().run()
