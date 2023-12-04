from aiogram import Bot,Dispatcher
import asyncio,logging,sys
from app.handlers import router
from databases.models import async_main
from config import TOKEN
import asyncio
from aiogram import F


async def main():
    
    await async_main()

    bot = Bot(token = TOKEN)
    dp = Dispatcher()
    dp.include_router(router=router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level = logging.INFO, stream = sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')