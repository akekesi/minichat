# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


import customtkinter

from sub_chat import SubChat
from sub_logo import SubLogo
from sub_list import SubList
from global_variable import (
    NAME,
    PADX,
    PADY,
    BORDER_WIDTH,
    BORDER_COLOR,
    SIZE_MINICHAT,
    PATH_ICO_MINICHAT,
    logger,
)


class MiniChat(customtkinter.CTk):
    def __init__(self) -> None:
        logger.debug("0")
        super().__init__()

        self.title(NAME)
        self.attributes("-topmost", True)
        self.geometry(f"{SIZE_MINICHAT["width"]}x{SIZE_MINICHAT["height"]}")
        self.minsize(width=SIZE_MINICHAT["width"], height=SIZE_MINICHAT["height"])
        self.iconbitmap(PATH_ICO_MINICHAT)

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
            "Chat",
            "Logo",
            "List",
        ]
        self.tabview.add(name=self.tabs[0])
        self.sub_chat = SubChat(master=self.tabview.tab(self.tabs[0]))

        self.tabview.add(name=self.tabs[1])
        self.sub_logo = SubLogo(master=self.tabview.tab(self.tabs[1]))

        self.tabview.add(name=self.tabs[2])
        self.sub_list = SubList(master=self.tabview.tab(self.tabs[2]))

        self.tab_current = self.tabview.get()
        self.click_tab()

        logger.debug("1")

    def set_bind(self) -> None:
        logger.debug("0")

        self.bind('<Return>', self.click_return)
        self.bind('<Alt-Right>', self.click_arrow_right)
        self.bind('<Alt-Left>', self.click_arrow_left)

        logger.debug("1")

    def click_tab(self) -> None:
        logger.debug("0")

        tab_previous = self.tab_current
        self.tab_current = self.tabview.get()

        logger.info("%s --> %s", tab_previous, self.tab_current)
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

    # pylint: disable=unused-argument
    def click_return(self, event=None) -> None:
        logger.debug("0")

        if self.tab_current == self.tabs[0]:
            self.sub_chat.send_message()

        if self.tab_current == self.tabs[1]:
            self.sub_logo.generate_logo()

        if self.tab_current == self.tabs[2]:
            self.sub_list.add_item()

        logger.info("%s", self.tab_current)
        logger.debug("1")


if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    minichat = MiniChat()
    minichat.mainloop()
