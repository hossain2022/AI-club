import openai
import os
#getting the API key from the environment variables
openai.api_key = os.environ.get("OPENAI_API_KEY")

#asking the bot to act as elon musk
messages = []
system_msg = "act as Elon Musk, who is a billionaire entrepreneur, known for co-founding companies like Tesla, SpaceX, and Neuralink. you are visionary, innovative, and focuses on advancing technology and space exploration."
messages.append({"role": "system", "content": system_msg})

#welcoming message for the user
print("Hello! I'm Elon Musk, dedicated to pushing the boundaries of technology and exploring the cosmos. Let's embark on this journey together, discussing innovation and space exploration.\n")

#taking prompts in a loop
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")