# pylint: disable=missing-module-docstring
# pylint: disable=fixme


import os
import json
import logging

from logger_config import Logging


NAME = "MiniChat"

PADX = 10
PADY = 10
BORDER_WIDTH = 2
BORDER_COLOR = "gray30"

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

PATH_ICO = os.path.join(os.path.dirname(__file__), "..", "ico")     # TODO: check existence & logger
PATH_ICO_MINICHAT = os.path.join(PATH_ICO, "minichat.ico")          # TODO: check existence & logger
PATH_LIST = os.path.join(os.path.dirname(__file__), "..", "list")   # TODO: check existence & logger
PATH_LIST_CONFIG = os.path.join(PATH_LIST, "list_config.json")      # TODO: check existence & logger
PATH_LOG = os.path.join(os.path.dirname(__file__), "..", "log")     # TODO: check existence & logger
PATH_PNG = os.path.join(os.path.dirname(__file__), "..", "png")     # TODO: check existence & logger
PATH_PNG_MINICHAT = os.path.join(PATH_PNG, "minichat.png")          # TODO: check existence & logger

with open(PATH_LIST_CONFIG, 'r', encoding="utf-8") as f:            # TODO: try/except & logger
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
    path_dir=PATH_LOG
)
