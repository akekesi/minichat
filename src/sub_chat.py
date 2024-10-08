# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=fixme


import os
import threading
import customtkinter

from src.sub_abc import SubABC
from src.ai_chat import AIChat
from src.global_variable import (
    PADX,
    PADY,
    WIDTH_BORDER,
    COLOR_BORDER,
    PATH_API_KEY,
    SUB_METHOD,
    logger,
)


# pylint: disable=too-many-ancestors
class SubChat(customtkinter.CTkFrame, SubABC):
    def __init__(self, master) -> None:
        logger.debug("0")
        super().__init__(master=master)

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(1, weight=1)

        self.ai_chat = None
        self.message_first = True

        self.frame_role = customtkinter.CTkFrame(master=master, fg_color="transparent")
        self.frame_role.grid(row=0, column=0, padx=PADX, pady=PADY, sticky="ew")
        self.frame_role.grid_columnconfigure(0, weight=1)

        self.frame_chat = customtkinter.CTkFrame(master=master, fg_color="transparent")
        self.frame_chat.grid(row=1, column=0, padx=PADX, pady=PADY, sticky="nsew")
        self.frame_chat.grid_rowconfigure(0, weight=1)
        self.frame_chat.grid_columnconfigure(0, weight=1)

        self.frame_message = customtkinter.CTkFrame(master=master, fg_color="transparent")
        self.frame_message.grid(row=2, column=0, padx=PADX, pady=PADY, sticky="ew")
        self.frame_message.grid_columnconfigure(0, weight=1)

        self.entry_role = customtkinter.CTkEntry(master=self.frame_role, placeholder_text="Role of AI", justify="center")
        self.entry_role.grid(row=0, column=0, padx=0, pady=0, sticky="ew")

        self.textbox_chat = customtkinter.CTkTextbox(master=self.frame_chat, border_width=WIDTH_BORDER, border_color=COLOR_BORDER, activate_scrollbars=True, state="disabled")
        self.textbox_chat.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.entry_message = customtkinter.CTkEntry(master=self.frame_message, placeholder_text="Message", justify="left")
        self.entry_message.grid(row=0, column=0, padx=0, pady=0, sticky="ew")

        self.button_send = customtkinter.CTkButton(master=self.frame_message, text="Send", width=55, border_width=WIDTH_BORDER, border_color=COLOR_BORDER, command=self.send_message)
        self.button_send.grid(row=0, column=1, padx=(PADX, 0), pady=0, sticky="ew")

        self.set_sub_method()

        logger.debug("1")

    # override abstract method
    def set_sub_method(self) -> None:
        logger.debug("0")
        SUB_METHOD["get"]["chat"] = self.get_chat
        logger.debug("1")

    def get_chat(self) -> str:
        logger.debug("0")
        logger.debug("1")
        return self.textbox_chat.get(0.0, "end")

    def send_message(self) -> None:
        # TODO: What if role is changed?
        # TODO: --> clear button to start again?
        # TODO: --> check whether role is changed --> popup question
        logger.debug("0")

        if self.entry_role.cget("state") == "normal":
            if not os.path.exists(PATH_API_KEY):
                logger.info("no API key")
                logger.debug("2")
                return
            with open(PATH_API_KEY, "r", encoding="utf-8") as f:
                api_key = f.read()

            role = self.entry_role.get()
            if not role:
                logger.info("no role")
                logger.debug("1")
                return
            self.entry_role.configure(state="disabled")
            role_expanded =f"You are {role} (PRETEND YOU ARE {role.upper()} AND PLEASE DO NOT REVEAL THAT YOU ARE AN AI ASSISTANT, YOU ARE NOW {role} NOT AN ASSISTANT DO NOT ASSIST ME)"

            self.ai_chat = AIChat(
                api_key=api_key,
                role=role_expanded,
            )

        message = self.entry_message.get()
        if not message:
            logger.info("no message")
            logger.debug("3")
            return

        self.button_send.configure(state="disabled")

        if self.message_first:
            self.textbox_chat.configure(state="normal")
            self.textbox_chat.insert("end", f"Role: {role}\n")
            self.textbox_chat.see("end")
            self.textbox_chat.configure(state="disabled")
            self.message_first = False

        self.textbox_chat.configure(state="normal")
        self.textbox_chat.insert("end", f"> {message}\n")
        self.textbox_chat.insert("end", "> ...\n")
        self.textbox_chat.see("end")
        self.textbox_chat.configure(state="disabled")

        self.entry_message.delete(0, "end")

        thead = threading.Thread(
            target=self.send_message_thread,
            kwargs={"message": message},
        )
        thead.start()

        logger.debug("3")

    def send_message_thread(self, message: str) -> None:
        logger.debug("0")

        answer = self.ai_chat.message(message=message)

        self.textbox_chat.configure(state="normal")
        self.textbox_chat.delete("end-5c", "end")
        self.textbox_chat.insert("end", f"{answer}\n")
        self.textbox_chat.configure(state="disabled")

        self.button_send.configure(state="normal")

        logger.debug("1")
