# Simple drag from a boxlayout onto a drop zone, animate the return if the drop zone is missed.
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.behaviors import DragBehavior
from kivy.uix.button import Button
from kivy.properties import BooleanProperty, ListProperty
from kivy.animation import Animation
from kivy.uix.image import Image, AsyncImage

kv = """
<DragButton>:

    drag_rectangle: self.x, self.y, self.width, self.height
    drag_timeout: 10000000
    drag_distance: 10
    on_release: print(f'Drag Button {self.text} pressed')

BoxLayout:
    BoxLayout:
        orientation: 'vertical'
        DragButton:
            text: ' '
            icon_size: 200, 200
            canvas:
                Rectangle:
                    source: '/home/atte/Documents/Kivy_stuff/assets/ims/cow.png'
                    size: self.icon_size
                    #allow_stretch: True
                    pos: self.pos[0] + self.width - self.icon_size[0], self.pos[1] + self.icon_size[1] / 2

        # DragButton:
        #     text: ''
        #     #icon_size: 16, 16
        #     canvas:
        #         Rectangle:
        #             source: '/home/atte/Documents/Kivy_stuff/assets/ims/fox.png'
        #             size: self.icon_size
        #             allow_stretch: True
        #             pos: self.pos[0] + self.width - self.icon_size[0], self.pos[1] + self.icon_size[1] / 2
        
        DragButton:
            text: '3'
    BoxLayout:
        id: middle
    BoxLayout:
        id:right
#        orientation: 'vertical'
        Image:
            source: '/home/atte/Documents/Kivy_stuff/assets/ims/spain.png'

            # canvas:
            #     Rectangle:
            #         source: '/home/atte/Documents/Kivy_stuff/assets/ims/spain.png'
            #         size: self.icon_size
            #         pos: self.pos[0] + self.width - self.icon_size[0], self.pos[1] + self.icon_size[1] / 2

        Image:
            source: '/home/atte/Documents/Kivy_stuff/assets/ims/sweden.png'

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
            if self.collide_widget(app.root.ids.remove_zone):
                self.parent.remove_widget(self)
            else:
                anim = Animation(pos=self.original_pos, duration=1)
                anim.start(self)
        return super().on_touch_up(touch)


class DragTestApp(App):
    def build(self):
        return Builder.load_string(kv)


DragTestApp().run()
 

