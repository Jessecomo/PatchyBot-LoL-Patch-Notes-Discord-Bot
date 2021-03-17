import os
import requests
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
import re

#Scrape the riot website for the latest patch notes
class League:
    def __init__(self):
        self.patch = {"title": None, "url": None, "desc": None, "img": None}

    def get_patch_info(self):
        base_url = 'https://na.leagueoflegends.com'
        fetch_url = 'https://na.leagueoflegends.com/en-us/news/tags/patch-notes'
        html_page = urlopen(fetch_url)
        html_text = html_page.read().decode("utf-8")

        soup = BeautifulSoup(html_text, "html.parser")

    #Find the first link ,ie. the latest, patch notes
        for link in soup.find_all("a", limit=1):
            self.patch["url"] = base_url + link["href"]

    #Open patch note link
        get_url = requests.get(self.patch["url"])
        get_text = get_url.text
        soup = BeautifulSoup(get_text, "html.parser")

    #Get patch info
        self.patch["title"] = soup.find('h1').text
        self.patch["img"] = soup.find('a',class_ ='skins cboxElement').img['src']
        description = soup.find("blockquote",{"class":"blockquote context"}).text
        self.patch["desc"] = description[:500] + (description[500:] and '...')

    def get_tft_patch_info(self):
        base_url = 'https://na.leagueoflegends.com'
        fetch_url = 'https://na.leagueoflegends.com/en-us/news/game-updates/'
        html_page = urlopen(fetch_url)
        html_text = html_page.read().decode("utf-8")
        soup = BeautifulSoup(html_text, "html.parser")

        for link in soup.select('a[href*="teamfight-tactics-patch"]', limit=1):
                self.patch["url"] = base_url + link["href"]

        #Open patch note link
        get_url = requests.get(self.patch["url"])
        get_text = get_url.text
        soup = BeautifulSoup(get_text, "html.parser")

        #Get patch info
        self.patch["title"] = soup.find('h1').text
        self.patch["img"] = soup.find('a',class_ ='skins cboxElement').img['src']
        description = soup.find("blockquote",{"class":"blockquote context"}).text
        self.patch["desc"] = description[:500] + (description[500:] and '...')

        #Get updated patch notes if current patch title doesn't match their new one



def get_patch_message(gameMode):
    embed = discord.Embed()
    LoL = League()
    if gameMode == 1:
        LoL.get_patch_info()
    elif gameMode == 2:
        LoL.get_tft_patch_info()
    if LoL.patch["title"] is None or LoL.patch["url"] is None:
        embed.title = "Error occurred when retrieving patch notes"
        return embed
    embed.title = LoL.patch["title"]
    embed.url = LoL.patch["url"]
    if LoL.patch["desc"] is not None:
        embed.description = description=LoL.patch["desc"]
    embed.set_thumbnail(url= 'https://i.imgur.com/PL8pjLM.png')
    embed.set_image(url=LoL.patch["img"])
    embed.set_footer(text="Patchy Notes v1.0", \
    icon_url = "https://i.imgur.com/cxPxk9s.png")
    embed.color = 0x0a6fdb
    return embed

#Prefix for all the commands.
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command()
async def patch(ctx, mode = None):
    if not mode:
        #Send LoL patch notes
        await ctx.send(embed = get_patch_message(1))
    elif mode == "tft":
        #Send TFT patch notes
        await ctx.send(embed = get_patch_message(2))
    elif mode == "help":
        embed = discord.Embed()
        embed.title = "Patchy Bot"
        embed.description = "Allows you to easily get the latest\
        League of Legends and Teamfight Tactics patch notes right\
         in your discord server!"
        embed.color = 0x0a6fdb
        embed.add_field(name = "Commands", value = "!patch - League of Legends \n \
        !patch tft - Teamfight Tactics", inline = False)
        embed.set_thumbnail(url = 'https://i.imgur.com/cxPxk9s.png')
        embed.set_footer(text = "Patchy Notes v1.0 by Jesse Como", \
        icon_url = "https://i.imgur.com/cxPxk9s.png")
        await ctx.send(embed = embed)
    else:
        embed = discord.Embed()
        embed.title = "Sorry I didn't understand that..."
        embed.add_field(name = "Commands", value = "!patch - League of Legends \n \
        !patch tft - Teamfight Tactics", inline = False)
        embed.set_thumbnail(url = 'https://i.imgur.com/cxPxk9s.png')
        embed.set_footer(text = "Patchy Notes v1.0 by Jesse Como", \
        icon_url = "https://i.imgur.com/cxPxk9s.png")
        embed.color = 0x0a6fdb
        await ctx.send(embed = embed)

load_dotenv()
bot.run(os.getenv('TOKEN'))
