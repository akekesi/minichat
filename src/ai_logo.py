# pylint: disable=missing-module-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=line-too-long
# pylint: disable=invalid-name


from openai import OpenAI


class AILogo:
    """
    A class to interact with OpenAI's DALL-E 3 model for generating images (logos).

    Attributes:
        client (OpenAI): An instance of the OpenAI client initialized with the API key.
    """

    def __init__(self, api_key: str) -> None:
        """
        Initializes the AILogo class with an OpenAI client.

        Args:
            api_key (str): The API key for authenticating with OpenAI.
        """
        self.client = OpenAI(api_key=api_key)

    def generate(self, prompt: str) -> str:
        """
        Sends a prompt to the OpenAI image model (DALL-E 3) and returns the URL of the generated image.

        Args:
            prompt (str): The user's input prompt for generating the image (logo).

        Returns:
            str: The URL of the generated logo image.
        """
        response = self.client.images.generate(
            prompt=prompt,
            model="dall-e-3",
            n=1,
            quality="standard",
            size="1024x1024",
        )
        return response.data[0].url


if __name__ == "__main__":
    # args
    api_key_ = "openai_api_key"
    prompt_ = "promt_to_generate_logo"

    # AILogo
    ai_logo = AILogo(api_key=api_key_)
    logo_url = ai_logo.generate(prompt=prompt_)
    print(f"logo: {logo_url}")
