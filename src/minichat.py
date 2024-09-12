import os
import customtkinter


from logger_config import logger

# TODO: put these into a separate file for global variable
SIZE = {
    "width": 450,
    "height": 550,
}
PATH_ICON = os.path.join(os.path.dirname(__file__), "..", "ico", "icon.ico")
TABS = [
    "Chat",
    "Logo",
    "Docs"
]


class MiniChat(customtkinter.CTk):
    def __init__(self):
        logger.debug(msg="0")
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
            # segmented_button_selected_color=,
            # segmented_button_selected_hover_color=,
            segmented_button_unselected_color="gray30",
            # segmented_button_unselected_hover_color=,
            border_color="gray30",
            border_width=2,
            command=self.click_tab,
        )
        self.tabview.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        for tab in TABS:
            self.tabview.add(name=tab)
        self.tab_current = TABS[0]
        self.click_tab()
        logger.debug(msg="1")

    def click_tab(self):
        logger.debug(msg="0")
        logger.debug(msg="1")


if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    minichat = MiniChat()
    minichat.mainloop()
