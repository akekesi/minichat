import os
import customtkinter

from PIL import Image
from typing import Dict
from logger_config import logger


# TODO: put these (inc. padx/y, border_width...) into a separate file for global variable
WIDGETS_LIST = [
    [],  # image of item:  widget - Label
    [],  # name of item:   widget - Entry
    [],  # type of item:   widget - Combobox
    [],  # delete button:  widget - Button
    [],  # hash of item
]
TYPES_ITEM = [
    "private",
    "public",
]
PATH_LIST = os.path.join(os.path.dirname(__file__), "..", "list")


class SubList(customtkinter.CTkFrame):
    def __init__(self, master):
        logger.debug("0")
        super().__init__(master=master)

        self.message_first = True

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        self.frame_list = customtkinter.CTkFrame(master=master, fg_color="transparent")
        self.frame_list.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.frame_list.grid_rowconfigure(0, weight=1)
        self.frame_list.grid_columnconfigure(0, weight=1)

        self.frame_add = customtkinter.CTkFrame(master=master, fg_color="transparent")
        self.frame_add.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.frame_add.grid_columnconfigure(0, weight=1)

        self.frame_docs_scrollable = customtkinter.CTkScrollableFrame(master=self.frame_list)
        self.frame_docs_scrollable.grid(row=0, column=0, sticky="nsew")
        self.frame_docs_scrollable.grid_columnconfigure(1, weight=1)

        self.button_add = customtkinter.CTkButton(master=self.frame_add, text="Add", width=75, border_width=2, border_color="gray30", command=self.add_item)
        self.button_add.grid(row=0, column=0, padx=(0, 2*10+6), pady=0, sticky="e")

        logger.debug("1")

    def add_item(self, item: Dict[str | int, str] | None = None) -> None:
        logger.debug("0")

        n = len(WIDGETS_LIST[0])
        
        hash_ = 0
        name_ = "alien_ice_cream"
        type_ = 0

        image_to_open = os.path.join(PATH_LIST, name_, f"{name_}.png")
        image_ = customtkinter.CTkImage(
            dark_image=Image.open(image_to_open),
            size=(25, 25)
        )

        WIDGETS_LIST[0].append(
            customtkinter.CTkLabel(master=self.frame_docs_scrollable, image=image_, text="", justify="center", cursor="hand2")
        )
        WIDGETS_LIST[0][n].grid(row=n, column=0, padx=(0, 0), pady=(10, 0), sticky="ew")
        WIDGETS_LIST[0][n].bind("<Button-1>", lambda event, name=name_: self.open_item(name))

        WIDGETS_LIST[1].append(
            customtkinter.CTkEntry(master=self.frame_docs_scrollable)
        )
        WIDGETS_LIST[1][n].grid(row=n, column=1, padx=(10, 0), pady=(10, 0), sticky="ew")
        WIDGETS_LIST[1][n].configure(state="normal")
        WIDGETS_LIST[1][n].delete(0, "end")
        WIDGETS_LIST[1][n].insert(0, name_)
        WIDGETS_LIST[1][n].configure(state="disabled")

        WIDGETS_LIST[2].append(
            customtkinter.CTkComboBox(master=self.frame_docs_scrollable, values=TYPES_ITEM, width=100, justify="center", state="readonly",)# command=lambda type_=type_, n=n: self.update_type(n, type_))
        )
        WIDGETS_LIST[2][n].grid(row=n, column=2, padx=(10, 0), pady=(10, 0), sticky="ew")
        WIDGETS_LIST[2][n].set(TYPES_ITEM[type_])

        WIDGETS_LIST[3].append(
            customtkinter.CTkButton(master=self.frame_docs_scrollable, text="Delete", width=75, border_width=2, border_color="gray30", command=lambda n=n: self.delete_item(n))
        )
        WIDGETS_LIST[3][n].grid(row=n, column=3, padx=10, pady=(10, 0), sticky="ew")

        WIDGETS_LIST[4].append(hash_)

        logger.debug("1")

    def delete_item(self, n: int) -> None:
        logger.debug("0")

        if WIDGETS_LIST[0][n]:
            WIDGETS_LIST[0][n].destroy()
            WIDGETS_LIST[1][n].destroy()
            WIDGETS_LIST[2][n].destroy()
            WIDGETS_LIST[3][n].destroy()

            WIDGETS_LIST[0][n] = ""
            WIDGETS_LIST[1][n] = ""
            WIDGETS_LIST[2][n] = ""
            WIDGETS_LIST[3][n] = ""
            WIDGETS_LIST[4][n] = "" 

        logger.info("delete %i", n)
        logger.debug("1")

    def open_item(self, name: str) -> None:
        logger.debug("0")
        logger.info("%s", name)
        logger.debug("1")
