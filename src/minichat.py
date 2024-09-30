# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


import os
import openai
import webbrowser
import customtkinter

from src.sub_chat import SubChat
from src.sub_logo import SubLogo
from src.sub_list import SubList
from src.sub_hover_message import create_hover_message
from src.global_variable import (
    NAME,
    PADX,
    PADY,
    WIDTH_BORDER,
    COLOR_FRAME,
    COLOR_BORDER,
    COLOR_INFO,
    COLOR_OK,
    COLOR_OK_HOVER,
    COLOR_NOK,
    COLOR_NOK_HOVER,
    SIZE_MINICHAT,
    PATH_ICO_MINICHAT,
    PATH_API_KEY,
    URL_OPENAI,
    logger,
)


class MiniChat(customtkinter.CTk):
    def __init__(self) -> None:
        logger.debug("0")
        super().__init__()

        self.title(NAME)
        self.geometry(f"{SIZE_MINICHAT["width"]}x{SIZE_MINICHAT["height"]}")
        self.minsize(width=SIZE_MINICHAT["width"], height=SIZE_MINICHAT["height"])
        self.iconbitmap(PATH_ICO_MINICHAT)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.api_key = ""
        self.tab_current = None

        if os.path.exists(PATH_API_KEY):
            with open(PATH_API_KEY, "r", encoding="utf-8") as f:
                self.api_key = f.read()

        self.set_tab()
        self.set_info()
        self.set_bind()

        self.check_api_key()

        logger.debug("1")

    def set_tab(self) -> None:
        logger.debug("0")

        self.tabview = customtkinter.CTkTabview(
            master=self,
            segmented_button_fg_color=COLOR_BORDER,
            segmented_button_unselected_color=COLOR_BORDER,
            border_width=WIDTH_BORDER,
            border_color=COLOR_BORDER,
            fg_color=COLOR_FRAME,
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

    def set_info(self) -> None:
        logger.debug("0")

        self.frame_info = customtkinter.CTkFrame(master=self, fg_color=COLOR_FRAME, border_width=WIDTH_BORDER, border_color=COLOR_BORDER)
        self.frame_info.grid(row=1, column=0, padx=PADX, pady=(0, PADY), sticky="nsew")
        self.frame_info.grid_columnconfigure(0, weight=1)

        self.button_api_key = customtkinter.CTkButton(master=self.frame_info, text="Set API Key", border_width=WIDTH_BORDER, border_color=COLOR_BORDER, command=self.set_api_key)
        self.button_api_key.grid(row=0, column=0, padx=2*PADX, pady=PADY, sticky="w")
        self.button_api_key.configure(fg_color=COLOR_NOK)
        self.button_api_key.configure(hover_color=COLOR_NOK_HOVER)

        self.label_openai = customtkinter.CTkLabel(master=self.frame_info, text="MiniChat is building on OpenAI", text_color=COLOR_INFO, cursor="hand2")
        self.label_openai.grid(row=0, column=1, padx=2*PADX, pady=PADY, sticky="e")
        create_hover_message(
            self.label_openai,
            text=f"Open {URL_OPENAI}",
        )

        self.label_openai.bind(sequence="<Button-1>", command=self.open_openai)

        logger.debug("1")

    def set_bind(self) -> None:
        logger.debug("0")

        self.bind("<Return>", self.click_return)
        self.bind("<Alt-Right>", self.click_arrow_right)
        self.bind("<Alt-Left>", self.click_arrow_left)

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

    def set_api_key(self) -> None:
        logger.debug("0")

        api_key = self.dialog_api_key(
            title="Set API Key",
            text= "Enter your OpenAI API Key:",
        )
        if api_key is None:
            return
        self.api_key = api_key

        self.save_api_key()
        self.check_api_key()

        logger.debug("1")

    def dialog_api_key(self, title: str, text: str) -> str:
        logger.debug("0")

        dialog = customtkinter.CTkInputDialog(title=title, text=text)
        input_ = dialog.get_input()

        logger.info("%s", input_)
        logger.debug("1")

        return input_

    def save_api_key(self) -> None:
        logger.debug("0")

        with open(PATH_API_KEY, "w", encoding="utf-8") as f:
            f.write(self.api_key)

        logger.debug("1")

    def check_api_key(self) -> bool:
        logger.debug("0")

        try:
            client = openai.OpenAI(api_key=self.api_key)
            client.models.list()
            logger.info("API connection successful")
            self.button_api_key.configure(fg_color=COLOR_OK)
            self.button_api_key.configure(hover_color=COLOR_OK_HOVER)
            logger.debug("1")
            return True
        except openai.APIConnectionError as e:
            logger.info("API connection failed\n\t%s", e)
            self.button_api_key.configure(fg_color=COLOR_NOK)
            self.button_api_key.configure(hover_color=COLOR_NOK_HOVER)
            logger.debug("2")
            return False
        except openai.AuthenticationError as e:
            logger.info("API key is incorrect\n\t%s", e)
            self.button_api_key.configure(fg_color=COLOR_NOK)
            self.button_api_key.configure(hover_color=COLOR_NOK_HOVER)
            logger.debug("3")
            return False

    # pylint: disable=unused-argument
    def open_openai(self, event=None) -> None:
        logger.debug("0")
        webbrowser.open(url=URL_OPENAI)
        logger.debug("1")


if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    minichat = MiniChat()
    minichat.mainloop()
