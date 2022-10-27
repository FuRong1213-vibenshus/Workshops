# Discord API
## To start with
  
https://realpython.com/how-to-make-a-discord-bot-python/

>**What Is Discord?**
>Discord is a voice and text communication platform for gamers. Players, streamers, and developers use Discord to discuss games, answer questions, chat while they play, and much more. 

>**What is Bot?**
>Automated programs that look and act like users and automatically respond to events and commands on Discord are called bot users.

## Bot setup

https://github.com/FuRong1213-vibenshus/Workshops/blob/main/discord/Discord_Setup.docx
>- An **application** that your bot will use to authenticate with Discord’s APIs
>- A **bot user** that you’ll use to interact with other users and events in your guild
>- A **guild** in which your user account and your bot user will be active
>- A **Discord account** with which you created everything else and that you’ll use to interact with your bot


## Do it yourself 

And find the answer to the following questions:
- what is a client ?
- Why should we use environment variables to read the token ?

## Connection
> A **Client** is an object that represents a connection to Discord. A Client handles events, tracks state, and generally interacts with Discord APIs.

> **Event handler**: on_ready() will be called (and your message will be printed) once client is ready for further action. 

> **intents**: An intent basically allows a bot to subscribe to specific buckets of events. The events that correspond to each intent is documented in the individual attribute of the Intents documentation.
https://discordpy.readthedocs.io/en/stable/intents.html

## Responding to Events
An **event** is something that happens on Discord that you can use to trigger a reaction in your code. Your code will listen for and then respond to events.
There are two ways in discord.py to implement an event handler:
- Using the client.event decorator
- Creating a subclass of Client and overriding its handler methods


## Extra reading
- **Coroutines**
https://realpython.com/async-io-python/#the-asyncawait-syntax-and-native-coroutines