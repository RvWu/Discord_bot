#This is where it starts...
import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        test = 'Stop testing fgt'.format(message)
        await client.send_message(message.channel, test)
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
        
    if message.content.startswith('!hello'):
        msg = 'Sup {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    
    if message.content.startswith('Good boy'):
        reply = 'Am good boy?{0.author.mention}'.format(message) 
        await client.send_message(message.channel, reply)
        answer = await client.wait_for_message(timeout=8.0, author=message.author)
        if answer is None:
            fmt = 'No answer is also an answer{0.author.mention} :FeelsSadMan:'
            await client.send_message(message.channel, fmt.format(answer)) #something wrong here, will work on that
            return
        right_answer = 'yes'
        if (answer.content) == right_answer :
            await client.send_message(message.channel, 'FeelsGoodMan')
        else:
            wrong_answer = 'no'
            if (answer.content) == wrong_answer :
                await client.send_message(message.channel, ':FeelsBadMan:')
            else:
                await client.send_message(message.channel, 'Sorry. i can not answer to that :/.'.format(answer))



client.run('Token')