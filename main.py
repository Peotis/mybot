from settings import settings
import discord
import random, logging, asyncio, os
from discord.ext import commands
from bot_logic import *

# Set up logging
logger = logging.getLogger('discord')
logger.setLevel(logging.ERROR)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.typing  = False
intents.presences = False

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'You have logged in as {bot.user}')

@bot.command()
async def organik(ctx):
    with open('organik.txt','r', encoding='UTF-8') as f:
        file_content = f.read()
        f.close()
    await ctx.send(file_content)

@bot.command()
async def anorganik(ctx):
    with open('anorganik.txt', 'r', encoding='UTF-8') as f:
        file_content = f.read()
    
    embed = discord.Embed(title='Anorganik', description=file_content, color=discord.Color.blue())
    await ctx.send(embed=embed)

# Saat bot menerima pesan, bot akan mengirimkan pesan di saluran yang sama!
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')
    embed = discord.Embed(title="Halo", description="bot ini di buat oleh clay", color=0x00ff00)
    embed.set_author(name="Kodland test bot", icon_url="https://pbs.twimg.com/media/FtYXfHyXgAgKcdl?format=png&name=small")
    embed.add_field(name="$list", value="gunakan $list, untuk mengetahui fungsi bot ini", inline=False)
    embed.set_footer(text="mengenalkan saya adalah bot yang dari sebuah project")
    await ctx.send(embed=embed)

@bot.command()
async def smile(ctx):
    embed = discord.Embed(title="emoji", description="bot ini di buat oleh clay", color=0x00ff00)
    embed.set_author(name="Kodland test bot", icon_url="https://pbs.twimg.com/media/FtYXfHyXgAgKcdl?format=png&name=small")
    embed.add_field(name=gen_emodji(), value="ini adalah emoji yang kamu dapatkan", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def coin(ctx):
    embed = discord.Embed(title="flip a coin", description="bot ini di buat oleh clay", color=0x00ff00)
    embed.set_author(name="Kodland test bot", icon_url="https://pbs.twimg.com/media/FtYXfHyXgAgKcdl?format=png&name=small")
    embed.add_field(name=flip_coin(), value="ini adalah koin yang kamu dapatkan", inline=False)
    await  ctx.send(embed=embed)
    
@bot.command()
async def password(ctx):
    embed = discord.Embed(title="random a passowrd", description="bot ini di buat oleh clay", color=0x00ff00)
    embed.set_author(name="Kodland test bot", icon_url="https://pbs.twimg.com/media/FtYXfHyXgAgKcdl?format=png&name=small")
    embed.add_field(name=gen_pass(10), value="ini adalah password random yang kamu dapatkan", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def list(ctx):
    with open('features.txt', 'r', encoding='UTF-8') as f:
        file_content = f.read()
    
    embed = discord.Embed(title='List', description=file_content, color=discord.Color.blue())
    await ctx.send(embed=embed)
    
@bot.command()
async def rps(ctx, user_choice):
    try:
        choices = ['rock', 'paper', 'scissors']
        bot_choice = random.choice(choices)

        user_choice = user_choice.lower()
        if user_choice not in choices:
            await ctx.send('Invalid choice. Please choose between rock, paper, or scissors.')
            return

        if user_choice == bot_choice:
            result = "It's a tie!"
        elif (
            (user_choice == 'rock' and bot_choice == 'scissors') or
            (user_choice == 'paper' and bot_choice == 'rock') or
            (user_choice == 'scissors' and bot_choice == 'paper')
        ):
            result = "You win!"
        else:
            result = "I win!"

        # Create an embedded message
        embed = discord.Embed(title="Rock Paper Scissors", color=0x00ff00)
        embed.set_author(name="Bot Name", icon_url="BOT_ICON_URL")
        embed.add_field(name="Your choice", value=user_choice, inline=True)
        embed.add_field(name="Bot's choice", value=bot_choice, inline=True)
        embed.add_field(name="Result", value=result, inline=False)

        # Send the embedded message to the channel
        await ctx.send(embed=embed)
    except Exception as e:
        logger.exception(f"An error occurred in the 'rps' command: {e}")
 
@bot.command()
async def eightball(ctx, *, question):
    # Tentukan daftar tanggapan 8ball
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."   
    ]

    # Choose a random response from the list
    response = random.choice(responses)

    # Create an embedded message
    embed = discord.Embed(title="8ball", description=f"Pertanyaan: {question}\nJawaban: {response}", color=0x00ff00)
    embed.set_author(name="Kodland test bot", icon_url="https://pbs.twimg.com/media/FtYXfHyXgAgKcdl?format=png&name=small")

    # Send the embedded message to the channel
    await ctx.send(embed=embed)


questions = [
    {
        'question': 'Siapakah presiden pertama Indonesia?',
        'options': ['Joko Widodo', 'Soeharto', 'Soekarno', 'Megawati Soekarnoputri'],
        'answer': 2
    },
    {
        'question': 'Ibukota Indonesia adalah...',
        'options': ['Jakarta', 'Surabaya', 'Bandung', 'Yogyakarta'],
        'answer': 0
    },
    {
        'question': 'Siapakah penemu bola lampu?',
        'options': ['Nikola Tesla', 'Albert Einstein', 'Isaac Newton', 'Thomas Alva Edison'],
        'answer': 3
    },
    {
        'question':'Ada berapakah pulau di indonesia yang terbesar?',
        'options': ['9','10','5','6'],
        'answer': 1
    }
]

@bot.command()
async def quiz(ctx):
    random.shuffle(questions)

    score = 0
    for i, question in enumerate(questions, start=1):
        options = '\n'.join(f'{index}. {option}' for index, option in enumerate(question['options'], start=1))
        
        embed = discord.Embed(title=f"Quiz Question {i}", description=question['question'], color=discord.Color.blue())
        embed.add_field(name='Options', value=options, inline=False)
        embed.set_footer(text=f"Reply with the correct option number (1-{len(question['options'])})")

        await ctx.send(embed=embed)

        try:
            def check(m):
                return m.author == ctx.author and m.channel == ctx.channel

            user_response = await bot.wait_for('message', check=check, timeout=30)
            user_answer = int(user_response.content)

            if user_answer - 1 == question['answer']:
                score += 1

        except asyncio.TimeoutError:
            await ctx.send("Timeout! You took too long to respond.")
            return

    score_embed = discord.Embed(title="Quiz Result", color=discord.Color.green())
    score_embed.add_field(name="Score", value=f"{score}/{len(questions)}")
    await ctx.send(embed=score_embed)

@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('images'))
    file_path = f'images/{img_name}'
    
    embed = discord.Embed(title='Meme', description='Here\'s a random meme:', color=discord.Color.blue())
    embed.set_image(url=f'attachment://{img_name}')
    
    with open(file_path, 'rb') as f:
        picture = discord.File(f, filename=img_name)
        embed.set_footer(text=f'Image: {img_name}')
        await ctx.send(file=picture, embed=embed)
      
bot.run(settings["TOKEN"])
