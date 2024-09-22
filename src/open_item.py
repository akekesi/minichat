# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


import customtkinter

from PIL import Image
from tkinter import PhotoImage
from global_variable import (
    NAME,
    PADX,
    PADY,
    BORDER_WIDTH,
    BORDER_COLOR,
    SIZE_OPEN_ITEM,
    SIZE_LOGO,
    logger,
)


class OpenItem(customtkinter.CTkToplevel):
    def __init__(
        self,
        name: str,
        path_chat: str,
        path_logo: str,
    ) -> None:
        logger.debug("0")
        super().__init__()

        self.path_chat = path_chat
        self.path_logo = path_logo

        self.title(f"{NAME} - {name}")
        self.attributes("-topmost", True)
        self.grab_set()
        self.geometry(f"{SIZE_OPEN_ITEM["width"]}x{SIZE_OPEN_ITEM["height"]}")
        self.minsize(width=SIZE_OPEN_ITEM["width"], height=SIZE_OPEN_ITEM["height"])
        self.wm_iconbitmap()
        icon_photo = PhotoImage(file=self.path_logo)
        self.after(200, lambda: self.iconphoto(False, icon_photo))

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.tab_current = None

        self.set_tab()
        self.set_bind()

        logger.debug("1")

    def set_tab(self) -> None:
        logger.debug("0")

        self.tabview = customtkinter.CTkTabview(
            master=self,
            segmented_button_fg_color=BORDER_COLOR,
            segmented_button_unselected_color=BORDER_COLOR,
            border_width=BORDER_WIDTH,
            border_color=BORDER_COLOR,
            command=self.click_tab,
        )
        self.tabview.grid(row=0, column=0, padx=PADX, pady=PADY, sticky="nsew")
        self.tabs = [
            "Logo",
            "Chat",
        ]

        self.tabview.add(name=self.tabs[0])
        self.sub_chat = SubChat(master=self.tabview.tab(self.tabs[0]), path_chat=self.path_chat)

        self.tabview.add(name=self.tabs[1])
        self.sub_logo = SubLogo(master=self.tabview.tab(self.tabs[1]), path_logo=self.path_logo)

        self.tab_current = self.tabview.get()
        self.click_tab()

        logger.debug("1")

    def set_bind(self) -> None:
        logger.debug("0")

        self.bind("<Escape>", self.click_escape)
        self.bind("<Alt-Right>", self.click_arrow_right)
        self.bind("<Alt-Left>", self.click_arrow_left)

        logger.debug("1")

    def click_tab(self) -> None:
        logger.debug("0")
        logger.debug("1")

    # pylint: disable=unused-argument
    def click_escape(self, event=None) -> None:
        logger.debug("0")
        self.destroy()
        logger.debug("1")

    # pylint: disable=unused-argument
    def click_arrow_right(self, event=None) -> None:
        logger.debug("0")

        tab_previous = self.tab_current
        index_current = self.tabs.index(self.tab_current)
        index_next = min(len(self.tabs) - 1, index_current + 1)
        self.tab_current = self.tabs[index_next]
        self.tabview.set(self.tab_current)

        logger.info("%s --> %s", tab_previous, self.tab_current)
        logger.debug("1")

    # pylint: disable=unused-argument
    def click_arrow_left(self, event=None) -> None:
        logger.debug("0")

        tab_previous = self.tab_current
        index_current = self.tabs.index(self.tab_current)
        index_next = max(0, index_current - 1)
        self.tab_current = self.tabs[index_next]
        self.tabview.set(self.tab_current)

        logger.info("%s --> %s", tab_previous, self.tab_current)
        logger.debug("1")


# pylint: disable=too-many-ancestors
class SubChat(customtkinter.CTkFrame):
    def __init__(
        self,
        master,
        path_chat: str,
    ) -> None:
        logger.debug("0")
        super().__init__(master=master)

        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

        self.textbox_chat = customtkinter.CTkTextbox(master=master, border_width=BORDER_WIDTH, border_color=BORDER_COLOR, activate_scrollbars=True, state="disabled")
        self.textbox_chat.grid(row=0, column=0, padx=PADX, pady=PADY, sticky="nsew")

        with open(path_chat, "r", encoding="utf-8") as f:
            chat = f.read()
        self.textbox_chat.configure(state="normal")
        self.textbox_chat.insert("end", chat)
        self.textbox_chat.configure(state="disabled")


# pylint: disable=too-many-ancestors
class SubLogo(customtkinter.CTkFrame):
    def __init__(
        self,
        master,
        path_logo: str,
    ) -> None:
        logger.debug("0")
        super().__init__(master=master)

        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

        logo = customtkinter.CTkImage(
            dark_image=Image.open(path_logo),
            size=SIZE_LOGO
        )
        self.label_logo = customtkinter.CTkLabel(master=master, image=logo, text="", justify="center")
        self.label_logo.grid(row=0, column=0, padx=PADX, pady=PADY, sticky="nsew")
