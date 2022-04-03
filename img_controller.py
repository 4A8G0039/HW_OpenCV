class img_controller(object):
    def __init__(self, ui):
        self.ui = ui
        self.__update_img()



    def __update_img(self):
        self.ui.verticalLayout.mouseReleaseEvent = self.show_mouse_release
        self.ui.verticalLayout.mouseMoveEvent = self.show_mouse_move

    def show_mouse_press(self, event):
        print(f"[show_mouse_press] {event.x()=}, {event.y()=}, {event.button()=}")


    def show_mouse_release(self, event):
        print(f"[show_mouse_release] {event.x()=}, {event.y()=}, {event.button()=}")

    def show_mouse_move(self, event):
        print(f"[show_mouse_move] {event.x()=}, {event.y()=}, {event.button()=}")

