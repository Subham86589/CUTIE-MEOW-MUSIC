
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from DAXXMUSIC import app

#--------------------------

MUST_JOIN = "ALLTYPECC"
#------------------------
@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await app.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/BILLA_GANG_NTWK" + MUST_JOIN
            else:
                chat_info = await app.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://graph.org/file/a602e8bd957ba012313cf.jpg", caption=f"𝙏𝙊 𝙎𝙏𝘼𝙍𝙏 𝙏𝙃𝙀 𝘽𝙊𝙏💌 𝙐 𝙈𝙐𝙎𝙏 𝘽𝙀 𝘼 𝘽𝙄𝙇𝙇𝘼 𝙇𝙊𝙑𝙀𝙍 𝘼𝙉𝘿 𝙈𝙐𝙎𝙏 𝙅𝙊𝙄𝙉 𝘽𝙄𝙇𝙇𝘼 𝙂𝘼𝙉𝙂⚡
𝘼𝙊𝙊 𝙊𝙍 𝙈𝙀𝙊𝙒 𝙈𝙀𝙊𝙒 𝙆𝙍𝙊 ❤ [๏sᴜᴘᴘᴏʀᴛ๏]({link}) ʏᴇᴛ, ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜsᴇ ᴍᴇ ᴛʜᴇɴ ᴊᴏɪɴ [๏sᴜᴘᴘᴏʀᴛ๏]({link}) ᴀɴᴅ sᴛᴀʀᴛ ᴍᴇ ᴀɢᴀɪɴ ! ",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("๏Jᴏɪɴ๏", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"๏ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ ᴍᴜsᴛ_Jᴏɪɴ ᴄʜᴀᴛ ๏: {MUST_JOIN} !")
