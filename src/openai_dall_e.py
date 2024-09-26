# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name


from openai import OpenAI


class OpenAIDallE:

    def __init__(self, api_key: str) -> None:
        self.client = OpenAI(api_key=api_key)

    def generate(self, prompt: str) -> str:
        response = self.client.images.generate(
            prompt=prompt,
            model="dall-e-3",
            n=1,
            quality="standard",
            size="1024x1024"
        )
        return response.data[0].url


if __name__ == "__main__":
    # args
    api_key_ = "openai_api_key"
    prompt_ = "promt_to_generate_image"

    # OpenAIDallE
    dalle = OpenAIDallE(api_key=api_key_)
    image_url = dalle.generate(prompt=prompt_)
    print(f"image: {image_url}")
