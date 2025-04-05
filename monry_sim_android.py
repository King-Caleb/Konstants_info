import sys

from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen


class AnimatedSplash(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.frames = [
            "C:\\Users\\aalamu\\Desktop\\Caleb's fun folder\\Code\\money sim\\Load_1.png",
            "C:\\Users\\aalamu\\Desktop\\Caleb's fun folder\\Code\\money sim\\Load_2.png",
            "C:\\Users\\aalamu\\Desktop\\Caleb's fun folder\\Code\\money sim\\Load_3.png",
            "C:\\Users\\aalamu\\Desktop\\Caleb's fun folder\\Code\\money sim\\Load_4.png"
        ]
        self.frame_index = 0
        self.update_interval = 0.2  # Frame change interval
        Clock.schedule_interval(self.update_frame, self.update_interval)
        # Stop animation after 3 seconds
        Clock.schedule_once(self.stop_animation, 3)

    def update_frame(self, dt):
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.source = self.frames[self.frame_index]

    def stop_animation(self, dt):
        Clock.unschedule(self.update_frame)
        app = App.get_running_app()
        # Switch to the main screen (you can replace MainScreen with your main screen)
        app.root.current = 'main'


class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(AnimatedSplash())  # Add AnimatedSplash as a widget of SplashScreen


class MainScreen(Screen):
    pass


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SplashScreen(name='splash'))  # Add SplashScreen instead of AnimatedSplash
        sm.add_widget(MainScreen(name='main'))
        sm.current = 'splash'  # Start with splash screen
        return sm


MyApp().run()
