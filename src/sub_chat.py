import customtkinter

from logger_config import logger


# TODO: put padx/y, border_width... into a separate file for global variable
class SubChat(customtkinter.CTkFrame):
    def __init__(self, master):
        logger.debug("0")
        super().__init__(master=master)

        self.message_first = True

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(1, weight=1)

        self.frame_role = customtkinter.CTkFrame(master=master, fg_color="transparent")
        self.frame_role.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.frame_role.grid_columnconfigure(0, weight=1)

        self.frame_chat = customtkinter.CTkFrame(master=master, fg_color="transparent")
        self.frame_chat.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.frame_chat.grid_rowconfigure(0, weight=1)
        self.frame_chat.grid_columnconfigure(0, weight=1)

        self.frame_message = customtkinter.CTkFrame(master=master, fg_color="transparent")
        self.frame_message.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        self.frame_message.grid_columnconfigure(0, weight=1)

        self.entry_role = customtkinter.CTkEntry(master=self.frame_role, placeholder_text="Role of AI", justify="center")
        self.entry_role.grid(row=0, column=0, padx=0, pady=0, sticky="ew")

        self.textbox_chat = customtkinter.CTkTextbox(master=self.frame_chat, border_width=2, border_color="gray30", activate_scrollbars=True, state="disabled")
        self.textbox_chat.grid(row=0, column=0, sticky="nsew")

        self.entry_message = customtkinter.CTkEntry(master=self.frame_message, placeholder_text="Message", justify="left")
        self.entry_message.grid(row=0, column=0, padx=0, pady=0, sticky="ew")

        self.button_send = customtkinter.CTkButton(master=self.frame_message, text="Send", width=55, border_width=2, border_color="gray30", command=self.send_message)
        self.button_send.grid(row=0, column=1, padx=(10, 0), pady=0, sticky="ew")

        logger.debug("1")

    def send_message(self, event=None) -> None:
        # TODO: What if role is changed?
        # TODO: --> clear button to strart again?
        # TODO: --> check whether role is changed --> popup question
        logger.debug("0")

        role = self.entry_role.get()
        if not role:
            logger.info("no role")
            logger.debug("1")
            return
        self.entry_role.configure(state="disabled")

        message = self.entry_message.get()
        if not message:
            logger.info("no message")
            logger.debug("2")
            return

        if self.message_first:
            self.textbox_chat.configure(state="normal")
            self.textbox_chat.insert("end", f"Role: {role}\n")
            self.textbox_chat.see("end")
            self.textbox_chat.configure(state="disabled")
            self.message_first = False

        self.textbox_chat.configure(state="normal")
        self.textbox_chat.insert("end", f"> {message}\n")
        self.textbox_chat.insert("end", f"> Here comes the answer of AI.\n")
        self.textbox_chat.see("end")
        self.textbox_chat.configure(state="disabled")
        self.entry_message.delete(0, "end")

        # TODO: thread for AI
        logger.debug("3")
