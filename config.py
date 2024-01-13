from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


Token = '6287271678:AAExNrndVKCbQUPtJWQpY_h4QGydYo2_-gg'
bot = Bot(token=Token)
dp = Dispatcher(bot, storage=MemoryStorage())