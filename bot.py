# (c) 2023 SPET-PV. All rights reserved.
# This is an open-source Discord Currency Conversion Bot that utilizes the 
# Discord API and https://github.com/fawazahmed0/currency-api API.
# Source code and licensing information 
# available at: https://github.com/SPET-PV/
# Licensed under the MIT License. See LICENSE file for details.


# Packages and Libraries

# Built-In Modules
import os
import datetime
import time
import platform
# External Modules
import discord
from colorama import Fore, Style, Back
from dotenv import load_dotenv # Secure Enviorenemnt
from discord.ext import commands
# Local Modules
from logic import get


def run_bot():
    # Loading the Discord (TOKEN/KEY) with dotenv 
    load_dotenv()
    discord_token = os.getenv('TOKEN')

    # BOT configs
    intents = discord.Intents.all()
    intents.message_content = True
    client = commands.Bot(command_prefix="/", intents=intents)
    current_time = time.gmtime()
#-----------------------------------------------------------------------------
    # Launch Response
    @client.event
    async def on_ready():
        prfx = (Back.BLACK + Fore.GREEN +
            time.strftime("%Y-%m-%d - %H:%M:%S UTC",current_time)
            + Back.RESET + Fore.WHITE + Style.BRIGHT)
        print(prfx + " Logged in as " + Fore.YELLOW + client.user.name)
        print(prfx + " Bot ID " + Fore.YELLOW + str(client.user.id))
        print(prfx + " Discord Version " + Fore.YELLOW + discord.__version__)
        print(prfx + " Python Version " + Fore.YELLOW +
              str(platform.python_version()))
        synced = await client.tree.sync()
        print(prfx + " Slash CMD's Synced " + Fore.YELLOW +
              str(len(synced)) + " Commands")

    # Commands

    ## Shutdown Command
    @client.tree.command(name="shutdown")
    async def shutdown(interation:discord.Interaction):
        print(Fore.RED +'The bot is shutting down')
        await interation.response.send_message(content='The bot '
                                               'is shutting down...')
        await client.close()
    
    ## Currency Command
    @client.tree.command(name="Currency",
                         description="This command convert currencies "
                         "with their codes (e.g., 'USD' to 'EUR').")
    async def currency(interaction:discord.Interaction,
                       fromcurrency:str,
                       tocurrency:str,
                       amount:str):
        try:
            # Split the string into a list of substrings based on whitespace
            values = get(fromcurrency,tocurrency,amount).split()
            # Assign the values to separate variables
            conversion = values[0]
            date = values[1]

            # Creation of the embed        
            embed = discord.Embed(color= discord.Color.blue(),
                                  title='Currency Exchange Conversion',
                                  type='rich')
            
            embed.add_field(name="Conversion : ", value=f'''{str(amount)}\
            {fromcurrency.upper()} = {conversion} {tocurrency.upper()}''')
            
            embed.set_footer(text=f'\'{date}\' Currency Exchange Rates')
            
            # Sending the Requested data
            await interaction.response.send_message(embed=embed,
                                                    ephemeral=True)
            
            # Console Logs
            print(Fore.GREEN + f'Request: {fromcurrency.upper()} to '
            f'{tocurrency.upper()} ({str(amount)})' + Fore.WHITE)
        
        # Error Cases
        except Exception as e:
            # Sending an error message
            await interaction.response.send_message('Oops, their is a ' 
                           'problem. Verify your inputs or retry later.'
                                                    , ephemeral=True)
            
            # Error Console Logs
            print(Fore.RED + f'{e}' + Fore.WHITE) 

    # Run the Bot
    client.run(discord_token)
