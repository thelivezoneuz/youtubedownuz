from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Bizning kanal", url="https://t.me/ultrasoft_uz")],
        [InlineKeyboardButton(
            "Savollar bo`yicha 😊", url="https://t.me/i_shakhzod")]
    ])
    welcomed = f"Botimizga xush kelibsiz <b>{message.from_user.first_name}</b>\nMenga YouTubedan yuklanadigan media ssilkasini yuboring"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
