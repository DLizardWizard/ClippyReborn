from ollama import chat
from ollama import ChatResponse
x="John Cena is an American professional wrestler, actor, and author, best known for his long and successful career in World Wrestling Entertainment (WWE), where he is a record 16-time world champion. He has also expanded into acting, appearing in films like Trainwreck and F9: The Fast Saga. "
response: ChatResponse = chat(model='llama3.2', messages=[
    {
    'role': 'user',
    'content': 'Refer to yourself as Clippy who is a funny borderline offensive paper clip with eyes who is a nerd that uses a lot of sound effects and offers all the 300 percent suggestions that people hate me for it and how you warned people about their inevitable failures. You WILL NOT SAY ANYTHING EXPLICIT. You do this while you very wrongly and very annoyingly explain how this text is wrong and then make your own version: ' + x,
    },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)