import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message, FSInputFile
from config import TOKEN
from dao.userdao import UserDAO
from answers import Answers
from keyboards import Keyboard, InlineKeyboard

dp = Dispatcher()
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

@dp.message(CommandStart())
async def command_start(message: Message) -> None:
    id_tg = message.from_user.id
    user = await UserDAO.find_one_or_none(id_tg=id_tg)
    photo = FSInputFile("/home/navruzoffd/Projects/SigmaToken/img/sigma.jpg")

    if user:
        return await message.answer(await Answers.exist_user(), reply_markup=await Keyboard.start())
    
    args = message.text.split()[1:]

    if args:

        try:
            referrer_id = int(*args)
        except:
            return await message.answer(await Answers.wrong_link())

        referrer = await UserDAO.find_one_or_none(id_tg=referrer_id)

        if not referrer:
            return await message.answer(await Answers.wrong_user())
        
        await UserDAO.add(id_tg = id_tg, username_tg = message.from_user.username,
                          invited = referrer.username_tg, balance = 100)
        
        await UserDAO.referral_reward(referrer_id)
        await message.answer_photo(photo=photo, caption=await Answers.start())
        await message.answer("\U0001F440")
        await bot.send_message(referrer_id, await Answers.msg_to_referrer(message.from_user.full_name))
        return await message.answer(
            await Answers.invited_start(message.from_user.full_name, referrer.username_tg),
            reply_markup=await Keyboard.start())
        
    
    username = message.from_user.username
    await UserDAO.add(id_tg=id_tg, username_tg=username)
    await message.answer_photo(photo=photo, caption=await Answers.start())
    await message.answer("\U0001F440", reply_markup=await Keyboard.start())

@dp.message(F.text == "Check")
async def check_subscription(message: Message):
    id_tg = message.from_user.id
    user = await UserDAO.find_one_or_none(id_tg=id_tg)

    if user.complite_tasks:
        return await message.answer("Все задания выполнены \U00002705", reply_markup=await Keyboard.start())
    
    channel = '@tetetetetetetttt'
    member = await bot.get_chat_member(channel, id_tg)

    if member.status in ['member', 'administrator', 'creator']:
        await UserDAO.task_reward(id_tg, 200)
        await message.answer("Отлично <b>200 $SIGMA</b> у вас!")
        await bot.delete_message(id_tg, user.task_msg)
        return await message.answer("\U0001F389", reply_markup=await Keyboard.start())
    
    return await message.answer("Вы не выполнили задания \U0000274C")

@dp.message(F.text == "Balance")
async def balance_info(message: Message) -> None:
    id_tg = message.from_user.id
    user = await UserDAO.find_one_or_none(id_tg=id_tg)
    return await message.answer(await Answers.balance_info(user.balance))

@dp.message(F.text == "Tasks")
async def get_tasks(message: Message):
    id_tg = message.from_user.id
    user = await UserDAO.find_one_or_none(id_tg=id_tg)

    if user.complite_tasks:
        return await message.answer("Все задания выполнены \U00002705", reply_markup=await Keyboard.start())
    
    await message.answer(await Answers.tasks(), reply_markup= await Keyboard.check_tasks())
    task_msg = await message.answer("Подпишитесь на:", reply_markup= await InlineKeyboard.tasks())
    await UserDAO.update_by_id_tg(id_tg=id_tg, task_msg=task_msg.message_id)

@dp.message(F.text == "Friends")
async def invite_friends(message: Message):
    id_tg = message.from_user.id
    user = await UserDAO.find_one_or_none(id_tg=id_tg)
    return await message.answer(await Answers.invite_friends(user.referrals, id_tg),
                                reply_markup= await InlineKeyboard.share_link(id_tg))

@dp.message(F.text == "Terms")
async def terms(message: Message):
    await message.answer("Здесь будут условия")

async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())