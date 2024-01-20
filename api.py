import openai

def set_api_key(api_key):
        openai.api_key = api_key

def get_recommendations(prompt):
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=300
        )
        return response.choices[0].text.strip()