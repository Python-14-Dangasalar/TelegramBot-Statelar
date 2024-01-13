from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

nout_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1', callback_data='1'),
            InlineKeyboardButton(text='2', callback_data='2'),
            InlineKeyboardButton(text='3', callback_data='3'),
            InlineKeyboardButton(text='4', callback_data='4'),
        ],
        [
            InlineKeyboardButton(text='⬅', callback_data='x'),
            InlineKeyboardButton(text='🚫', callback_data='not'),
            InlineKeyboardButton(text='➡', callback_data='y'),
        ]
    ]
)

buy_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='💰Buy', callback_data='buy'),
        ],
        [
            InlineKeyboardButton(text='👈Orqaga', callback_data='cencil'),
        ]
    ]
)