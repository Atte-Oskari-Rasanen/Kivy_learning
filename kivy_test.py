# Simple drag from a boxlayout onto a drop zone, animate the return if the drop zone is missed.
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.behaviors import DragBehavior
from kivy.uix.button import Button
from kivy.properties import BooleanProperty, ListProperty
from kivy.animation import Animation
from kivy.uix.image import Image, AsyncImage
#https://realpython.com/mobile-app-kivy-python/#displaying-an-image
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)



#https://github.com/kivy-garden/draggable

#layouts:https://kivy.org/doc/stable/guide/widgets.html
kv = """

<DragButton>:

    drag_rectangle: self.x, self.y, self.width, self.height
    drag_timeout: 10000000
    drag_distance: 10
    on_release: print(f'Drag Button {self.text} pressed')
    name: 'Test game'

StackLayout:
    size_hint: .5, .5
    StackLayout:
        #orientation: 'vertical'
        size_hint: .2, .2
        DragButton:
            canvas:
                Rectangle:
                    pos: self.pos
                    size: self.size
                    source: '/home/atte/Documents/Kivy_stuff/assets/ims/cow.png'

        DragButton:
            canvas:
                Rectangle:
                    pos: self.pos
                    size: self.size
                    source: '/home/atte/Documents/Kivy_stuff/assets/ims/fox.png'

                # canvas:
                #     Rectangle:
                #         source: '/home/atte/Documents/Kivy_stuff/assets/ims/cow.png'
                #         
                #         size: self.icon_size
                #         #allow_stretch: True
                #         pos: self.pos[0] + self.width - self.icon_size[0], self.pos[1] + self.icon_size[1] / 2


        Image:
            id: remove_zone
            source: '/home/atte/Documents/Kivy_stuff/assets/ims/sweden.png'
            pos_hint: {'left':1, 'top':1}
            size_hint: 1, 1
            pos: 100, 100
            size: 200, 300
            allow_stretch: True
            keep_ratio: False
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 0.2    # blue
                Rectangle:
                    pos: self.pos
                    size: self.size

        Image:
            id: remove_zone
            source: '/home/atte/Documents/Kivy_stuff/assets/ims/spain.png'
            pos: 100, 200
            pos_hint: {'left':1, 'top':1}
            
            size_hint: 1, 1
            size: 200, 300
            allow_stretch: True
            keep_ratio: False
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 0.2    # blue
                Rectangle:
                    pos: self.pos
                    size: self.size


            # orientation: 'vertical'
            # Label:
            #     text: 'Do Nothing'
            #     # canvas:
            #     #     Rectangle:
            #     #         source: '/home/atte/Documents/Kivy_stuff/assets/ims/spain.png'
            #     #         size: self.icon_size
            #     #         pos: self.pos[0] + self.width - self.icon_size[0], self.pos[1] + self.icon_size[1] / 2

            # Label:
            #     id: remove_zone
            #     text: 'Remove Widget'
"""

class ThirdScreen(Screen):
    def enable_cropping(self):
        print("\nThirdScreen:")
        print(self.ids.main_image.pos)
        print(self.ids.main_image.size)
        print("\tAbsolute size=", self.ids.main_image.norm_image_size)
        print("\tAbsolute pos_x=", self.ids.main_image.center_x - self.ids.main_image.norm_image_size[0] / 2.)
        print("\tAbsolute pos_y=", self.ids.main_image.center_y - self.ids.main_image.norm_image_size[1] / 2.)

class DragButton(DragBehavior, Button):
    dragging = BooleanProperty(False)
    original_pos = ListProperty()

    def on_pos(self, *args):
        self.drag_rectangle = [self.x, self.y, self.width, self.height]

    def on_size(self, *args):
        self.drag_rectangle = [self.x, self.y, self.width, self.height]

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            print('on touch down')
            self.original_pos = self.pos
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if touch.grab_current is self:
            self.opacity = 0.4
            self.dragging = True
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        app = App.get_running_app()
        if self.dragging:
            self.opacity = 1
            self.dragging = False
            if self.collide_widget(app.root.ids.remove_zone):  # refers to the image in kv string, removes the image
                self.parent.
                self.parent.remove_widget(self)
            # else:
            #     anim = Animation(pos=self.original_pos, duration=1)
            #     anim.start(self)
        return super().on_touch_up(touch)


class DragTestApp(App):
    def build(self):
        return Builder.load_string(kv)


DragTestApp().run()
 

