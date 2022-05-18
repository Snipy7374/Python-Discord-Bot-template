import os
import json
import sys
import disnake
from disnake.ext.commands import Bot
from disnake.ext import commands
from server_host import server

# preformatting config.json file
if not os.path.isfile("./config.json"):
  config_key = {
    "TOKEN": "",
    "BotStatus": "",
    "Prefix": "",
    "Test_guilds": []
  }
  # if file config.json doesn't exist then create a new config.json file with the preformatted key
  with open("./config.json", "w") as file:
    json.dump(config_key, file, indent=2)
  sys.exit("Config file not found, i'm creating a config file but you need to configure it!")

else:
  # reading the config.json file; getting TOKEN variable and test_guilds list
  with open("./config.json") as file:
    config = json.load(file)
    test_guilds = config["Test_guilds"]
    TOKEN = config["TOKEN"]

def get_prefix(bot, message):
  with open("config.json", "r") as file: prefix = json.load(file)
  return prefix["Prefix"]

# required through https://discord.com/developers/applications/{YOUR_APP_ID}/bot 
# PRESENCE INTENTE = TRUE (ENABLED)
# SERVER MEMBER INTENT = TRUE (ENABLED)
# MESSAGE CONTENT INTENT = TRUE (ENABLED)
intents = disnake.Intents.all()

bot = Bot(
  command_prefix=get_prefix,
  intents=intents,
  help_command=None,
  case_insensitive=True,
  sync_commands_debug=False,
  test_guilds=test_guilds
)
# Insensitive case command ex: -namecommands == -NAMECOMMANDS == -NameCommands ......

@bot.event
async def on_ready():
  print(f"\033[1;32m Logged in as {bot.user}\n Bot is ready!  \n")

  for filename in os.listdir("./cogs/admin"):
    if filename.endswith(".py"):
      try:
        bot.load_extension(f"cogs.admin.{filename[:-3]}")
      except Exception as error:
        exc = "{}: {}".format(type(error).__name__, error)
        print(f"Failed to load cog cog.admin.{filename}\n{exc}")
        
  for filename in os.listdir("./cogs/fun"):
    if filename.endswith(".py"):
      try:
        bot.load_extension(f"cogs.fun.{filename[:-3]}")
      except Exception as error:
        exc = "{}: {}".format(type(error).__name__, error)
        print(f"Failed to load cog cog.fun.{filename}\n{exc}")

  for filename in os.listdir("./cogs/misc"):
    if filename.endswith(".py"):
      try:
        bot.load_extension(f"cogs.misc.{filename[:-3]}")
      except Exception as error:
        exc = "{}: {}".format(type(error).__name__, error)
        print(f"Failed to load cog cog.misc.{filename}\n{exc}")


@bot.command()
@commands.has_permissions(administrator=True)
async def reloadcog(ctx, folder: str):
  # folder == admin, fun, misc
  cog_count = 0
  for filename in os.listdir(f"./cogs/{folder}"):
    if filename.endswith(".py"):
      try:
        bot.reload_extension(f"cogs.{folder}.{filename[:-3]}")
        cog_count += 1
      except Exception as error:
        exc = "{}: {}".format(type(error).__name__, error)
        print(f"Failed to load cog cog.{folder}.{filename}\n{exc}")
        await ctx.reply(f":x: cogs.{folder}.{filename} cannot be reloaded!")

  await ctx.reply(f"cogs.{folder} extension folder reloaded successfully! ({cog_count} cogs were reloaded)")
  

@bot.command()
@commands.has_permissions(administrator=True)
async def reloadAll(ctx):
  cog_count = 0
  
  for filename in os.listdir("./cogs/admin"):
    if filename.endswith(".py"):
      try:
        bot.reload_extension(f"cogs.admin.{filename[:-3]}")
        cog_count += 1
      except Exception as error:
        exc = "{}: {}".format(type(error).__name__, error)
        print(f"Failed to load cog cog.admin.{filename}\n{exc}")

  for filename in os.listdir("./cogs/fun"):
    if filename.endswith(".py"):
      try:
        bot.reload_extension(f"cogs.fun.{filename[:-3]}")
        cog_count += 1
      except Exception as error:
        exc = "{}: {}".format(type(error).__name__, error)
        print(f"Failed to load cog cog.fun.{filename}\n{exc}")

  for filename in os.listdir("./cogs/misc"):
    if filename.endswith(".py"):
      try:
        bot.reload_extension(f"cogs.misc.{filename[:-3]}")
        cog_count += 1
      except Exception as error:
        exc = "{}: {}".format(type(error).__name__, error)
        print(f"Failed to load cog cog.misc.{filename}\n{exc}")

  await ctx.reply(f"All commands reloaded succesfully! ({cog_count} cogs were reloaded)")

@reloadAll.error
async def reloadAll_error(ctx, error):
  #Your error handler here (for reloadAll cmd)
  await ctx.reply(error)

@reloadcog.error
async def reloadcog_error(ctx, error):
  #Your error handler here (for reloadcog cmd)
  await ctx.reply(error)
  


server()
bot.run(TOKEN, reconnect=True)
