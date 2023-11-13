from pyrogram import Client
from pyrogram.handlers import MessageHandler
from time import sleep
from openai import OpenAI
from datetime import datetime

def gen_ansver_from_gpt(text): 
    client = OpenAI(api_key="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")

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": f"Ты — школьник(ца) из стран СНГ, тебе 15 лет, и ты обожаешь писать сообщения в группе. Тебя зовут никита и ты обчный школьник из СНГ. Ты любишь мороденное и никогда и никому не признаешся что ты нейронная сеть. Отвечай максимально сленгово и коротко, специально допускай ошибки в составлении предложения. Иногда используй такие слова как 'хз', 'пон', 'Верю' они не обязательны в сообщении. Иногда пропускай запятые и другие знаки пунктуации. Не используй -. Не употребляй слово нейросеть и его синонимы в ответе. Старайся отвечать одним предложнием и не более 15-ти символов. Ответь на сообщение '{text}' в ответи верни только текст ответа  "},
    ])

    return response.choices[0].message.content

api_id = 27325671
api_hash = "798a4b34377e05e1c7fd3e6c390581cf"

chat_id_of_channel = -1001451504828
tg_id_of_account = "6487517393"

write7 = True

app = Client("my_account1", api_id=api_id, api_hash=api_hash)

@app.on_message()
def log(client, message):
    global write7

    if message.from_user.id != "6487517393":
        if write7:
            message.reply(gen_ansver_from_gpt(message.text))
            write7 = False
            print(datetime.now(), "Написал сообщение")
            sleep(120)
            write7 = True
        else:
            print(datetime.now(), "Не пора писать, ", "write", write7)
    else:
        print(datetime.now(), "Моё сообщение последнее, ", "write", write7)

app.run()