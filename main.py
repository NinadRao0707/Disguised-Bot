import discord
import os
import random
from random import randint
from discord import member
from discord.message import Attachment
import requests
import json
import random
import pyjokes
from discord.ext import commands
import pywhatkit as kt
from datetime import datetime

# Define prefix of bot commands
bot = commands.Bot(command_prefix='!', help_command=None)

# Connecting the bot to discord
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Giving response on new member join
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, Welcome to my Discord server!')

# Invalid command tracker
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.channel.send('Invalid command !!')

# Get a quote from a website
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return(quote)

# Get a weather info from a website
def get_weather_info(location):
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&appid=53b4148f8b88ecf923267cf7eb4500fe".format(location))
    json_data = json.loads(response.text)['main']
    return(json_data)

# Help command
@bot.command()
async def help(ctx):
    em = discord.Embed(title='Disguised Bot Help Center !!', description='Use !help command for extended information on command', colour=discord.Colour.blue())
    em.add_field(name='!welcome', value='Will give you a warm welcome to our server :)', inline=False)
    em.add_field(name='Feeling Lonely?', value='Disguised Bot will always be there for you anytime <3', inline=False)
    em.add_field(name='!inspire', value='Will get you a random inspiring quote to make your day better :)', inline=False)
    em.add_field(name='!rolldice', value='Feeling bored? This will get you a random dice number. Who knows that this might be your lucky number o_O', inline=False)
    em.add_field(name='!8ball', value='Do you feel insecure? Ask 8ball and get the answer to every question !!', inline=False)
    em.add_field(name='!tictactoe', value='Tired of studying? Play TicTacToe with your friend and have a fun time !!', inline=False)
    em.add_field(name='!joke', value='Do you want someone to put a smile on your face? Ask a joke and you will definitely laugh XD', inline=False)
    em.add_field(name='!roastme', value='Do you think that no one can roast you? Disguised bot will roast the hell out of you XD', inline=False)
    em.add_field(name='!weather', value='Want to check weather over the world? You can find it over here with one click :o', inline=False)
    em.add_field(name='!image', value='Shows you an image out of nowhere :)', inline=False)
    em.add_field(name='!fact', value='Want to find out something new? Fact command will give you the fact of the day !!', inline=False)
    em.add_field(name='!meme', value='Bored from 9gag? Disguised bot will provide you the funniest memes XD', inline=False)
    em.add_field(name='!whatsapp', value='Lazy to bring a mobile to send a whatsapp message? Disguised bot will do your job :0', inline=False)
    em.add_field(name='!rps', value='Play Rock Paper Scissors with Disguised Bot and make sure you win once :)', inline=False)
    await ctx.channel.send(embed=em)

# Welcome command
@bot.command(name='welcome')
async def welcome(ctx):
    em = discord.Embed(title='Hello, Welcome to Debuggers !!', description='Elite Server', colour=discord.Colour.blue())
    em.set_image(url='https://pyxis.nymag.com/v1/imgs/e1c/8ff/8b545a8509aaffa7c3ce22cb4ca47c049a-wojak-05.2x.w710.jpg')
    await ctx.channel.send(embed=em)

async def check_for_birthday(self):
    now = datetime.datetime.now()
    curmonth = now.month
    curday = now.day

# Inspire command
@bot.command(name='inspire', help='Gives a random inspiring quote')
async def inspire_quotes(ctx):
    quote = get_quote()
    await ctx.channel.send(quote)

# Roll dice command
@bot.command(name='rolldice', help='Simulates a rolling dice')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.channel.send(', '.join(dice))

# Roll dice command error tracker
@roll.error
async def roll_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.channel.send('Please specify the arguments correctly !!')

# 8Ball command
@bot.command(name='8ball', help='Ask a Yes–No question to the ball, it will answer the truth')
async def magic_ball(ctx, question):
    eightball_file = open("/Disguised Bot/eightballmessages.txt", mode="r", encoding="utf8")
    eightball_file_facts = eightball_file.read().split("\n")
    eightball_file.close()
    for i in eightball_file_facts:
        if i == "": 
            eightball_file_facts.remove(i)
    await ctx.channel.send(random.choice(eightball_file_facts))

# 8Ball command error tracker
@magic_ball.error
async def magic_ball_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.channel.send('Please specify the arguments correctly !!')

# Rock Paper Scissors command
@bot.command(name='rps', help='Play Rock Paper Scissors with Disguised Bot')
async def rps(ctx, message):
    choose = ["rock", "paper", "scissors"]
    # Random choice for bot
    disguisedbot = choose[randint(0, 2)]
    player = message.lower()
    
    if player == "rock":
        await ctx.channel.send("You choosed 👊")
    elif player == "paper":
        await ctx.channel.send("You choosed ✋")
    else:
        await ctx.channel.send("You choosed ✌️")
        
    if disguisedbot == "rock":
        await ctx.channel.send("Disguised Bot choosed 👊")
    elif disguisedbot == "paper":
        await ctx.channel.send("Disguised Bot choosed ✋")
    else:
        await ctx.channel.send("Disguised Bot choosed ✌️")
        
    if player == disguisedbot:
        await ctx.channel.send("Tie!")
    elif player == "rock":
        if disguisedbot == "paper":
            await ctx.channel.send("You lose! ✋ covers 👊")
        else:
            await ctx.channel.send("You win! 👊 smashes ✌️")
    elif player == "paper":
        if disguisedbot == "scissors":
            await ctx.channel.send("You lose! ✌️ cut ✋")
        else:
            await ctx.channel.send("You win! ✋ covers 👊")
    elif player == "scissors":
        if disguisedbot == "rock":
            await ctx.channel.send("You lose! 👊 smashes ✌️")
        else:
            await ctx.channel.send("You win! ✌️ cut ✋")
    else:
        await ctx.channel.send("That's not a valid play. Check your spelling!")

# Tic Tac Toe command
@bot.command(name='tictactoe', help='Play TicTacToe with your friend')
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver
    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0
        player1 = p1
        player2 = p2
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")

@bot.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver
    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]
                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the !tictactoe command.")

# Check winner in Tic Tac Toe game
def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

# Tic Tac Toe command error tracker
@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command !!")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>) !!")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark !!")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer !!")

# Joke command
@bot.command(name='joke', help='Will give you a random joke XD')
async def funny_joke(ctx):
    randno = random.randint(1,2)
    if randno == 1:
        joke_file = open("/Disguised Bot/jokes.txt", mode="r", encoding="utf8")
        joke_file_jokes = joke_file.read().split("\n")
        joke_file.close()
        for i in joke_file_jokes:
            if i == "": 
                joke_file_jokes.remove(i)
        rand_joke = random.choice(joke_file_jokes)
    else:
        rand_joke = pyjokes.get_joke()
    await ctx.channel.send(rand_joke)

# Roast me command
@bot.command(name='roastme', help='Will roast you !!')
async def roast_message(ctx):
    roast_file = open("/Disguised Bot/roasts.txt", mode="r", encoding="utf8")
    roast_file_jokes = roast_file.read().split("\n")
    roast_file.close()
    for i in roast_file_jokes:
        if i == "": 
            roast_file_jokes.remove(i)
            ros = random.choice(roast_file_jokes)
    await ctx.channel.send(ros)

# Roast command error tracker
@roast_message.error
async def roast_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.channel.send('Please specify the arguments correctly !!')

# Random Image command
@bot.command(name='image', help='Gives you a random image !!')
async def random_image(ctx):
    message = discord.Embed(title='Random Image', color=discord.Colour.blue())
    randno = random.randint(1,200)
    url_img = "https://source.unsplash.com/random/200x200?sig={}".format(randno)
    message.set_image(url=url_img)
    await ctx.channel.send(embed=message)

# Weather Info command
@bot.command(name='weather', help='Gives you weather information about your city :3')
async def weather_info(ctx, location):
    weather_data = get_weather_info(location)
    del weather_data['humidity']
    del weather_data['pressure']
    key_features = {'temp' : 'Temperature', 'feels_like' : 'Feels Like', 'temp_min' : 'Minimum Temperature', 'temp_max' : 'Maximum Temperature'}
    location = location.title()
    message = discord.Embed(title=f'{location} Weather', description=f'Here is the weather in {location}.', color=discord.Colour.blue())
    for key in weather_data:
        message.add_field(name=key_features[key], value=str(weather_data[key]), inline=False)
    await ctx.channel.send(embed=message)

# Weather Info command error tracker
@weather_info.error
async def weather_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.channel.send('Please specify the arguments correctly !!')

# Random Facts command
@bot.command(name='fact', help='Gives you the fact of the day :)')
async def random_fact(ctx):
    start = "Did you know that "
    fact_file = open("/Disguised Bot/facts.txt", mode="r", encoding="utf8")
    fact_file_facts = fact_file.read().split("\n")
    fact_file.close()
    for i in fact_file_facts:
        if i == "": 
            fact_file_facts.remove(i)
    await ctx.channel.send(start + random.choice(fact_file_facts).lower())
    
# Random Meme command
@bot.command(name='meme', help='Gives you the funniest meme XD')
async def meme_image(ctx):
    path = "D:\\Disguised Bot\\images"
    files = os.listdir(path)
    img = random.choice(files)
    meme_img = img.lower()
    await ctx.channel.send(file = discord.File("images/{}".format(meme_img)))

# Sending a whastapp message command
@bot.command(name='whatsapp', help='Sends a whatsapp message to the member :o')
async def whatsapp_message(ctx, m1: discord.Member, whatsapp_message):
    global member
    member = m1.name
    now = datetime.now()
    time_hours = int(now.strftime("%H"))
    time_minutes = int(now.strftime("%M")) + 2
    if member in whatsapp_numbers.keys():
        number = "+" + whatsapp_numbers[member]
        kt.sendwhatmsg(number, whatsapp_message, time_hours, time_minutes)
        response = "You have sent the message :)"
    else:
        response = "Sorry, couldn't find the number :("
    await ctx.channel.send(response)

# On message command
@bot.event
async def on_message(message):
	if any(word in message.content for word in sad_words):
		await message.channel.send(random.choice(starter_encouragements))

	await bot.process_commands(message)
    
player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]

starter_encouragements = ["Cheer up!", "Hang in there.", "You are a great person!"]

whatsapp_numbers = {'Aamir Ansari' : "918850604991", 'IshaGawde' : "919029563005", 'jishaa1234' : "918482913514", 'Kanha' : "917622091456", 
    'Nindiya0707' : "918356852631", 'Shal' : "919619680468", 'Sreekesh Iyer' : "917506916922", 'vkrishna2090' : "918779949739"}

bot.run('ODQzNzA5MjI2OTkwOTYwNjgx.YKHzcw.ZK6DkYl4MPAfh879fM5h58DtAiQ')