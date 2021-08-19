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
            final_list = []
            
            for index in message.content.split(config.prefix):
                for image_name, image_value in images.emotes:
                    if emote_text.count(config.prefix) >= 2 and config.prefix+image_name+config.prefix in emote_text:
                        emote_text = emote_text.replace(config.prefix+image_name+config.prefix,"\\"+image_value+"\\")
                        emote_text_list = emote_text.split("\\")
                        final_list += emote_text_list
                        emote_text = emote_text_list[len(emote_text_list)-1]
                        emote_text_list = []
                        
            if(len(final_list) > 0):           
                await message.delete()
                
                for text in final_list:
                    if text != "":
                        await message.channel.send(text)


# In[ ]:


client = Client()
try:
    client.run(config.token, bot = False)
except discord.LoginFailure:
    print("ERROR: Client failed to log in. [Invalid token]")
except discord.HTTPException:
    print("ERROR: Client failed to log in. [Unknown Error]")

