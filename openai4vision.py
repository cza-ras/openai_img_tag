from openai import OpenAI
import yaml

class openai4vision():

    def tag_image(image_url):

        #get secrets
        with open('Projects/img_tagging/secrets.yaml', 'r') as secrets:
            secrets_keys = yaml.safe_load(secrets)
        apikey = secrets_keys['openai']['apikey']

        #init openai
        client = OpenAI(api_key=apikey)
        prompt = "Describe the contents of the following image in five key phrases separated by commas."

        # Use the OpenAI API to extract image topics
        response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {
                "type": "image_url",
                "image_url": {
                    "url": image_url,
                },
                },
            ],
            }
        ],
        max_tokens=300,
        )

        print(response.choices[0])