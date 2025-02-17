from aiogram import Dispatcher, Bot
import asyncio
import os
from dotenv import load_dotenv
from handlers.user_register import router as user_router
from handlers.handlers import router as handlers_router
from database.models import async_main
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from database import requests as rq
from aiogram.types import FSInputFile


scheduler = AsyncIOScheduler(timezone="Europe/Moscow")


async def send_scheduled_message(bot: Bot):
    users = await rq.get_all_users()
    message_text = "Слух: Apple Intelligence придёт на Apple Vision Pro вместе с новым иммерсивным контентом."
    image_path = '/root/imagnate/images/IMG_1262.JPG'  # Укажите путь к вашему изображению

    # Используем InputFile для отправки изображения
    photo = FSInputFile(image_path)

    for user in users:
        if user.telegram_id:
            try:
                # Отправка фото с подписью
                await bot.send_photo(chat_id=user.telegram_id, photo=photo, caption=message_text)
            except Exception as e:
                print(f"Failed to send message to user {user.telegram_id}: {e}")


async def main():
    load_dotenv()
    await async_main()
    bot = Bot(token=os.getenv('TOKEN_ID'))

    dp = Dispatcher()
    dp.include_router(user_router)
    dp.include_router(handlers_router)

    # Проверка на существование задачи перед добавлением
    if not scheduler.get_job("daily_post"):
        # Настройка планировщика для выполнения задачи в 14:00
        scheduler.add_job(send_scheduled_message, 'cron', hour=17, minute=35, args=[bot], id="daily_post")

    # Запуск планировщика
    scheduler.start()

    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
