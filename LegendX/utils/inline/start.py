from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from LegendX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ð¥º á´á´á´ á´á´ á´á´ Êá´á´Ê É¢Êá´á´á´© ð¥º",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="â¨Êá´Êá´©â¨",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="â¨sá´á´á´ÉªÉ´É¢sâ¨", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="âå½¡[á´á´á´ á´Êá´á´á´Ê]å½¡â", user_id=OWNER),
            InlineKeyboardButton(
                text="ððððððð", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ð¥º á´á´á´ á´á´ á´Êsá´ Êá´á´ É¢á´Ê ð¥º",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="â¨Êá´Êá´©â¨", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="âå½¡[á´á´á´ á´Êá´á´á´Ê]å½¡â", user_id=OWNER),
            InlineKeyboardButton(
                text="ððððððð", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                    text="ðð ð¦ð£ðð ðð ðð", url=f"{config.UPSTREAM_REPO}"
                )
        ],
     ]
    return buttons
