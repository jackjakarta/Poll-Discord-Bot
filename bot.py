import discord
import keys

TOKEN = keys.DISCORD_TOKEN

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    activity = discord.Activity(name="-poll", type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.content.startswith('-poll'):
        # Get the poll question and answer options
        poll_data = message.content[6:].split('/')
        question = poll_data[0].strip()
        options = [option.strip() for option in poll_data[1:]]
        # Create the poll message embed
        embed = discord.Embed(title=question, color=0x4BA081)
        for i, option in enumerate(options):
            embed.add_field(name=f"{i+1}. {option}", value="\u200b", inline=False)
        # Send the poll message and save it to a variable
        poll_message = await message.channel.send(embed=embed)
        # Add the reactions to the poll message
        for i in range(len(options)):
            await poll_message.add_reaction(f'{i+1}\u20e3')


    if message.content.startswith("-help"):
        help_text = "-poll - example: -poll what color?/blue/red/yellow \n" \
                    "-help - how to use the poll bot \n"
            
        embed = discord.Embed(title="list of commands:", description=help_text, color=discord.Color.blurple)
        await message.channel.send(embed=embed)        


client.run(TOKEN)
