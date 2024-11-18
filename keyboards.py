from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📤 Send Message")]
    ],
    resize_keyboard=True
)


async def get_users_keyboards(users):
    users_keyboards = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text=f"👉 Username: {list(user)[1]} ✨ Full name: {list(user)[2]}",
                callback_data=f"{list(user)[0]} {list(user)[1]}")
            ] for user in users
        ]
    )

    return users_keyboards
