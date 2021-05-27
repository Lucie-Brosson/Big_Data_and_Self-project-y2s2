import discord
import logging
from discord.ext import commands

#wikipedia API and setup
import wikipedia
import wikipediaapi

# other library
import random
import emoji

# To do
# work with the study and statistic
#or work with the other API and add picture and details on everything
# send a message when someone join on how to play with the bot



# Token to access discord
TOKEN = "Put your token here"

# define the bot command and it's prefix
client = commands.Bot(command_prefix = 'al ')
client.remove_command("help")

#Give you logging information
logging.basicConfig(level=logging.INFO)

# When the bot is ready
@client.event
async def on_ready():
    print ("I am here to fight")

    # change bot presence
    game = ('cluedo', 'monopoly', 'russian roulette','trivial pursuit','the flute','poker with the dogs')
    await client.change_presence(activity = discord.Activity( type = discord.ActivityType.playing, name = random.choice(game)))

# when a member join
@client.event
async def on_member_join(member):
    print(f'{member} has joined us, rejoice !')

#when a member quit, is ban...
@client.event
async def on_member_remove(member):
    print(f'{member} left, grieve')

# other command
@client.command(name = "hello", help="greets you")
async def hello(ctx):
    await ctx.send(f'Well good day {ctx.author}, how may I assist you today')

@client.command(name="status", help="gives you his")
async def status(ctx):
    status = ("Pretty good I should say","I... That is a good question, this is the first time someone ask. I would say better now that you asked","Terrible I have to say, I can't find the 3rd volume of my botanic encyclopedia")

    await ctx.send(random.choice(status))

@client.command(name="statistic", help="help you with statistic")
async def statistic(ctx):
    await ctx.send('to be modified stats')

@client.command(name="definition", help="helps you with definition")
async def definition(ctx):
    await ctx.send('to be modified definition')

    User_message = ctx.message.content
    wikipedia_research_definition = User_message[3:]

    await ctx.send('Dear debater, here I my humble research on ' + wikipedia_research_definition + " :book:")

    await ctx.send('Definition : ' + wikipedia.summary(wikipedia_research_definition, sentences=3))


@client.command(name="date", help="helps you with date")
async def date(ctx):

    User_message = ctx.message.content
    wikipedia_research_date = User_message[3:]

    await ctx.send('Dear debater, here I my humble research on ' + wikipedia_research_date + " :moyai:")

    await ctx.send('Description : ' + wikipedia.summary(wikipedia_research_date, sentences=3))

    date_events = wikipedia.page("Events" + wikipedia_research_date).section('Events','January-December','Date unknown')
    date_cut = date_events[:200]

    await ctx.send(date_cut)


@client.command(name="study", help="helps you with studies")
async def study(ctx):
    await ctx.send('to be modified study')



@client.command(name="artwork", help="helps you with your art research")
async def artwork(ctx):

    User_message = ctx.message.content
    wikipedia_research_art = User_message[3:]

    # add images with the poster find a way to get the right picture
    await ctx.send(wikipedia.page(wikipedia_research_art).images[1])

    await ctx.send('Dear debater, here I my humble research on ' + wikipedia_research_art + " :art:")
    await ctx.send('Description : ' + wikipedia.summary(wikipedia_research_art, sentences=2))


@client.command(name="movie", help="helps you with movie")
async def movie(ctx):
    User_message = ctx.message.content
    wikipedia_research_movie = User_message[3:]
    await ctx.send('Dear debater, here I my humble research on the ' + wikipedia_research_movie + " :clapper:")

    # add images with the poster find a way to get the right picture
    await ctx.send(wikipedia.page(wikipedia_research_movie).images[1])

    # find how to access the little bando + add the director + date + main actor

    await ctx.send('Description : ' + wikipedia.summary(wikipedia_research_movie, sentences=1))

    # I cut the plot for it to be short enough (less than 4000 words) and also to not spoil other user
    plot = wikipedia.page(wikipedia_research_movie).section('Plot')
    plot_cut = plot[:200]

    await ctx.send("Plot :   " + plot_cut + " .......  oh sorry I didn't meant to spoil, go look for yourself :exclamation:")



@client.command(name="funfact", help="gives you his favourite fun fact")
async def fun_fact(ctx):
    random_page = wikipedia.random(pages=1)
    await ctx.send(wikipedia.summary(random_page, sentences = 10))

# personnalize help menu
@client.group(invoke_without_command = True)
async def help(ctx):
    em = discord.Embed(title = "Glossary of my extended knwoledge", description ="use the 'al help + your subject of interest' to have more detail on how to use a specific command", color = dark_purple)

    em.add_field(name = "hello", value = "I will greet you")
    em.add_field(name = "status", value = "you will see")

    em.add_field(name = ("date :moyai:"), value = "I will help you find the events that happened at this fatihfull date. => use commands = 'al date + your date' ")
    em.add_field(name = ("definition :book:"), value = "I will help you find the definition to your words. => use commands = 'al definition + your word' ")
    em.add_field(name = ("artwork :art:"), value = "I will help you find the artwork you are looking for. => use commands = 'al date + your artwork name' ")
    em.add_field(name = ("movie :clapper:"), value = "I will help you find the movie you are searching. => use commands = 'al date + your movie title' ")
    em.add_field(name = "statistic", value = "I am still enquyring about this field, I shall come back soon enough to help you in your quest of knowledge")
    em.add_field(name = "study", value = "I am still enquyring about this field, I shall come back soon enough to help you in your quest of knowledge")
    em.add_field(name = "funfact", value = "get a fun recap of a random subject")
    em.add_field(name = "need more help", value = "go to this link http : ")


    await ctx.send(embed =em)





client.run(TOKEN)
