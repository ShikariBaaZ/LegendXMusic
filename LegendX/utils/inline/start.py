from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from LegendX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥺 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ 🥺",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✨ʜᴇʟᴩ✨",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="✨sᴇᴛᴛɪɴɢs✨", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="★彡[ᴅᴇᴠᴇʟᴏᴘᴇʀ]彡★", user_id=OWNER),
            InlineKeyboardButton(
                text="𝓈𝓊𝓅𝓅𝑜𝓇𝓉", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥺 ᴀᴅᴅ ᴍᴇ ᴇʟsᴇ ʏᴏᴜ ɢᴇʏ 🥺",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="✨ʜᴇʟᴩ✨", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="★彡[ᴅᴇᴠᴇʟᴏᴘᴇʀ]彡★", user_id=OWNER),
            InlineKeyboardButton(
                text="𝓈𝓊𝓅𝓅𝑜𝓇𝓉", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                    text="𝕊𝕠𝕦𝕣𝕔𝕖 𝕔𝕠𝕕𝕖", url=f"{config.UPSTREAM_REPO}"
                )
        ],
     ]
    return buttons
