from telethon import __version__, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


START_BUTTON = [
    [
        Button.inline("• 𝐂𝐎𝐌𝐌𝐀𝐍𝐃 •", data="help_back")
    ],
    [
        Button.url("• 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 •", "https://t.me/monster_discussion"),
        Button.url("• 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 •", "https://t.me/monster_king_is_here")
    ],
    [
        Button.url("• 𝐎𝐖𝐍𝐄𝐑 •", "https://t.me/MONSTER_TERA_BAAP1")
    ],
    [ 
        Button.url("• 𝐌𝐎𝐍𝐒𝐓𝐄𝐑 𝐐𝐔𝐄𝐄𝐍 •", "https://t.me/MONSTER_QUEENN")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        ANNIE = await event.client.get_me()
        bot_name = ANNIE.first_name
        bot_id = ANNIE.id
        TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [MONSTER](https://t.me/MONSTER_TERA_BAAP1)**\n\n"
        TEXT += f"» **MONSTER BHAI :** `M 1.8.31`\n"
        TEXT += f"» **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `3.11.3`\n"
        TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
              event.chat_id,
                    "https://graph.org/file/38343b1ece04117d60ac8.jpg",
                    caption=TEXT, 
                    buttons=START_BUTTON
                )
