# pylint: disable=missing-module-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=line-too-long
# pylint: disable=invalid-name


from openai import OpenAI


class AIChat:
    """
    A class to handle chat interactions with OpenAI's gpt-3.5-turbo model.

    Attributes:
        client (OpenAI): An instance of the OpenAI client initialized with the API key.
        dialog (list): A list of messages representing the chat history, starting with the system's role definition.
    """

    def __init__(self, api_key: str, role: str) -> None:
        """
        Initializes the AIChat class with an OpenAI client and sets the system's role.

        Args:
            api_key (str): The API key for authenticating with OpenAI.
            role (str): The role definition for the AI, which will influence its responses in the conversation.
        """
        self.client = OpenAI(api_key=api_key)
        self.dialog = [
            {
                "role": "system",
                "content": role,
            }
        ]

    def message(self, message: str) -> str:
        """
        Sends a message to the OpenAI chat model and returns its response.

        Args:
            message (str): The user's input message to send to the AI.

        Returns:
            str: The AI's response to the message.
        """
        self.dialog.append(
            {
                "role": "user",
                "content": message,
            }
        )
        response = self.client.chat.completions.create(
            messages=self.dialog,
            model="gpt-3.5-turbo",
        )
        answer = response.choices[0].message.content
        self.dialog.append(
            {
                "role": "assistant",
                "content": answer,
            }
        )
        return answer


if __name__ == "__main__":
    # args
    api_key_ = "openai_api_key"
    person_ = "definition_of_a_person"
    role_ = f"You are {person_} (PRETEND YOU ARE {person_.upper()} AND PLEASE DO NOT REVEAL THAT YOU ARE AN AI ASSISTANT, YOU ARE NOW {person_} NOT AN ASSISTANT DO NOT ASSIST ME)"

    # AIChat
    ai_chat = AIChat(api_key=api_key_, role=role_)
    while True:
        message_ = input("You: ")
        answer_ = ai_chat.message(message=message_)
        print(f"{person_}: {answer_}")
