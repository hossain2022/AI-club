import openai

openai.api_key = "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"

messages = []
system_msg = "you are a twitter bios write"
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready! just tell me a little bit about yourself and I will write you a twitter bio\n")
message = input()
messages.append({"role": "user", "content": message})
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages)
reply = response["choices"][0]["message"]["content"]
messages.append({"role": "assistant", "content": reply})
print("\n" + reply + "\n")
