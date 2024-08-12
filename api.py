import openai

def set_api_key(api_key):
        openai.api_key = api_key

def get_recommendations(gpt_model, persona, prompt):
    response = openai.chat.completions.create(
        model=gpt_model,
        messages=[
            {"role": "system", "content": persona},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )
    return response.choices[0].message.content.strip()