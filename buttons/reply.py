from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('💻Noutbuklar'),
            KeyboardButton('📱Smartfonlar'),
            KeyboardButton('⌨Keyboarda va Sichqonchalar'),
        ],
        [
            KeyboardButton('Contact', request_contact=True),
            KeyboardButton('Location', request_location=True),
        ]
    ],
    resize_keyboard=True
)