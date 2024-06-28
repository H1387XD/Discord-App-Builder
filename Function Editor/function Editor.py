from tkinter import *
root=Tk()
root.geometry("20x20")
debug=Text(root)
commandName=Entry(root)
dropdown=StringVar()
dropdown.set("0")
commandMode=OptionMenu(root,dropdown,*["0","1","2","3"])
commandName.pack()
commandMode.pack()
commandResponse=Entry(root)
commandResponse.pack()
def createCodeCommand():
	global debug
	global commandsCreated
	if commandName in commandsCreated:
		debug.insert("1.0","\nCommand Already Exists, Please restart if you recently cleared!")
		return
	with open("funcs.ini","r") as f:
		d=f.read()
	starter=d+"\n"
	if d=="":
		starter=""
	with open("funcs.ini","w") as f:
		a=str(commandName.get())
		debug.insert("1.0",chars=f"\nCommand Created: {a}")
		commandsCreated.append(a)
		b=str(dropdown.get())
		c=str(commandResponse.get())
		f.write(f"{starter}{a},{b},{c}")
def clear():
	open("funcs.ini","w").close()
	global debug
	debug.insert("1.0",chars="\nCLEARED ALL commands, Restart To See Changes")
def compile():
	global debug
	debug.insert("1.0",chars="\nCompiling Code..")
def createCommand():
	global debug
	
	if commandName.get()=="":
		debug.insert("1.0",chars="\nNo Command Name Chosen!")
		return
	newLabel=Label(root,
		text=f"Command: {commandName.get()}"
	)
	newLabel.pack()
	createCodeCommand()

b=Button(
	root,
	text="Create Command",
	command=createCommand
)
b.pack()
commandsCreated=[]
with open("funcs.ini","r") as f:
		d=f.read()
		
for thing in d.split("\n"):
	if thing=="":
		continue
	newLabel=Label(root, text="Command: "+thing.split(",")[0])
	newLabel.pack()
	commandsCreated.append(thing.split(',')[0])
debug.pack(side=BOTTOM)
nb=Button(
	root,
	text="Compile",
	command=compile
)
cb=Button(
	root,
	text="Remove All Commands",
	command=clear
)
Label(root,text="Debug").pack(side=BOTTOM, anchor="w")
cb.pack(side=BOTTOM)
nb.pack(side=BOTTOM)

root.mainloop()