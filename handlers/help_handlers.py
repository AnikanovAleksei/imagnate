from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

HELP_COMMAND = """
/start - начало работы
/help - список команд
/contact - связь с менеджером
/website - сайт iMagnate
"""

router = Router()


# Обработка команды /help
@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(text=HELP_COMMAND)
