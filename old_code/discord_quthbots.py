import discord ,config


class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged on as", self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == "ping":
            await message.channel.send("pong")

        if "how are you" in (message.content).lower():
            await message.channel.send("I am good thanks for asking!")


client = MyClient()
client.run(config.discord_token)
