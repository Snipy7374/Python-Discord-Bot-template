from disnake.ext import commands
import disnake

class adminCommands(commands.Cog):

  def __init__(self, bot):
    self.bot = bot


  @commands.command()
  @commands.has_permissions(administrator=True)
  async def adminCommand(self, ctx):
    #Your only admin command here, replace "adminCommand" with the name of the command, paste the script here
    return await ctx.reply(":)")


  @adminCommand.error
  async def nameCommand_error(self, ctx, error):
    #Your command error handler for adminCommands cmd here
    return await ctx.reply(error)


def setup(bot):
  bot.add_cog(adminCommands(bot))