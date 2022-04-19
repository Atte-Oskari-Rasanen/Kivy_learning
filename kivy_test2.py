import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.scrollview    import ScrollView
from kivy.uix.widget import Widget
from kivy.uix.behaviors import DragBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.properties import NumericProperty

from kivy.base import runTouchApp
from kivy.lang import Builder

Builder.load_string('''
<WidgetMenu>:
    canvas.before:
        Color:
            rgb: 0.9,0.5,0.3
        RoundedRectangle:
            pos:self.pos
            size: self.size
            radius: [20,]
    orientation: "vertical"
    padding:40

    # ScrollView:

    #     GridLayout:
    #         cols:1
    #         size_hint_y:None
    #         row_default_height:root.height*.15
    #         height:self.minimum_height
    #         MoveableImage:
    #             source:'/home/atte/Documents/Kivy_stuff/assets/ims/cow2.png'
    #         MoveableImage:
    #             source:'/home/atte/Documents/Kivy_stuff/assets/ims/fox.png'



<MoveableImage>:
    drag_rectangle: self.x, self.y, self.width, self.height
    drag_timeout: 100000000
    drag_distance: 0
    size_hint:None,None
    size:34,34
    
    #this will draw a canvas rectangle around the image, not needed
    # canvas:
    #     # Color:
    #     #     rgb:1,0,1
    #     Rectangle:
    #         pos: self.pos
    #         size: self.size

<MainLayout>:
    canvas:
        # Color:
        #     rgb:1,1,1
        Rectangle:
            size: self.size
            pos: self.pos
    WidgetMenu:
        size_hint: 0.15,0.15

''')

class MainLayout(FloatLayout):
    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(MainLayout, self).__init__(**kwargs)

        # let's add a Widget to this layout
        self.add_widget(
            country(source='/home/atte/Documents/Kivy_stuff/assets/ims/spain.png', size_hint=(.8, .5), pos_hint ={'x':.2, 'y':.5}))
    
        self.add_widget(
            country(source='/home/atte/Documents/Kivy_stuff/assets/ims/sweden.png', size_hint=(.8, .5), pos_hint ={'x':.5, 'y':.5}))
        self.add_widget(
            MoveableImage(source='/home/atte/Documents/Kivy_stuff/assets/ims/cow2.png'))
        self.add_widget(
            MoveableImage(source='/home/atte/Documents/Kivy_stuff/assets/ims/fox.png'))
        # if country.collide_widget(MoveableImage):
        #     print("!!!")


class country(Image):
    pass

class WidgetMenu(BoxLayout):
    pass
class MoveableImage(DragBehavior,FloatLayout, Image):
    def __init__(self, **kwargs):
        super(MoveableImage, self).__init__(**kwargs)
        #super(MoveableImage, self).on_touch_down(touch)
        self.drag_timeout = 10000000
        self.opacity=0.7
        self.drag_distance = 0
        self.drag_rectangle = [self.x, self.y, self.width, self.height]
        #opacity = NumericProperty(0.8)

        self.size_hint = (.13, .13)  
        self.keep_ratio = True
        self.allow_stretch = True  
    def on_pos(self, *args):
        self.drag_rectangle = [self.x, self.y, self.width, self.height]

    def on_size(self, *args):
        self.drag_rectangle = [self.x, self.y, self.width, self.height]

    # def on_touch_down(self,touch):
    #     if not self.collide_point(*touch.pos):
    #         return False
    #     workspace = self.parent.parent.parent.parent
    #     grid = self.parent
    #     menu = self.parent.parent.parent
    #     if "MainLayout" in str(workspace):
    #         grid.remove_widget(self)
    #         workspace.remove_widget(menu)

    #         # the following code assumes that workspace is the entire Window
    #         self.x = Window.mouse_pos[0] - (touch.pos[0] - self.x)
    #         self.y = Window.mouse_pos[1] - (touch.pos[1] - self.y)
    #         workspace.add_widget(self)
    #         touch.pos = Window.mouse_pos
    #     return super(MoveableImage, self).on_touch_down(touch)
class ScrollApp(App):
    def build(self):
        return MainLayout()

ScrollApp().run()
