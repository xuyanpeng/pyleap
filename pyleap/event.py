from pyleap.window import window
from pyleap.mouse import mouse
from pyleap.collision import shape_clicked
from pyleap.util import all_shapes


@window.event
def on_mouse_motion(x, y, dx, dy):
    """ 当鼠标没有按下时移动的时候触发 """
    mouse.x, mouse.y = x, y
    mouse.move()
    window.update_caption(mouse)


@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    """ 当鼠标按下并且移动的时候触发 """
    mouse.x, mouse.y = x, y
    mouse.move()


class MouseKeyCode:
    """
    button
    1 - 左键
    2 - 滚轮
    4 - 右键
    """
    LEFT = 1
    MIDDLE = 2
    RIGHT = 4

@window.event
def on_mouse_press(x, y, button, modifiers):
    """ 按下鼠标时 

    """ 
    if button == MouseKeyCode.LEFT:
        mouse.press()
    elif button == MouseKeyCode.RIGHT:
        mouse.right_press()

    # 判断是否有图形的点击事件被触发了
    shapes = list(all_shapes)
    while shapes:
        shape = shapes.pop()
        if(shape._press and shape_clicked(shape)):
            shape._press()


@window.event
def on_mouse_release(x, y, button, modifiers):
    """ 松开鼠标时 """ 
    if button == MouseKeyCode.LEFT:
        mouse.release()
    elif button == MouseKeyCode.RIGHT:
        mouse.right_release()
