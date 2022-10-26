import discord

TOK_FILE = "token.txt"

fav_emojis = {}
reacts = {}

def get_token():
  tokfile = open(TOK_FILE, 'r')
  token = tokfile.read()
  tokfile.close()
  return token

client = discord.Client()

@client.event
async def on_ready():
    print("Connected!")

@client.event
async def on_message(message):
    contents = message.content
    userid = message.author.id
    if contents.startswith("!echo "):
        rem = contents[6:]
        reply = "Du sendte: " + rem
        print(rem)
        emoji = "\N{EYES}"
        if userid in fav_emojis:
            emoji = fav_emojis[userid]
        await message.add_reaction(emoji)
        await message.channel.send(reply)
    elif contents.startswith("!setemoji "):
        rem = contents[10:]
        fav_emojis[userid] = rem
    elif contents == "!reacts":
        msg = ""
        for (k, v) in reacts.items():
            msg += f"{k} : {v}\n"
        await message.channel.send(msg)


@client.event
async def on_reaction_add(reaction, user):
    if user == client.user:
        return
    emoji = reaction.emoji
    chan = reaction.message.channel

    if emoji in reacts:
        reacts[emoji] += 1
    else:
        reacts[emoji] = 1

    msg_text = f"<@{user.id}> reacted to a message with {emoji}"
    msg = await chan.send(msg_text)

token = get_token()
client.run(token)

