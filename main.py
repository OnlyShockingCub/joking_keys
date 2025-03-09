from pynput import keyboard
from openai import OpenAI

API_KEY = 'ENTER API HERE'

client = OpenAI(api_key=API_KEY)

def generate_text(prompt, model="gpt-3.5-turbo", max_tokens=100, temperature=0.7):
    try:
        response = client.chat.completions.create(model=model,
                                                  messages=[{"role": "user", "content": prompt}],
                                                  max_tokens=max_tokens,
                                                  temperature=temperature)
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {e}"

def on_press(key):
    try:
        key_name = key.char
    except AttributeError:
        key_name = str(key)

    prompt = f"Tell a funny joke about the '{key_name}' key."
    joke = generate_text(prompt)

    print(joke)

def start_key_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start_key_listener()
