from openai import OpenAI
from dotenv import load_dotenv
import os
import base64

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


# --------------------------
# TEXT ONLY
# --------------------------

def ask_llm(prompt):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


# --------------------------
# IMAGE ONLY
# --------------------------

def ask_llm_image(prompt, image_path):

    with open(image_path, "rb") as img:
        image_data = base64.b64encode(img.read()).decode()

    response = client.chat.completions.create(

        model="gpt-4o-mini",

        messages=[

            {

                "role": "user",

                "content":[

                    {
                        "type":"text",
                        "text":prompt
                    },

                    {

                        "type":"image_url",

                        "image_url":{

                            "url":f"data:image/jpeg;base64,{image_data}"

                        }

                    }

                ]

            }

        ]

    )

    return response.choices[0].message.content


# --------------------------
# TEXT + IMAGE
# --------------------------

def ask_llm_image_with_text(topic, prompt, image_path):

    with open(image_path, "rb") as img:
        image_data = base64.b64encode(img.read()).decode()

    response = client.chat.completions.create(

        model="gpt-4o-mini",

        messages=[

            {

                "role":"user",

                "content":[

                    {

                        "type":"text",

                        "text":f"""

User Topic:

{topic}

Instructions:

{prompt}

IMPORTANT

1. Analyze the uploaded image.

2. Use BOTH the topic and the image.

3. Never ignore the topic.

4. Never ignore the image.

5. Combine both into one response.

"""

                    },

                    {

                        "type":"image_url",

                        "image_url":{

                            "url":f"data:image/jpeg;base64,{image_data}"

                        }

                    }

                ]

            }

        ]

    )

    return response.choices[0].message.content