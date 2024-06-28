import sys
import os
if len(sys.argv)<3:
	quit("Segmentation Fault")
BOT_TOKEN=None
BOT_PREFIX=None
BOT_STATUS=None
BOT_HAS_DEFAULT_HELP_COMMAND=True
botHelper={"False":True, "True":False}
#TEST FOR CONFIG
try:
	open(sys.argv[1], 'r').close()
except:
	quit(f"Invalid CONFIG File: app.config Instead of {sys.argv[1]}")


with open(sys.argv[1], 'r') as f:
	config=f.read()

#TEST FOR FUNCTIONS

try:
	open(sys.argv[2], 'r').close()
except:
	quit(f"Invalid FUNCS File: funcs.dbb Instead of {sys.argv[2]}")

with open(sys.argv[2], 'r') as f:
	funcs=f.read()

for settings in config.split('\n'):
	setting = settings.split('=')
	if len(setting)==1:
		quit(f"Invalid CONFIG File: Setting Has No Argument : {setting}")
	settingConfig=setting[0]
	argument=setting[1]

	if settingConfig not in ["Prefix","Token","Status","NoDefaultHelpCommand"]:
		quit(f"Invalid CONFIG File: Invalid settingConfig : {settingConfig}")
	if settingConfig=="Prefix":
		BOT_PREFIX=argument
	if settingConfig=="Token":
		BOT_TOKEN=argument
	if settingConfig=="Status":
		BOT_STATUS=argument
	if settingConfig=="NoDefaultHelpCommand":
		BOT_HAS_DEFAULT_HELP_COMMAND=botHelper[argument]
open("output.py", "w").close()



output=open("output.py", 'w')
output.write("import discord\nfrom discord.ext import commands\nintents = discord.Intents.all()\nclient = commands.Bot(command_prefix=\"")
output.write(BOT_PREFIX+"\", intents=intents)")
if not BOT_HAS_DEFAULT_HELP_COMMAND:
	output.write("\nclient.remove_command('help')\n")
if BOT_STATUS is None:
	output.write("""
@client.event
async def on_ready():
	print(f"Logged in as {client.user.name}")
""")
else:
	output.write("""
@client.event
async def on_ready():
	print(f"Logged in as {client.user.name}")
	await client.change_presence(activity=discord.CustomActivity(name='"""+BOT_STATUS+"'))\n")
template="@client.command()\nasync def "
templateEnd="(ctx, member : discord.Member):\n\t"
templateEnd2="(ctx):\n\t"
os.system('cls')
for function in funcs.split("\n"):
	functionCode=function.split(",")
	if len(functionCode)<3:
		print("Invalid Function: "+function)
		output.close()
		quit("Correct Function Usage: [FunctionName],[MODE],[MessageReply]")
	functionName,functionMode,functionReply=functionCode
	print("CREATING Function: "+functionName)
	if functionMode=="0":
		output.write(f"{template}{functionName}{templateEnd2}await ctx.send(\"{functionReply}\")\n")
	if functionMode=="1":
		output.write(f"{template}{functionName}{templateEnd}await member.ban()\n\tawait ctx.send(\"{functionReply}\")\n")
	if functionMode=="2":
		output.write(f"{template}{functionName}{templateEnd}await member.kick()\n\tawait ctx.send(\"{functionReply}\")\n")
output.write(f"client.run(\"{BOT_TOKEN}\")")

output.close()
os.system('cls')
print("Completed Compiling\nRunning Bot")
