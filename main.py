from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from carpal_data_collection_app.screens.camera_screen import CameraScreen
from carpal_data_collection_app.screens.loading_screen import LoadingScreen
from carpal_data_collection_app.screens.personelinfo_screen import PersonalInfoScreen

class ScreenManagement(ScreenManager):
    pass

class MyApp(App):

    def build(self):
        # Arka plan rengini beyaz yapma
        Window.clearcolor = (1, 1, 1, 1)
        screen_manager = ScreenManagement()
        loading_screen = LoadingScreen(name='loading')
        personal_info_screen = PersonalInfoScreen(name='personal_info')
        camera_screen = CameraScreen(name='camera_screen')
        screen_manager.add_widget(loading_screen)
        screen_manager.add_widget(personal_info_screen)
        screen_manager.add_widget(camera_screen)
        screen_manager.current = 'loading'

        # Kamera ekranını başlangıçta yükle, ancak otomatik oynatma özelliğini devre dışı bırak
        camera_screen.toggle_camera(None)

        return screen_manager


if __name__ == '__main__':
    MyApp().run()
