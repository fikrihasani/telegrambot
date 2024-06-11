import os
import telebot

from langchain_huggingface import ChatHuggingFace
from langchain_huggingface import HuggingFaceEndpoint

ACCESS_TOKEN = "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"

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    huggingfacehub_api_token=ACCESS_TOKEN,
    max_new_tokens=512,
    do_sample=False,
    repetition_penalty=1.03,
)

chat_model = ChatHuggingFace(llm=llm)
bot = telebot.TeleBot("7257981613:AAGG5XuQV3jF-H3E3PyZS1ypXHh4Zt8eCuc")

def llm_respond(message):
    return chat_model.invoke(message).content

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, llm_respond(message.text))

bot.infinity_polling()