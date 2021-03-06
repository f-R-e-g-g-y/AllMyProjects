from kivy.app import App

from kivy.lang import Builder

from kivy.uix.boxlayout import BoxLayout

import time

from androidtoast import toast

Builder.load_string('''

<CameraClick>:

    orientation: 'vertical'

    Camera:

        id: camera

        resolution: (1280, 720)

        play: False

        canvas.before:

            PushMatrix

            Rotate:

                angle: -90

                origin: self.center

        canvas.after:

            PopMatrix

    ToggleButton:

        text: 'Play'

        on_press: camera.play = not camera.play

        size_hint_y: None

        height: '48dp'

    Button:

        text: 'Capture'

        size_hint_y: None

        height: '48dp'

        on_press: root.capture()

''')

class CameraClick(BoxLayout):

    def capture(self):

        '''

        Function to capture the images and give them the names

        according to their captured time and date.

        '''

        camera = self.ids['camera']

        timestr = time.strftime("%Y%m%d_%H%M%S")

        #camera.export_to_png("IMG_" + timestr)

        camera.export_to_png("/sdcard/IMG_{}.png".format(timestr))

        toast("Captured", True, 80, 200, 0)

class TestCamera(App):

    def build(self):

        return CameraClick()

TestCamera().run()
