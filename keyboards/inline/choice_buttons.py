from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import URL_APP, URL_FACEBOOK, URL_TICKET, URL_MARKET, URL_INSTAGRAM
from keyboards.inline.callback_datas import buy_callback


choice = InlineKeyboardMarkup(row_width=2)

buy_pear = InlineKeyboardButton(text="Instagram", callback_data=buy_callback.new(item_name="pear", quantity=1))
choice.insert(buy_pear)

buy_apples = InlineKeyboardButton(text="Facebook", callback_data="buy:apple:5")
choice.insert(buy_apples)

buy_cross = InlineKeyboardButton(text="Market", callback_data="buy:market:5")
choice.insert(buy_cross)

buy_ticket = InlineKeyboardButton(text="Ticket", callback_data="buy:ticket:5")
choice.insert(buy_ticket)

buy_about = InlineKeyboardButton(text="App", callback_data="buy:app:5")
choice.insert(buy_about)

cancel_button = InlineKeyboardButton(text="Cancel", callback_data="cancel")
choice.insert(cancel_button)

pear_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Visit", url=URL_INSTAGRAM)
    ]
])
apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="visit", url=URL_FACEBOOK)
    ]
])
buy_about = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="visit", url=URL_APP)
    ]
])
buy_ticket = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="visit", url=URL_TICKET)
    ]
])
buy_cross = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="visit", url=URL_MARKET)
    ]
])
