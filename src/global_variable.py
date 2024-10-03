# pylint: disable=line-too-long
# pylint: disable=fixme

"""
Global Variables for MiniChat GUI Application

This module contains global constants, file paths, and configurations for the MiniChat GUI project. 
It includes parameters for window sizes, color schemes, widget settings, and logging setup. 
These variables are used throughout the application to maintain consistency and manage resources.

Attributes:
    NAME (str): The name of the application.
    PADX (int): Horizontal padding for widgets.
    PADY (int): Vertical padding for widgets.
    WIDTH_BORDER (int): Border width for frames and widgets.
    COLOR_* (str): Color settings for various UI components.
    SIZE_* (dict/tuple): Size configurations for different windows and logo elements.
    PATH_* (str): File paths to various resources like icons, logs, and API keys.
    URL_OPENAI (str): URL to OpenAI's website.
    LIST_CONFIG (dict): Configuration loaded from 'list_config.json' file.
    WIDGETS_LIST (list): Lists used to manage different UI elements like labels, entries, comboboxes, and buttons.
    TYPES_ITEM (list): Types of items available in the application (e.g., "private", "public").
    SUB_METHOD (dict): Dictionary to store subscription methods for chat and logo features.
    logger (Logger): Configured logger for the application.
"""

import os
import json
import logging

from src.logger_config import Logging


NAME = "MiniChat"

PADX = 10
PADY = 10

WIDTH_BORDER = 2

COLOR_FRAME = "gray17"
COLOR_BORDER = "gray30"
COLOR_INFO = "gray40"
COLOR_OK = "#007d00"
COLOR_OK_HOVER = "#005700"
COLOR_NOK = "#b30000"
COLOR_NOK_HOVER = "#7d0000"

SIZE_MINICHAT = {
    "width": 450,
    "height": 550,
}
SIZE_OPEN_ITEM = {
    "width": 450,
    "height": 550,
}
SIZE_LOGO = (256, 256)
SIZE_LOGO_LIST = (25, 25)

PATH_ICO = os.path.join(os.path.dirname(__file__), "..", "ico")         # TODO: check existence & logger
PATH_ICO_MINICHAT = os.path.join(PATH_ICO, "minichat.ico")              # TODO: check existence & logger
PATH_LIST = os.path.join(os.path.dirname(__file__), "..", "list")       # TODO: check existence & logger
PATH_LIST_CONFIG = os.path.join(PATH_LIST, "list_config.json")          # TODO: check existence & logger
PATH_LOG = os.path.join(os.path.dirname(__file__), "..", "log")         # TODO: check existence & logger
PATH_PNG = os.path.join(os.path.dirname(__file__), "..", "png")         # TODO: check existence & logger
PATH_PNG_MINICHAT = os.path.join(PATH_PNG, "minichat.png")              # TODO: check existence & logger
PATH_API_KEY = os.path.join(os.path.dirname(__file__), "..", "api.key") # TODO: check existence & logger

URL_OPENAI = "https://openai.com/"

with open(PATH_LIST_CONFIG, "r", encoding="utf-8") as f:                # TODO: try/except & logger
    LIST_CONFIG = json.load(f)

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

SUB_METHOD = {
    "get": {
        "chat": None,
        "logo": None,
    },
}

# set logger up
logger = Logging().set_logger(
    name=NAME,
    level=logging.DEBUG,
    path_dir=PATH_LOG,
)
