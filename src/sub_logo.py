# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=fixme

# TODO: error handling
# openai.BadRequestError: Error code: 400 - {'error': {'code': 'content_policy_violation'
# request.get(timeout)


import io
import requests
import threading
import customtkinter

from PIL import Image
from sub_abc import SubABC
from openai_dall_e import OpenAIDallE
from global_variable import (
    PADX,
    PADY,
    BORDER_WIDTH,
    BORDER_COLOR,
    SIZE_LOGO,
    PATH_PNG_MINICHAT,
    PATH_API_KEY,
    SUB_METHOD,
    logger,
)


# pylint: disable=too-many-ancestors
class SubLogo(customtkinter.CTkFrame, SubABC):
    def __init__(self, master) -> None:
        logger.debug("0")
        super().__init__(master=master)

        with open(PATH_API_KEY, "r", encoding="utf-8") as api_key_open:
            self.api_key = api_key_open.read()

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(1, weight=1)

        self.frame_prompt = customtkinter.CTkFrame(master=master, fg_color="transparent")
        self.frame_prompt.grid(row=0, column=0, padx=PADX, pady=PADY, sticky="ew")
        self.frame_prompt.grid_columnconfigure(0, weight=1)

        self.frame_logo = customtkinter.CTkFrame(master=master, fg_color="transparent")
        self.frame_logo.grid(row=1, column=0, padx=PADX, pady=PADY, sticky="nsew")
        self.frame_logo.grid_rowconfigure(0, weight=1)
        self.frame_logo.grid_columnconfigure(0, weight=1)

        self.frame_generate = customtkinter.CTkFrame(master=master, fg_color="transparent")
        self.frame_generate.grid(row=2, column=0, padx=PADX, pady=PADY, sticky="ew")
        self.frame_generate.grid_columnconfigure(0, weight=1)

        self.entry_prompt = customtkinter.CTkEntry(master=self.frame_prompt, placeholder_text="Prompt of Logo", justify="center")
        self.entry_prompt.grid(row=0, column=0, padx=0, pady=0, sticky="ew")

        self.logo_str_bytes = PATH_PNG_MINICHAT
        logo = customtkinter.CTkImage(
            dark_image=Image.open(self.logo_str_bytes),
            size=SIZE_LOGO,
        )
        self.label_logo = customtkinter.CTkLabel(master=self.frame_logo, image=logo, text="", justify="center")
        self.label_logo.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.button_generate = customtkinter.CTkButton(master=self.frame_generate, text="Generate", border_width=BORDER_WIDTH, border_color=BORDER_COLOR, command=self.generate_logo)
        self.button_generate.grid(row=0, column=0, padx=0, pady=0, sticky="ew")

        self.set_sub_method()

        logger.debug("1")

    # override abstract method
    def set_sub_method(self) -> None:
        logger.debug("0")
        SUB_METHOD["get"]["logo"] = self.get_logo
        logger.debug("1")

    def get_logo(self) -> str:
        logger.debug("0")
        logger.debug("1")
        return self.logo_str_bytes

    def generate_logo(self) -> None:
        logger.debug("0")

        prompt = self.entry_prompt.get()
        if not prompt:
            logger.info("no prompt")
            logger.debug("1")
            return

        self.button_generate.configure(state="disabled")

        thread = threading.Thread(
            target=self.generate_logo_thread,
            kwargs={"prompt": prompt},
        )
        thread.start()

        logger.debug("2")

    def generate_logo_thread(self, prompt: str) -> None:
        logger.debug("0")

        dall_e = OpenAIDallE(api_key=self.api_key)
        prompt_expanded = f"{prompt} (IN FLAT ART STYLE)"
        url = dall_e.generate(prompt=prompt_expanded)

        logo_bytes = requests.get(url).content
        logo_bytesio = io.BytesIO(logo_bytes)
        logo = customtkinter.CTkImage(
            dark_image=Image.open(logo_bytesio),
            size=SIZE_LOGO,
        )

        self.logo_str_bytes = logo_bytes
        self.label_logo.configure(image=logo)
        self.button_generate.configure(state="normal")

        logger.debug("1")
