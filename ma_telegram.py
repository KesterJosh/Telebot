from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '6407839508:AAGrtObU9NkSw9FKpV3I7HOUf24jOMsekJE'
BOT_USERNAME: Final = '@tokenburncheckerbot'

async def start_command(update: Update, context: Context):
    await update.message.reply_text('Hello, welcome to Token Burn Checker Bot. Kindly let me have the address of the token you want to check.')

async def handle_message(update: Update, context: Context):
    await update.message.reply_text('Hello, I check burnt Token, hand over an address.')

async def error(update: Update, context: Context):
    await update.message.reply_text('Hello, I check burnt Token, hand over an address.')

# Responses 

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'How are you?'
    if 'fine' in processed:
        return 'That is good'
    if 'I love token' in processed:
        return 'Don\'t forget to subscribe'
    return 'I don\'t understand you, nor can I detect any address'

async def handle_message(update: Update,  context: ContextTypes.DEFAULT_TYPE ):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else: 
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update,  context: ContextTypes.DEFAULT_TYPE ):
    print(f'Update {update} caused error {context.error}')

if __name__=='_main_':
    print('Starting Bot...')
    app =  Application.builder().token(TOKEN).build()

    # Commands 
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Messages 
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors 
    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=3)