import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from aiogram import F

from Kitoblarkeyboards import KitoblarButton
# Bot token can be obtained via https://t.me/BotFather
TOKEN = "7445150312:AAHyt5X1YroN7LSViqDBUSQg19J64iWQZy0"

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()

Kitoblar = {
    "Harry Poter":{
        "price":"100$",
        "info":"lorem ipsum dolar",
        "imgId":"AgACAgIAAxkBAAPNZnpcbpY5hHaWEeqlr3YvU_6TgDsAAv3bMRsNN9BLPQ1GxM65LRcBAAMCAANzAAM1BA"
    }
}

@dp.message(F.text == "Harry Poter")
async def harry_Handler(message : Message):
    await message.answer_photo(photo=Kitoblar["Harry Poter"]["imgId"], caption=f"kitob nomi:Harry Poter\nnarxi:{Kitoblar['Harry Poter']['price']} ")

@dp.message(F.photo)
async def rasm_handler(message : Message):
    rasmId = message.photo[0].file_id
    await message.answer(f"Id: {rasmId}")


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!" , reply_markup=KitoblarButton)


@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())