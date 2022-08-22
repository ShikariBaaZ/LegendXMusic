import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from LegendX import LOGGER, app, userbot
from LegendX.core.call import Legend
from LegendX.plugins import ALL_MODULES
from LegendX.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("LegendX").error(
            "WTF Baby ! Atleast add a pyrogram string, How Cheap..."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("LegendX").warning(
            "Spotify Client Id & Secret not added, Chutiya Saala ek itni simple cheej nahi laa paaya."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("LegendX.plugins" + all_module)
    LOGGER("LegendX.plugins").info(
        "Necessary Modules Imported Successfully."
    )
    await userbot.start()
    await Legend.start()
    try:
        await Legend.stream_call(
            "https://telegra.ph/file/8d5db123638c2f6bb6ce4.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("LegendX").error(
            "[ERROR] - \n\nHey Baby, firstly open telegram and turn on voice chat in Logger Group else fu*k off. If you ever ended voice chat in log group i will stop working and users will fu*k you up."
        )
        sys.exit()
    except:
        pass
    await Legend.decorators()
    LOGGER("LegendX").info("Music Bot Started Successfully, For any issue Contact us at @ShikariSupportNetwork")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("LegendX").info("Stopping Music Bot, Dur Ho jao meri aankho se (Mai naraj hu)")
