# to retrieve the public ip address of the server
# send discord message if it's changed
import requests
import csv
import discord
from datetime import datetime

def bot(new_ip):
    TOKEN = '' # TODO: add your unique discord token
    DISCORD_ID = '' # TODO: add your discord id
    CHANNEL_ID = '' # TODO: add your discord channel id
    client = discord.Client()

    @client.event
    async def on_ready():
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(f'<@{DISCORD_ID}>, looks like the public ip changed to: {new_ip}...')
        await client.close()

    client.run(TOKEN)

def pubip():
    now = datetime.now()
    dtstmp = now.strftime('%Y-%m-%d %H:%M:%S.%f')
    data = requests.get('https://ipinfo.io/ip')
    pubip = data.content.decode('utf-8')
    with open('ips.csv', 'r') as f:
        data = list(csv.reader(f))
    ip = data[-1][0]
    if pubip != ip:
        with open('ips.csv', 'a') as f:
            f.write(pubip)
        bot(pubip) # send discord message with the new public ip
        print(f'{dtstmp} | Public ip changed to {pubip}')

if __name__ == '__main__':
    pubip()
