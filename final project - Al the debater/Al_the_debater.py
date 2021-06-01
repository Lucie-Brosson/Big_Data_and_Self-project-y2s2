import discord
import logging
from discord.ext import commands

#wikipedia API and setup
import wikipedia
import wikipediaapi

# other library
import random
import emoji
import giphy_client
from giphy_client.rest import ApiException


# API Gif giphy - to replace the image that I want I will you gif
giphy_API_key = "put your API key here"
giphy_API_instance = giphy_client.DefaultApi()

# Token to access discord
TOKEN = "put your API key here"


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

@client.command(name="status", help="gives you his status")
async def status(ctx):

    status = ("Pretty good I should say", "I... That is a good question, this is the first time someone ask. I would say better now that you asked", "Terrible I have to say, I can't find the 3rd volume of my botanic encyclopedia")

    await ctx.send(random.choice(status))


@client.command(name="definition", help="helps you with definition")
async def definition(ctx):


    User_message = ctx.message.content
    wikipedia_research_definition = User_message[3:]

    try :
        await ctx.send('Dear debater, here I my humble research on ' + wikipedia_research_definition + " :book:")
        await ctx.send('Definition : ' + wikipedia.summary(wikipedia_research_definition, sentences=3))

    except wikipedia.exceptions.PageError as a :

        await ctx.send ("I am sorry my dear but this is out of my jurisdiction")


@client.command(name="date", help="helps you with date")
async def date(ctx):

    User_message = ctx.message.content
    wikipedia_research_date = User_message[3:]

    try :
        await ctx.send('Dear debater, here I my humble research on ' + wikipedia_research_date + " :moyai:")

        await ctx.send('Description : ' + wikipedia.summary(wikipedia_research_date, sentences=3))

        date_events = wikipedia.page("Events" + wikipedia_research_date).section('Events','January-December','Date unknown')
        date_cut = date_events[:200]

        await ctx.send(date_cut)
    except wikipedia.exceptions.PageError as a :

        await ctx.send ("I am sorry my dear but this is out of my jurisdiction")


@client.command(name="artwork", help="helps you with your art research")
async def artwork(ctx):

    User_message = ctx.message.content
    wikipedia_research_art = User_message[3:]

    try :

        await ctx.send('Dear debater, here I my humble research on ' + wikipedia_research_art + " :art:")

        try :
            giphy_api_response = giphy_API_instance.gifs_search_get(giphy_API_key, wikipedia_research_art, limit=2)
            movie_gif_list = list(giphy_api_response.data)
            Movie_gif = random.choice(movie_gif_list)

            emb = discord.Embed(title=wikipedia_research_art)
            emb.set_image(url=f'https://media.giphy.com/media/{Movie_gif.id}/giphy.gif')
            await ctx.send (embed=emb)

        except ApiException as e:
            await ctx.send ("nothing to see here, go through")

        await ctx.send('Description : ' + wikipedia.summary(wikipedia_research_art, sentences=2))

    except wikipedia.exceptions.PageError as a :

        await ctx.send ("I am sorry my dear but this is out of my jurisdiction")


@client.command(name="movie", help="helps you with movie")
async def movie(ctx):

    User_message = ctx.message.content
    wikipedia_research_movie = User_message[3:]

    try :

        await ctx.send('Dear debater, here I my humble research on the ' + wikipedia_research_movie + " :clapper:")

        try :
            giphy_api_response = giphy_API_instance.gifs_search_get(giphy_API_key, wikipedia_research_movie, limit=2)
            movie_gif_list = list(giphy_api_response.data)
            Movie_gif = random.choice(movie_gif_list)

            emb = discord.Embed(title=wikipedia_research_movie)
            emb.set_image(url=f'https://media.giphy.com/media/{Movie_gif.id}/giphy.gif')
            await ctx.send (embed=emb)

        except ApiException as e:
            await ctx.send ("nothing to see here, go through")

        # find how to access the little bando + add the director + date + main actor

        await ctx.send('Description : ' + wikipedia.summary(wikipedia_research_movie, sentences=2))

        # I cut the plot for it to be short enough (less than 4000 words) and also to not spoil other user
        plot = wikipedia.page(wikipedia_research_movie).section('Plot')
        plot_cut = plot[:200]

        await ctx.send("Plot :   " + plot_cut + " .......  oh sorry I didn't meant to spoil, go look for yourself :exclamation:")

    except wikipedia.exceptions.PageError as a :

        await ctx.send ("I am sorry my dear but this is out of my jurisdiction")




@client.command(name="funfact", help="gives you his favourite fun fact")
async def fun_fact(ctx):
    random_page = wikipedia.random(pages=1)
    await ctx.send(wikipedia.summary(random_page, sentences = 10))

# personnalize help menu
@client.group(invoke_without_command = True)
async def help(ctx):
    em = discord.Embed(title = "Glossary of my extended knwoledge", description ="use the 'al help + your subject of interest' to have more detail on how to use a specific command")

    em.add_field(name = "hello", value = "I will greet you")
    em.add_field(name = "status", value = "you will see")

    em.add_field(name = ("date :moyai:"), value = "I will help you find the events that happened at this fatihfull date. => use commands = 'al date + your date' ")
    em.add_field(name = ("definition :book:"), value = "I will help you find the definition to your words. => use commands = 'al definition + your word' ")
    em.add_field(name = ("artwork :art:"), value = "I will help you find the artwork you are looking for. => use commands = 'al date + your artwork name' ")
    em.add_field(name = ("movie :clapper:"), value = "I will help you find the movie you are searching. => use commands = 'al date + your movie title' ")
    em.add_field(name = "funfact", value = "get a fun recap of a random subject")
    em.add_field(name = "need more help", value = "go to this link http : ")


    await ctx.send(embed = em)

client.run(TOKEN)
