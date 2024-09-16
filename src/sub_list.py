import os
import json
import shutil
import customtkinter

from PIL import Image
from typing import Dict
from logger_config import logger
from global_variable import SUB_METHOD


# TODO: put these (inc. padx/y, border_width...) into a separate file for global variable
SIZE_LOGO = (256, 256)
SIZE_LOGO_LIST = (25, 25)
PATH_LIST = os.path.join(os.path.dirname(__file__), "..", "list")
PATH_LIST_CONFIG = os.path.join(PATH_LIST, "list_config.json")
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

try:
    with open(PATH_LIST_CONFIG, 'r') as f:
        LIST_CONFIG = json.load(f)
    logger.info("%s is opened", PATH_LIST_CONFIG)
except:
    logger.info("%s is not found", PATH_LIST_CONFIG)
    # TODO: break


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

        self.load_list()

        logger.debug("1")

    def add_item(self, item: Dict[str | int, str] | None = None) -> None:
        # TODO: check whether hash and n have conflict
        # TODO: split into smaller sub functions 
        logger.debug("0")

        if item:
            hash_ = item["hash"]
            name_ = item["name"]
            type_ = item["type"]
        else:
            hash_ = str(len(LIST_CONFIG))
            while True:
                name_ = self.dialog_item_name(
                    title="Name of Item",
                    text="Enter the name of the item:",
                )
                if name_ == None:
                    return
                if not name_:
                    logger.info("no name")
                    continue
                path_item = os.path.join(PATH_LIST, name_)
                if os.path.exists(path_item):
                    logger.info("%s is already exist", path_item)
                    continue
                break
            type_ = 0

            os.makedirs(path_item)
            logger.info("%s is created", path_item)

            chat = SUB_METHOD["get"]["chat"]()
            logo = SUB_METHOD["get"]["logo"]()
            self.save_chat(name=name_, chat=chat)
            self.save_logo(name=name_, logo=logo)

            item = {
                hash_: {
                    "state": 1,
                    "hash": hash_,
                    "name": name_,
                    "type": type_,
                },
            }
            LIST_CONFIG.update(item)
            self.update_list_config()

        n = len(WIDGETS_LIST[0])

        logo_path = os.path.join(PATH_LIST, name_, f"{name_}.png")
        logo_open = Image.open(logo_path)
        logo = customtkinter.CTkImage(
            dark_image=logo_open,
            size=SIZE_LOGO_LIST
        )

        WIDGETS_LIST[0].append(
            customtkinter.CTkLabel(master=self.frame_docs_scrollable, image=logo, text="", justify="center", cursor="hand2")
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
            customtkinter.CTkComboBox(master=self.frame_docs_scrollable, values=TYPES_ITEM, width=100, justify="center", state="readonly", command=lambda type_=type_, n=n: self.update_type(n, type_))
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

        hash_ = WIDGETS_LIST[4][n]
        LIST_CONFIG[hash_]["state"] = 0
        self.update_list_config()

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

    def dialog_item_name(self, title: str, text: str) -> str:
        logger.debug("0")

        dialog = customtkinter.CTkInputDialog(title=title, text=text)
        input_ = dialog.get_input()

        logger.info("%s", input_)
        logger.debug("1")

        return input_

    def save_chat(self, name: str, chat: str) -> None:
        logger.debug("0")

        path_chat = os.path.join(PATH_LIST, name, f"{name}.txt")
        with open(path_chat, 'w') as f:
            f.write(chat)

        logger.debug("1")

    def save_logo(self, name: str, logo: str | bytes) -> None:
        logger.debug("0")

        path_logo = os.path.join(PATH_LIST, name, f"{name}.png")

        # no logo generated --> path of default logo
        if type(logo) == str:
            shutil.copyfile(logo, path_logo)

        # logo generated --> logo in bytes
        if type(logo) == bytes:
            with open(path_logo, "wb") as f:
                f.write(logo)

        logger.debug("1")

    def load_list(self) -> None:
        logger.debug("0")

        for item in LIST_CONFIG.values():
            if item["state"]:
                self.add_item(item=item)

        logger.debug("1")

    def update_type(self, n: int, type_: str) -> None:
        logger.debug("0")

        hash_ = WIDGETS_LIST[4][n]
        LIST_CONFIG[hash_]["type"] = TYPES_ITEM.index(type_)
        self.update_list_config()

        logger.info("%i --> %s", n, type_)
        logger.debug("1")

    def update_list_config(self) -> None:
        logger.debug("0")

        with open(PATH_LIST_CONFIG, "w") as f:
            json.dump(LIST_CONFIG, f, indent=4)

        logger.info("list is updated")
        logger.debug("1")
