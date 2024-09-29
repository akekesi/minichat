# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


import customtkinter

from tkinter import Toplevel
from global_variable import (
    PADX,
    PADY,
    WIDTH_BORDER,
    COLOR_FRAME,
    COLOR_BORDER,
    COLOR_INFO,
    logger,
)


class SubHoverMessage():
    def __init__(self, widget) -> None:
        logger.debug("0")

        self.widget = widget
        self.message_window = None

        logger.debug("1")

    def show(self, text: str) -> None:
        logger.debug("0")

        if self.message_window or not text:
            return
        x, y, _, dy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 5
        y = y + self.widget.winfo_rooty() + int(dy)

        self.message_window = Toplevel(master=self.widget, background=COLOR_BORDER, borderwidth=WIDTH_BORDER)
        self.message_window.wm_overrideredirect(1)
        self.message_window.wm_geometry(f"+{x}+{y}")

        frame = customtkinter.CTkFrame(master=self.message_window, fg_color=COLOR_FRAME)
        frame.pack()
        label = customtkinter.CTkLabel(master=frame, text=text, text_color=COLOR_INFO, justify="left")
        label.pack(padx=PADX, pady=0.5*PADY)

        logger.debug("1")

    def hide(self):
        logger.debug("0")

        if self.message_window:
            self.message_window.destroy()
        self.message_window = None

        logger.debug("1")


def create_hover_message(widget: customtkinter.CTkLabel, text: str) -> None:
    logger.debug("0")

    hover_message = SubHoverMessage(widget=widget)

    # pylint: disable=unused-argument
    def enter(event=None) -> None:
        hover_message.show(text=text)

    # pylint: disable=unused-argument
    def leave(event=None) -> None:
        hover_message.hide()

    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

    logger.debug("1")
