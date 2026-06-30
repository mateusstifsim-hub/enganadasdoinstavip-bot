import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

TOKEN = "7953201676:AAH_jLpht_iI1GVdAFjaxHOqxNP8oaAnZG4"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    teclado = [
        [InlineKeyboardButton("📅 1 Semana - R$5,90", callback_data="1semana")],
        [InlineKeyboardButton("🗓️ 1 Mês - R$10,00", callback_data="1mes")],
        [InlineKeyboardButton("♾️ Vitalício - R$15,00", callback_data="vitalicio")],
    ]
    markup = InlineKeyboardMarkup(teclado)

    texto = (
        "🔞 DERAM MOLE E A INTERNET NÃO ESQUECEU 🔞\n\n"
        "Gostosas que acharam que ninguém ia ver. Erraram feio.\n\n"
        "🔥 Tudo aqui dentro: flagras, vazados, momentos que elas queriam apagar.\n"
        "📉 PREÇO PROMOCIONAL: Só hoje R$15,00 (Pagamento único!)\n"
        "✅ Acesso Instantâneo\n"
        "✅ Sigilo Absoluto\n\n"
        "VAI FICAR DE FORA OU VAI VER O QUE ELA NÃO QUERIA? 😈👇"
    )

    await update.message.reply_text(text=texto, reply_markup=markup)

async def enviar_recuperacao(context, chat_id):
    await asyncio.sleep(300)

    if context.bot_data.get(f"pagou_{chat_id}"):
        return

    teclado = [
        [InlineKeyboardButton("📅 1 Semana - R$5,90", url="https://pay.cakto.com.br/fcuqim4_948367")],
        [InlineKeyboardButton("🗓️ 1 Mês - R$10,00", url="https://pay.cakto.com.br/zny2oym")],
        [InlineKeyboardButton("♾️ Vitalício - R$15,00", url="https://pay.cakto.com.br/3fmdjoc")],
    ]

    await context.bot.send_message(
        chat_id=chat_id,
        text=(
            "😈 Ei... você quase entrou.\n\n"
            "Sabe o que tá te esperando lá dentro? Flagras e vazados de gostosas que deram mole "
            "e não puderam fazer nada. Conteúdo que você não acha em lugar nenhum.\n\n"
            "🔥 Ainda dá tempo. Mas não por muito.\n\n"
            "👇 Escolha seu plano e entra agora:"
        ),
        reply_markup=InlineKeyboardMarkup(teclado)
    )

async def botao_clicado(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat_id

    if query.data == "1semana":
        asyncio.create_task(enviar_recuperacao(context, chat_id))
        await query.edit_message_text(
            text=(
                "📅 Você escolheu 1 Semana por R$5,90!\n\n"
                "⚡ OFERTA RELÂMPAGO — SÓ AGORA!\n\n"
                "Por apenas R$10,00 você leva o mês inteiro!\n"
                "Muito mais conteúdo por uma diferença pequena. 🔥\n\n"
                "👇 Escolha como quer prosseguir:"
            ),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔥 Quero o Mês por R$10,00!", url="https://pay.cakto.com.br/zny2oym")],
                [InlineKeyboardButton("📅 Manter 1 Semana por R$5,90", url="https://pay.cakto.com.br/fcuqim4_948367")],
                [InlineKeyboardButton("🔙 Voltar", callback_data="voltar")],
            ])
        )
    elif query.data == "1mes":
        asyncio.create_task(enviar_recuperacao(context, chat_id))
        await query.edit_message_text(
            text=(
                "🗓️ Você escolheu 1 Mês por R$10,00!\n\n"
                "♾️ ESPERA — VIU ISSO?\n\n"
                "Por apenas R$5,00 a mais você garante acesso VITALÍCIO.\n"
                "Paga uma vez, acessa para sempre. 😈\n\n"
                "👇 Escolha como quer prosseguir:"
            ),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("♾️ Quero o Vitalício por R$15,00!", url="https://pay.cakto.com.br/3fmdjoc")],
                [InlineKeyboardButton("🗓️ Manter 1 Mês por R$10,00", url="https://pay.cakto.com.br/zny2oym")],
                [InlineKeyboardButton("🔙 Voltar", callback_data="voltar")],
            ])
        )
    elif query.data == "vitalicio":
        asyncio.create_task(enviar_recuperacao(context, chat_id))
        await query.edit_message_text(
            text=(
                "♾️ Você escolheu o Vitalício por R$15,00!\n\n"
                "Paga uma vez e nunca mais se preocupa. Acesso para sempre. 😈\n\n"
                "👇 Clique abaixo para finalizar:"
            ),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("💳 Pagar Agora", url="https://pay.cakto.com.br/3fmdjoc")],
                [InlineKeyboardButton("🔙 Voltar", callback_data="voltar")],
            ])
        )
    elif query.data == "voltar":
        teclado = [
            [InlineKeyboardButton("📅 1 Semana - R$5,90", callback_data="1semana")],
            [InlineKeyboardButton("🗓️ 1 Mês - R$10,00", callback_data="1mes")],
            [InlineKeyboardButton("♾️ Vitalício - R$15,00", callback_data="vitalicio")],
        ]
        await query.edit_message_text(
            text=(
                "🔞 DERAM MOLE E A INTERNET NÃO ESQUECEU 🔞\n\n"
                "Gostosas que acharam que ninguém ia ver. Erraram feio.\n\n"
                "🔥 Tudo aqui dentro: flagras, vazados, momentos que elas queriam apagar.\n"
                "📉 PREÇO PROMOCIONAL: Só hoje R$15,00 (Pagamento único!)\n"
                "✅ Acesso Instantâneo\n"
                "✅ Sigilo Absoluto\n\n"
                "VAI FICAR DE FORA OU VAI VER O QUE ELA NÃO QUERIA? 😈👇"
            ),
            reply_markup=InlineKeyboardMarkup(teclado)
        )

async def pegar_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.video:
        file_id = update.message.video.file_id
        await update.message.reply_text(f"FILE_ID DO VÍDEO:\n{file_id}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(botao_clicado))
app.add_handler(MessageHandler(filters.VIDEO, pegar_id))
app.run_polling()
