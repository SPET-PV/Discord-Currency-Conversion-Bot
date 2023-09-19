# Discord Weather Bot
- The Discord Currency Bot is a simple utility bot that provides real-time currency conversion rates. It can convert currencies based on the latest exchange rates from a trusted source (https://github.com/fawazahmed0/currency-api).

# Commands:
- `/currency [fromCurrency] [toCurrency] [amount]`: Use this command to convert an amount from one currency to another. Replace `[fromCurrency]`, `[toCurrency]`, and `[amount]` with the appropriate values to perform the conversion.
- `/shutdown`: Shutdown the bot.

# Requirements 🧾
- A Discord Bot (create one using the [Discord developer portal](https://discord.com/developers/applications))
- Python 3.10 or above (https://www.python.org/downloads)
  - Recommended version [3.10.2](https://www.python.org/downloads/release/python-3102/)
- A Discord server that you own.
  - Make sure to "enable community" in your server if you haven't already! (`Settings` -> `Enable Community`)

# Installation 🚀
## Step 01 :
- Install `requirements.txt` with the command below 
```
pip install -r requirements.txt
```
> If you are on Windows, you might need to run command prompt as Administrator

## Step 02 :
- In the `.env` file, place your Discord Token in the TOKEN field.
```
TOKEN=''
```

## Step 03 :
- Execute the main.py file and patiently await the bot's majestic launch.
