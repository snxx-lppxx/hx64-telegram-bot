#!/usr/bin/env python3
# -*- encoding: utf8 -*-
#
# https://t.me/hx64bot
import asyncio

from aiogram import Bot, Dispatcher, types, executor

API_TOKEN='TOKEN'
bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)

@dp.message_handler(commands=['creator'])
async def send_welcome(message: types.Message):
	await bot.send_message(message.chat.id, 
		'Developer:' + \
		'[snxx](tg://user?id=1186345584)!', 
		parse_mode='markdown'
	)
if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)
