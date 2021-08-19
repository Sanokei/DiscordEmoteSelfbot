#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import discord

import config
import images


# In[ ]:


class Client(discord.Client):
    async def on_connect(self):
        print(f"""
            Client has successfully logged in as {client.user.name}#{client.user.discriminator}
            Your discord ID is {client.user.id}
        """)
    
    async def on_message(self, message):
        if message.author != client.user:
            return
        
        if message.content.count(config.prefix) >= 2:
            emote_text = message.content
            emote_text_list = []
            for index in message.content.split(config.prefix):
                for image_name, image_value in images.emotes:
                    if emote_text.count(config.prefix) >= 2:
                        emote_text.replace(config.prefix+image_name+config.prefix,config.prefix+image_value+config.prefix)
                        emote_text_list = emote_text.split(config.prefix,2)
                        final_list = emote_text_list
                        emote_text = emote_text_list[2]
                        emote_text_list = []
                        
            await message.delete()
            await message.channel.send(text)
            
            for index,text in enumerate(emote_text_list[1::]):
                    if "https://cdn.discordapp.com/emojis/" not in text[index-1]:
                        emote_text_list[index-1 : index] = [reduce(lambda i, j: i + j, emote_text_list[index-1 : index])]   
            
            for text in emote_text_list:
                await message.channel.send(text)


# In[ ]:


client = Client()
try:
    client.run(config.token, bot = False)
except discord.LoginFailure:
    print("ERROR: Client failed to log in. [Invalid token]")
except discord.HTTPException:
    print("ERROR: Client failed to log in. [Unknown Error]")

