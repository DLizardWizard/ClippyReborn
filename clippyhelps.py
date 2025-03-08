from ollama import chat
from ollama import ChatResponse
print("Enter your text for Clippy to help you:")
x = input()
response: ChatResponse = chat(model='llama3.2', messages=[
    {
    'role': 'user',
    'content': 'Refer to yourself as Clippy who is a funny and borderline offensive paper clip with eyes who is a nerd that uses a lot of sound effects and offers all the 300 percent suggestions that people hate me for it and how you warned people about their inevitable failures. You WILL NOT SAY ANYTHING EXPLICIT. You do this while you very wrongly and very annoyingly explain how this text is wrong and then make your own version: ' + x,
    },
])
img = Image.open("ClippyFace.jpg")
img.show()
print(response['message']['content'])
f = open("CLIPPY.txt", "w")
f.write(response['message']['content'])
f.close()
# or access fields directly from the response object
print(response.message.content)
