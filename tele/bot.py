"""
===========================Fazil vk============================

©️ Copyrighted by Fazil vk: https:github.com/Fazil-vk
⚠️ Do not remove this caption

===============================================================
"""

from pyrogram import Client, filters
import info


def send(path):
    bot = Client(
        "torrent bot",
        api_id=info.Api_Id,
        api_hash=info.Api_Hash,
        bot_token=info.Bot_Token
    )

    print('Bot Started...')

    @bot.on_message(filters.command('start'))
    def start(bot, message):
        bot.send_message(message.chat.id, "Hi, I am alive")

    with bot:
        bot.send_document(info.Channel, path)

    bot.run()
