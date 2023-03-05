from telethon import TelegramClient, events

# set up Telegram API credentials
api_id = <your_api_id>
api_hash = '<your_api_hash>'
phone_number = '<your_phone_number>'
client = TelegramClient(phone_number, api_id, api_hash)

# set up event handler to listen for messages in a group
@client.on(events.NewMessage(chats=<your_group_chat_id>))
async def handle_message(event):
    text = event.message.text
    numbers = [int(s) for s in text.split() if s.isdigit()] # find all numbers in the message
    tags = [s for s in text.split() if s.startswith('@')] # find all telegram tags in the message
    print('Numbers:', numbers)
    print('Tags:', tags)

# start the client
client.start()
client.run_until_disconnected()