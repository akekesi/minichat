# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=line-too-long
# pylint: disable=invalid-name


from openai import OpenAI


class OpenAIChatGPT:

    def __init__(self, api_key: str, role: str) -> None:
        self.client = OpenAI(api_key=api_key)
        self.dialog = [
            {
                "role": "system",
                "content": role,
            }
        ]

    def message(self, message: str) -> str:
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

    # OpenAIChatGPT
    chatgpt = OpenAIChatGPT(api_key=api_key_, role=role_)
    while True:
        message_ = input("You: ")
        answer_ = chatgpt.message(message=message_)
        print(f"{person_}: {answer_}")
