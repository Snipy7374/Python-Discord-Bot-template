from disnake.ext import commands
import disnake

class miscCommands(commands.Cog):

  def __init__(self, bot):
    self.bot = bot


  @commands.command()
  async def miscCommand(self, ctx):
    # Your miscCommand here
    return await ctx.reply(":)")

  @miscCommand.error
  async def miscCommand_error(self, ctx, error):
    # Your custom error handler for miscCommand cmd here
    await ctx.reply(error)


def setup(bot):
  bot.add_cog(miscCommands(bot))