import os
import time
from rich.console import Console
from os.path import exists
console = Console()

setup_done = exists(".setup-done-before")

if setup_done == True:
	console.log("[red]Setup was already completed! Please make sure you have to run this script again. If you have to, please delete the file .setup-done-before")
	exit()

console.log("Setup Assistant")

console.log(
	"You're in the setup wizard. Would you like to setup? [bold Green]y/n"
)

ensureSetupIsRequired = input("Are you sure you want to continue? > ").casefold()
if ensureSetupIsRequired != "y":
	console.log("[red]Exiting...")
	time.sleep(0.5)
	exit()
else:
	console.log("[bold red] This will overwrite your current settings. Are you sure you want to continue? [bold green]y/n")
	overwriteSettings = input("Are you sure you want to continue? > ").casefold()
	if overwriteSettings != "y":
		console.print("[red]Abort mission! Exiting...")
		time.sleep(0.5)
		exit()
	else:
		console.log("[bold green]Alright! Let's get started!")
		time.sleep(1)

console.log("Ensure you have the following ready to enter:")
console.log("[bold green]Reddit Client ID")
console.log("[bold green]Reddit Client Secret")
console.log("[bold green]Reddit User Agent")
console.log("[bold green]Reddit Discord Webhook URL")
time.sleep(0.5)
console.log("[green]If you don't have these, please follow the instructions in the README.md file to set them up.")
console.log("[green]If you do have these, type yes to continue. If you dont, go ahead and grab those quickly and come back.")
confirmUserHasCredentials = input("Are you sure you have the credentials? > ").casefold()
if confirmUserHasCredentials != "yes":
	console.log("[red]I don't understand that.")
	console.log("[red]Exiting...")
	exit()
else:
	console.log("[bold green]Alright! Let's get started!")
	time.sleep(1)


console.log("Enter your credentials now.")
cliID = input("Client ID > ")
cliSec = input("Client Secret > ")
user = input("User Agent > ")
URL = input("Discord Webhook URL > ")
time.sleep(0.5)
console.log("Removing old .env file...")
os.remove(".env")
time.sleep(0.5)
console.log("Creating new .env file...")
with open('.env', 'a') as f:
	f.write(f'REDDIT_CLIENT_ID="{cliID}"\n')
	time.sleep(0.5)
	f.write(f'REDDIT_CLIENT_SECRET="{cliSec}"\n')
	time.sleep(0.5)
	f.write(f'REDDIT_USER_AGENT="{user}"\n')
	time.sleep(0.5)
	f.write(f'DISCORD_WEBHOOK="{URL}"\n')

with open('.setup-done-before', 'a') as f:
	f.write("This file blocks the setup assistant from running again. Delete this file to run setup again.")

console.log("[bold green]Setup Complete! Returning...")

os.system("python3 main.py")