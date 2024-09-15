import os
import customtkinter

from PIL import Image
from logger_config import logger
from global_variable import SUB_METHOD


# TODO: put these (inc. padx/y, border_width...) into a separate file for global variable
# TODO: add abstract class for set_sub_method
SIZE_LOGO = (256, 256)
PATH_LOGO = os.path.join(os.path.dirname(__file__), "..", "png")
PATH_LOGO_DEFAULT = os.path.join(PATH_LOGO, "minichat.png")


class SubLogo(customtkinter.CTkFrame):
    def __init__(self, master):
        logger.debug("0")
        super().__init__(master=master)

        self.message_first = True

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(1, weight=1)

        self.frame_prompt = customtkinter.CTkFrame(master=master, fg_color="transparent")
        self.frame_prompt.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.frame_prompt.grid_columnconfigure(0, weight=1)

        self.frame_logo = customtkinter.CTkFrame(master=master, fg_color="transparent")
        self.frame_logo.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.frame_logo.grid_rowconfigure(0, weight=1)
        self.frame_logo.grid_columnconfigure(0, weight=1)

        self.frame_generate = customtkinter.CTkFrame(master=master, fg_color="transparent")
        self.frame_generate.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        self.frame_generate.grid_columnconfigure(0, weight=1)

        self.entry_prompt = customtkinter.CTkEntry(master=self.frame_prompt, placeholder_text="Prompt of Logo", justify="center")
        self.entry_prompt.grid(row=0, column=0, padx=0, pady=0, sticky="ew")

        self.path_logo = PATH_LOGO_DEFAULT
        logo = customtkinter.CTkImage(
            dark_image=Image.open(self.path_logo),
            size=SIZE_LOGO
        )

        self.label_logo = customtkinter.CTkLabel(master=self.frame_logo, image=logo, text="", justify="center")
        self.label_logo.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.button_generate = customtkinter.CTkButton(master=self.frame_generate, text="Generate", border_width=2, border_color="gray30", command=self.generate_logo)
        self.button_generate.grid(row=0, column=0, padx=0, pady=0, sticky="ew")

        self.set_sub_method()

        logger.debug("1")

    def set_sub_method(self) -> None:
        logger.debug("0")
        SUB_METHOD["get"]["logo"] = self.get_logo
        logger.debug("1")

    def get_logo(self) -> str:
        logger.debug("0")
        logger.debug("1")
        return self.path_logo

    def generate_logo(self) -> None:
        logger.debug("0")

        prompt = self.entry_prompt.get()
        if not prompt:
            logger.info("no prompt")
            logger.debug("1")
            return

        # TODO: thread for AI
        logger.debug("2")
