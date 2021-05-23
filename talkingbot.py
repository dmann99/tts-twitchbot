import configparser
import pyttsx3
import re
from twitchio.ext import commands


# Read configuration
config = configparser.ConfigParser()
config.read('talkingbot.properties')

config_token     = config['DEFAULT']['irc_token']
config_gender    = int( config['DEFAULT']['gender'] )
config_wpm_rate  = int( config['DEFAULT']['wpm_rate'] )
config_channel   = config['DEFAULT']['channel']
config_client_id = config['DEFAULT']['client_id']
config_nick      = config['DEFAULT']['nick']
config_prefix    = config['DEFAULT']['prefix']

# Init TTS Engine
engine = pyttsx3.init()
engine.setProperty('rate', config_wpm_rate)
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice',  voices[ config_gender ].id)

# Extract arguments from a Raw Message
def extracttext( rawmess ):
    outstring = re.findall(r":!.*",rawmess)[0]
    outstring = re.findall(r" .*",outstring)[0]
    outstring = outstring.replace('@','')
    return outstring

# Speak text
def speak( phrase ):
    engine.say( phrase )
    engine.runAndWait()

# Bot class, encapsulates event capture and command responses
class Bot(commands.Bot):

    def __init__(self):
        super().__init__(irc_token=config_token, client_id=config_client_id, nick=config_nick, prefix=config_prefix,
                         initial_channels=[config_channel])

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | User {self.nick} | Channels {self.initial_channels}')

    async def event_message(self, message):
        print(message.content)
        await self.handle_commands(message)

    # Commands use a different decorator
#    @commands.command(name='greet')
#    async def my_command(self, ctx):
#        await ctx.send(f'Hello there {ctx.author.name}!')
##        await ctx.send(f'RAW_DATA: {ctx.message.raw_data}')
#        speak("Hello there " + ctx.author.name )

#    @commands.command(name='test')
#    async def my_command(self, ctx):
#        speak("You invoked " ctx.command)


    @commands.command(name='so')
    async def my_command_shoutout(self, ctx):
        await ctx.send( "Shout out to " + extracttext( ctx.message.raw_data ) )
        speak( "Shout out to " + extracttext( ctx.message.raw_data ) )

    @commands.command(name='bits')
    async def my_command_bits(self, ctx):
        await ctx.send( "Thanks for the bitties " + extracttext( ctx.message.raw_data ) )
        speak( "Thanks for the bitties " + extracttext( ctx.message.raw_data ) )

    @commands.command(name='speak')
    async def my_commandspeak(self, ctx):
        await ctx.send( extracttext( ctx.message.raw_data ) )
        speak( extracttext( ctx.message.raw_data ) )

    @commands.command(name='info')
    async def my_commandinfo(self, ctx):
        await ctx.send(f'Hello {ctx.message.author.name} !')
        print(f'ID     : {ctx.message.author.id}')
        print(f'User   : {ctx.message.author.name}')
        print(f'Is Mod : {ctx.message.author.is_mod}')
        print(f'Badges : {ctx.message.author.badges}')

bot = Bot()
bot.run()