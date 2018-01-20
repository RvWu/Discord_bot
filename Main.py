#This is where it starts...
import discord
import asyncio

client = discord.Client()
@client.event
async def on_message(message):
if message.content.startswith('!hello'):
        msg = 'Sup {0.author.mention}'.format(message)

await client.send_message(message.channel, msg)
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

client.run('NDA0MjkxMTc1NzUxNzQ1NTM3.DUTtBw.d5UE2eHI7i7f7LR9oItRGj0lalc')