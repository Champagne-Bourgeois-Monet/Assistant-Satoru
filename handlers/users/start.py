import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import command_callback
from keyboards.inline.start_buutons import mian_keyboard
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if message.from_user.language_code == "ru":
        await message.answer(f'Привет, {message.from_user.full_name}!', reply_markup=mian_keyboard)
    elif message.from_user.language_code == "kz":
        await message.answer(f'Сәлем, {message.from_user.full_name}!', reply_markup=mian_keyboard)
    else:
        await message.answer(f'Hello, {message.from_user.full_name}!', reply_markup=mian_keyboard)


@dp.callback_query_handler(command_callback.filter(name_command="start"))
async def menu_command_start(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"callback_data = {call.data}")
    logging.info(f"callback_data dict = {callback_data}")
    arguments = callback_data.get("arguments")

    if arguments == "":
        await call.message.answer(f"Какая то там реакция из за нажатия кнопки: {arguments}")
    else:
        await call.message.answer(f"Какая то там реакция из за нажатия кнопки: {arguments}")
