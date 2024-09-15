import os
import customtkinter

from PIL import Image
from logger_config import logger


# TODO: put these (inc. padx/y, border_width...) into a separate file for global variable
PATH_IMAGE = os.path.join(os.path.dirname(__file__), "..", "png")
PATH_IMAGE_DEFAULT = os.path.join(PATH_IMAGE, "image_default.png")


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

        self.frame_image = customtkinter.CTkFrame(master=master, fg_color="transparent")
        self.frame_image.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.frame_image.grid_rowconfigure(0, weight=1)
        self.frame_image.grid_columnconfigure(0, weight=1)

        self.frame_generate = customtkinter.CTkFrame(master=master, fg_color="transparent")
        self.frame_generate.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        self.frame_generate.grid_columnconfigure(0, weight=1)

        self.entry_prompt = customtkinter.CTkEntry(master=self.frame_prompt, placeholder_text="Prompt of Logo", justify="center")
        self.entry_prompt.grid(row=0, column=0, padx=0, pady=0, sticky="ew")

        image = customtkinter.CTkImage(
            dark_image=Image.open(PATH_IMAGE_DEFAULT),
            size=(256, 256)
        )

        self.label_image = customtkinter.CTkLabel(master=self.frame_image, image=image, text="", justify="center")
        self.label_image.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.button_generate = customtkinter.CTkButton(master=self.frame_generate, text="Generate", border_width=2, border_color="gray30", command=self.generate_image)
        self.button_generate.grid(row=0, column=0, padx=0, pady=0, sticky="ew")

        logger.debug("1")

    def generate_image(self) -> None:
        logger.debug("0")

        prompt = self.entry_prompt.get()
        if not prompt:
            logger.info("no prompt")
            logger.debug("1")
            return

        # TODO: thread for AI
        logger.debug("2")
