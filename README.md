# Sheikah Slate


## Overview
Sheikah Slate is a Discord bot that takes in user requests for information and data on in-game objects from The Legend of Zelda: Breath of the Wild through a ping system. The bot uses a third-party API to gather its informaiton, parses and alters the information and returns it in an embed object in the channel it was called in.

## Libraries & Dependencies

| Dependency                |                Description                                                                 | 
| :-------------:           |                :-------------                                                              |
|   **discord.py**          | *To create and operate a discord-compliant bot*                                            |
|   **json**                | *Required to parse json data from the API*                                                 |
|   **pyrule-compendium**   | *An API wrapper to easily communicate with the API that handles the data information*      |

> ❗️ **NOTE**
>
> A Discord bot token is required. This is a secret and can be stored in a config file or some other way as an environment variable.

## Installation
Simply clone or download the main.py file, install the dependencies, and run the code locally for testing or host the bot's code online to have it running without your local machine.

### Usage & Details
It's important to note that the bot uses a ping system wherein the bot looks for user requests sent to a channel in servers it operates in with the prefix `!` and one of the listed aliases such as `Sheikahslate`. Below is the full list of aliases the bot is set to respond to. These aliases are what users in the Discord server may type, along with the ping prefix, to call the bot to execute its function.

**Aliases**:
+ *Sheikahslate*
+ *sheikahslate* 
+ *info*
+ *totk*
+ *totkinfo*

The bot's aliases can be updated in the `main.py` file under line 21, in the list passed to the `alias` parameter. See below:

```python
@client.command(
        alias = ['Sheikahslate', 'sheikahslate', 'info', 'totk', 'totkinfo']
)
```

## Post-MVP
While the bot is now functional and can be invited to servers and handle user requests to return data on game objects from The Legend of Zelda: Breath of the Wild, the data that is returned is rudimentary and only tied to Breath of the Wild as the bot connects to `pyrule-compendium`, an API and its wrapper to make the necessary GET requests to gather data. The current goal is to create my own API that will serve The Legend of Zelda: Tears of the Kingdom's object data which can be far more detailed and robust, giving both users of the API access to detailed backend data on all game objects in the latest entry as well as allowing this Discord bot to serve even more detailed information on game objects.

This API is currently being developed and will be visible in its own repo on GitHub.

Along with the major change to the bot with the new API, I'd also like to eventually update the bot to utilize a logger, to track errors. From there, it'd be best to account for error-handling with both detailed error messages and bot functionality, to prevent breaking.
