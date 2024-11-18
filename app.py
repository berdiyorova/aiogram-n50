from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.utils import executor

from file_manager import user_manager
from keyboards import menu_keyboard, get_users_keyboards

BOT_TOKEN = "7889811891:AAGgP2ZhtNzAvuzK5jA6nB0iJ-n-8WJ6fGA"

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(
        text=f"<b>👨🏻‍💻 Hello, {message.from_user.full_name}!</b>  Welcome to our chat bot!",
        reply_markup=menu_keyboard
    )
    data = [message.chat.id, message.from_user.username, message.from_user.full_name]
    user_manager.add_data(data=data)


@dp.message_handler(text=["📤 Send Message"])
async def select_user(message: types.Message, state: FSMContext):
    await state.set_state('send-message')
    users = user_manager.read_data()
    users_keyboards = await get_users_keyboards(users)

    await message.answer(
        text="Select the user you want to send a message to",
        reply_markup=users_keyboards
    )


@dp.callback_query_handler(state='send-message')
async def send_message(call: types.CallbackQuery, state: FSMContext):
    user_id = call.data.split(' ')[0]
    username = call.data.split(' ')[1]
    await state.update_data(user_id=user_id)
    await call.answer(f"Enter the message you want to send to {username}", show_alert=True)
    await state.set_state('get-message')



@dp.message_handler(state=["get-message"])
async def get_message(message: types.Message, state: FSMContext):
    data = await state.get_data()
    print(data)
    user_id = data['user_id']
    await bot.send_message(chat_id=user_id, text=message.text)
    await state.finish()



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
