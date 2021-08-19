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
            
            for image_name, image_value in images.emotes:
                if config.prefix+image_name+config.prefix in emote_text:
                        emote_text = emote_text.replace(config.prefix+image_name+config.prefix,"\\"+image_value+"\\")
                    final_list = emote_text.split("\\")
                        
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

