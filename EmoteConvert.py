#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import discord

import config
import images


# In[ ]:


class Client(discord.Client):
    async def on_connect(self):
        os.system('clear')
        print(f"""
            Client has successfully logged in as {client.user.name}#{client.user.discriminator}
            Your discord ID is {client.user.id}
        """)
    
    async def on_message(self, message):
        if message.author != client.user:
            return
        
        if message.content.count(config.prefix) >= 2:
            emote_text_list = message.content.split(config.prefix)
            if message.content.count(config.prefix) % 2 == 1:
                last = emote_text_list[len(emote_text_list) - 1]
                emote_text_list.pop()
            for index,emote_text in enumerate(emote_text_list[::2]):
                for image_name, image_value in images.emotes:
                    if image_name in emote_text.lower().replace(" ",""):
                        emote_text_list[index] = image_value
            emote_text_list.append(last)
            await message.delete()
            
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

