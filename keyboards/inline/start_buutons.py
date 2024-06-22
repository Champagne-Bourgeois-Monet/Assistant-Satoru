from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import command_callback

name_it_is_command = "start"

name_button = {
    "Name #1": "Что то. #1",
    "Name #2": "Что то. #2",
    "Name #3": "Что то. #3",
}

arguments_button = {
    "Arguments #1": "Что то. #1",
    "Arguments #2": "Что то. #2",
    "Arguments #3": "Что то. #3",
}

element_inline_keyboard = []

for i in range(1, len(name_button) + 1):
    element_inline_keyboard.append([InlineKeyboardButton(
        text=f"{name_button[f"Name #{i}"]}",
        callback_data=command_callback.new(name_command=f"{name_it_is_command}",
                                           arguments=f"{arguments_button[f"Arguments #{i}"]}")
    )])

mian_keyboard = InlineKeyboardMarkup(row_width=2, inline_keyboard=element_inline_keyboard)