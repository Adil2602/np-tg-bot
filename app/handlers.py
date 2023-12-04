from aiogram import Router,F,Bot
from aiogram.types import Message,CallbackQuery,FSInputFile
from aiogram.filters import CommandStart
import app.keyboards as kb
from databases.request import get_product
from config import TOKEN

bot = Bot(TOKEN)

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет {message.from_user.first_name}!\nЯ бот-магазин спортивного питания.\nЧем могу помочь?', reply_markup=kb.main)

@router.message(F.text == 'Категории')
async def category(message: Message):
    await message.answer(f'Выберите категорию', reply_markup=await kb.categories())

@router.message(F.text == 'Контакты')
async def contact(message: Message):
    await message.answer(f'номер: +996 755 760 300 - Дастан\n\ninstagram: https://www.instagram.com/next_protein/\n\nпочта: Dastan@nextprotein1.com\n\nадрес: https://go.2gis.com/h4oym')


@router.callback_query(F.data.startswith('category_'))
async def category_select(callback: CallbackQuery):
    category_id = callback.data.split('_')[1]
    await callback.message.answer(f'Товары по выбранной категории', reply_markup=await kb.product(category_id=category_id))


@router.callback_query(F.data.startswith('product_'))
async def product_select(callback: CallbackQuery):
    
    product_id = callback.data.split('_')[1]
    product = await get_product(product_id=product_id)
    photo = FSInputFile(product.image)
    await bot.send_photo(callback.message.chat.id,photo,caption=f'продукт: {product.name}\n\nописание: {product.description}\n\nцена: {product.price}')

# @router.callback_query(F.data.startswith('product_'))
# async def product_delete(callback: CallbackQuery):
#     if callback.data == "delete":
#         bot.delete_message(callback.message.chat.id, callback.message.message_id-1)