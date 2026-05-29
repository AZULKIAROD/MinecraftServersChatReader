import sys
import threading
import time
from javascript import require, On #Install: "pip install javascript", Install Node.js to: "npm install mineflayer"

mineflayer = require('mineflayer')

SERVER_IP = 'SERVER_HERE' # Replace with your target Minecraft server IP
SERVER_PORT = 25565 # Replace with the server port (Default: 25565)
BOT_NICK = 'YOUR_NICK_HERE' # Replace with the bot's username/nickname

bot_ready = False

print(f"[*] Connecting to server {SERVER_IP}:{SERVER_PORT} as '{BOT_NICK}'...")

bot = mineflayer.createBot({
    'host': SERVER_IP,
    'port': SERVER_PORT,
    'username': BOT_NICK,
    'version': '1.20.2' #Change the version if necessary
})

bot.plugins = {}

@On(bot, 'spawn')
def handle_spawn(*args):
    global bot_ready
    time.sleep(2)
    bot_ready = True
    print(f"\n[+] Bot {BOT_NICK} ready and connected!")

@On(bot, 'messagestr')
def handle_message(this, message, position, jsonMsg, *args):
    if not message.strip() or "chunk" in message.lower():
        return
    print(message)

@On(bot, 'error')
def handle_error(this, err):
    if "node" not in str(err).lower():
        print(f"[-] Error: {err}")

@On(bot, 'end')
def handle_end(*args):
    print("[-] The bot was disconnected from the server.")
    sys.exit()

def listen_terminal():
    while True:
        try:
            message = input()
            if message.strip():
                if not bot_ready:
                    print("[*] Please wait for the bot to fully spawn...")
                    continue

                bot.chat(message)
        except (KeyboardInterrupt, EOFError):
            print("\n[*] Closing the bot...")
            bot.quit()
            break

thread_terminal = threading.Thread(target=listen_terminal, daemon=True)
thread_terminal.start()
