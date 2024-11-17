from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

BOT_TOKEN = ""

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

@dp.message_handler(commands=["start"])
async def start(message:types.Message):
    await message.answer(text="<b>Welcome to our chat bot!</b>")



if __name__ == "__main__":
    executor.start_polling(dp)
