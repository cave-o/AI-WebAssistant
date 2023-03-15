# engine.py

from .key import API_KEY
import openai

openai.api_key = API_KEY

def model(request):
    prompt = request.POST.get('prompt')
    response = openai.Completion.create(
        engine='text-davinci-003',
        temperature=0.5,
        prompt=prompt,
        max_tokens=1000,
    )
    text = response.choices[0].text
    chats = {'prompt':  prompt,
                 'response': text
                }
    return chats