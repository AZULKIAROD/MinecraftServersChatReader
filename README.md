# Minecraft Terminal Chat Bot

A simple Node.js and Python-based Minecraft bot that connects to a specific server, displays the in-game chat directly in your terminal, and allows you to send messages back to the server from your console.

## 📋 Features

* **Live Chat Bridge:** Read server chat logs in real-time within your terminal.
* **Interactive Console:** Type messages or commands (like `/login`) directly into the terminal to make the bot speak in-game.
* **Automated Connection:** Automatically handles spawning and basic error reporting.

## 🛠️ Prerequisites

Before running the script, make sure you have the following installed on your system:

1. **Python 3.8 or higher**
2. **Node.js (v14 or higher)** - Required by the `mineflayer` JavaScript library wrapper.

## 🚀 Installation

1. **Clone or download** this repository to your local machine.
2. Install the required Python packages and Node dependencies by running:

```bash
pip install javascript
npm install mineflayer
```

⚙️ Configuration
Open the script file (MinecraftServersChatReader.py) and modify the following configuration constants at the top of the file:

``` Python
SERVER_IP = 'SERVER_HERE'     # Replace with your target Minecraft server IP
SERVER_PORT = 25565           # Replace with the server port (Default: 25565)
BOT_NICK = 'YOUR_NICK_HERE'   # Replace with the bot's username/nickname
```

⚠️ Note: The bot is currently configured for Minecraft version 1.20.2. If your server uses a different version, make sure to update the 'version' field inside the mineflayer.createBot initialization block.

💻 Usage
Run the script using Python:

```Bash
python MinecraftServersChatReader.py
```

How to interact:
Once the terminal prints [+] Bot <Nick> ready and connected!, you can start typing.

Anything you type into the terminal and press Enter will be sent as a chat message or command by the bot in the server.

To safely disconnect and close the bot, press Ctrl + C in your terminal.
