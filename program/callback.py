# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Salut/Bună [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) vă permite să redați muzică și videoclipuri în grupuri prin noua functie video Telegram!**

💡 **Află toate comenzile Bot-ului și cum funcționează apăsând pe butonul » 📚 Commands !**

🔖 **Pentru a ști cum să utilizezi acest bot, te rog sa apesi pe » ❓ Basic Guide button!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Adauga-ma in grupul tau ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ Basic Guide", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 Commands", callback_data="cbcmds"),
                    InlineKeyboardButton("❤ Donate", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 Official Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 Official Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🌐 Translation", url="https://t.me/OTRportal/"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **Basic Guide for using this bot:**

1.) **Mai întâi, adaugă-mă în grupul tău.**
2.) **Apoi da-mi functia de administrator și toate permisiunile, cu excepția administratorului anonim.**
3.) **După ce imi dai functia de admin, tasteaza /reload in grup/canal pentru a da refresh la actualizari.**
3.) **Adauga @{ASSISTANT_NAME} in grupul/canalul tau sau tasteaza /userbotjoin ca sa o inviti.**
4.) **Porniți mai întâi chatul video (voice in grup/canal) înainte de a începe să redai videoclipuri/muzică.**
5.) **Uneori utilizând comanda /reload te poate ajuta să remediezi o problemă.**

📌 **Dacă bot'u nu a intrat pe video/voice chat in grup/canal, asigurate că chatul este deja pornit sau tasteaza /userbotleave apoi tasteaza din nou /userbotjoin .**

💡 **Dacă aveți întrebări ulterioare despre acest bot, o puteți face pe chatul de asistență aici: @{GROUP_SUPPORT}**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **apăsați butonul de mai jos pentru a citi explicația și a vedea lista comenzilor disponibile !**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 Comenzi Admin", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 Sudo Cmd", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 Comenzi Basic", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 Inapoi", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 Basic:

» /mplay (nume melodie sau link) - reda muzica pe voice
» /vplay (video name/link) - reda video pe voice
» /vstream - reda video de pe YouTube sau stream m3u8
» /playlist - arata playlist
» /video (query) - descarca video de pe YouTube
» /song (query) - descarca melodie de pe YouTube
» /lyric (query) - incearca sa faca rost de versurile melodiei
» /search (query) - cauta pe youtube

» /ping - arata ping'ul la bot
» /uptime - arata uptime bot in privat
» /alive -  arata uptime bot (numai pe grup/canal)

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 Admin ONLY:

» /pause - pune pauza la stream
» /resume - da resume la stream
» /skip - schimba stream'ul
» /stop - opreste stream'ul
» /vmute - pune botu pe mute in voice
» /vunmute - scoate botu de pe mute in voice
» /volume `1-200` - ajusteaza volumul (botul trebuie sa aiba grad de admin)
» /reload - da refresh la bot si la permisiunile de admin
» /userbotjoin - invita botu sa intre pe un grup
» /userbotleave - ordona botului sa iasa de pe grup

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 Sageti:

» /rmw - cuarata toate fisierele raw 
» /rmd - curata toate fisierele descarcate pe bot (video/muzica)
» /sysinfo - arata info (heroku/VPS)
» /update - fa update la bot la ultima versiune (nu garanteaza nimeni ca va mai fi in romana dupa)
» /restart - restarteaza bot'u
» /leaveall - ordona botului sa iasa de pe toate grupurile/canalele

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Inapoi", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 numai administratorul cu permisiunea de gestionare voice chat poate folosi acest buton !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **settings of** {query.message.chat.title}\n\n⏸ : pause stream\n▶️ : resume stream\n🔇 : mute bot\n🔊 : unmute bot\n⏹ : opreste stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 Close", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ nu se face stream la nimic momentan", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 numai administratorul cu permisiunea de gestionare voice chat poate folosi acest buton !", show_alert=True)
    await query.message.delete()
