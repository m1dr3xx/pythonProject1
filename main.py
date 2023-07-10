import asyncio  # Работа с асинхронностью

from aiogram import Bot, Dispatcher
from aiogram.filters import Command  # Фильтр для /start, /...
from aiogram.types import Message  # Тип сообщения

from config import config  # Config

API_TOKEN: str = config.token

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()  # Менеджер бота


@dp.message(Command(commands=['start']))  # Берём только сообщения, являющиеся командой /start
async def start_command(message: Message):
    await message.answer("Привет!")

@dp.message (Command(commands=['help']))
async def help_command(message: Message):
    await message.answer('Чем могу быть полезен?')
@dp.message (Command(commands=['how_are_you']))
async def question_command(message: Message):
    await message.answer('Всё отлично!')
@dp.message (Command(commands=['Сколько_раз_можешь_подтянуться?']))
async def question_command(message: Message):
    await message.answer('Пока рекорд 9 раз:(')
@dp.message ()
async def echo(message: Message):
    await message.answer(message.text)
async def main():
    try:
        print('Bot Started')
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':  # Если мы запускаем конкретно этот файл.
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')