import os
import customtkinter

from sub_chat import SubChat
from sub_logo import SubLogo
from sub_list import SubList
from logger_config import logger


# TODO: put these (inc. padx/y, border_width...) into a separate file for global variable
SIZE = {
    "width": 450,
    "height": 550,
}
PATH_ICON = os.path.join(os.path.dirname(__file__), "..", "ico", "minichat.ico")
TABS = {
    "Chat": SubChat,
    "Logo": SubLogo,
    "List": SubList,
}
TABS_KEYS = list(TABS.keys())


class MiniChat(customtkinter.CTk):
    def __init__(self):
        logger.debug("0")
        super().__init__()

        self.title("MiniChat")
        self.geometry(f"{SIZE["width"]}x{SIZE["height"]}")
        self.minsize(width=SIZE["width"], height=SIZE["height"])
        self.iconbitmap(PATH_ICON)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.tabview = customtkinter.CTkTabview(
            master=self,
            segmented_button_fg_color="gray30",
            segmented_button_unselected_color="gray30",
            border_color="gray30",
            border_width=2,
            command=self.click_tab,
        )
        self.tabview.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        for tab in TABS_KEYS:
            self.tabview.add(name=tab)
        self.tab_current = self.tabview.get()
        self.click_tab()

        self.sub_chat = SubChat(master=self.tabview.tab(TABS_KEYS[0]))
        self.sub_logo = SubLogo(master=self.tabview.tab(TABS_KEYS[1]))
        self.sub_list = SubList(master=self.tabview.tab(TABS_KEYS[2]))

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

    def click_arrow_right(self, event=None) -> None:
        logger.debug("0")

        tab_previous = self.tab_current
        index_current = TABS_KEYS.index(self.tab_current)
        index_next = min(len(TABS_KEYS) - 1, index_current + 1)
        self.tab_current = TABS_KEYS[index_next]
        self.tabview.set(self.tab_current)

        logger.info("%s --> %s", tab_previous, self.tab_current)
        logger.debug("1")

    def click_arrow_left(self, event=None) -> None:
        logger.debug("0")

        tab_previous = self.tab_current
        index_current = TABS_KEYS.index(self.tab_current)
        index_next = max(0, index_current - 1)
        self.tab_current = TABS_KEYS[index_next]
        self.tabview.set(self.tab_current)

        logger.info("%s --> %s", tab_previous, self.tab_current)
        logger.debug("1")

    def click_return(self, event=None) -> None:
        logger.debug("0")

        if self.tab_current == TABS_KEYS[0]:
            self.sub_chat.send_message()

        if self.tab_current == TABS_KEYS[1]:
            self.sub_logo.generate_image()

        if self.tab_current == TABS_KEYS[2]:
            self.sub_list.add_item()

        logger.info("%s", self.tab_current)
        logger.debug("1")


if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    minichat = MiniChat()
    minichat.mainloop()
