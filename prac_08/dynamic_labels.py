from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_list = ['Bob', 'Denise', 'Nick']

    def build(self):
        # Create a main layout for the app
        self.title = 'Dynamic Labels'
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.name_list:
            label = Label(text=name)
            self.root.add_widget(label)


DynamicLabelsApp().run()