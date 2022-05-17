from disnake.ext import commands
import disnake

class funCommands(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  
  @commands.command()
  async def funCommand(self, ctx):
    # Your fun command here
    return await ctx.reply(":)")


  @funCommand.error
  async def funCommand_error(self, ctx, error):
    # Your custom error handler for funCommand cmd here
    await ctx.reply(error)


def setup(bot):
  bot.add_cog(funCommands(bot))