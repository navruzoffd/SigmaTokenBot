from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from answers import Answers

class Keyboard:

    @classmethod
    async def start(cls):
        button_first_row = [KeyboardButton(text="Balance"),
                            KeyboardButton(text="Friends")]
        
        button_second_row = [KeyboardButton(text="Tasks"),
                             KeyboardButton(text="Terms")]

        keyboard = ReplyKeyboardMarkup(
            keyboard=[button_first_row, button_second_row],
            resize_keyboard=True
            )
        return keyboard
    
    @classmethod
    async def check_tasks(cls):
        button_row = [KeyboardButton(text="Check")]
        keyboard = ReplyKeyboardMarkup(keyboard=[button_row], resize_keyboard=True)
        return keyboard
    
class InlineKeyboard:

    @classmethod
    async def tasks(cls):
        button = InlineKeyboardButton(text="Канал", url="https://t.me/tetetetetetetttt")
        keyboard = InlineKeyboardMarkup(inline_keyboard = [[button]])
        return keyboard
    
    @classmethod
    async def share_link(cls, id_tg):
        button = InlineKeyboardButton(text="Пригласить друзей",
                                      switch_inline_query=await Answers.share_link(id_tg))
        keyboard = InlineKeyboardMarkup(inline_keyboard=[[button]])
        return keyboard