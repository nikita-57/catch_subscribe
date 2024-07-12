from aiogram import Bot,Dispatcher,executor,types
import emoji

bot = Bot('5592227762:AAHI7sKS5UGYERnyvOOsLLArtHd4Yi7zIf4')
dp = Dispatcher(bot)

@dp.message_handler(content_types = ["new_chat_members"])
async def new_member(message):
    await bot.send_message(message.chat.id, "@" + str(message.from_user.username) + " Приветствую в нашем чате" + emoji.emojize(":wave:", language='alias'),parse_mode="html")
    
if __name__ == "__main__":
    executor.start_polling(dp)
