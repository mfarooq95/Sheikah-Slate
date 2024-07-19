import discord
from discord.ext import commands
from pyrule_compendium import compendium
import json
import config # Holds Discord bot token

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(
    command_prefix = '!',
    intents = intents
)

@client.event
async def on_ready():
    print('We are connected and ready to go!')


@client.command(
        alias = ['Sheikahslate', 'sheikahslate', 'info', 'totk', 'totkinfo']
)
async def sheikahslate(ctx, *, user_request):
    api_input = user_request.replace(' ', '_')

    try:
        result_json_str_from_api = compendium().get_entry(api_input)
    except Exception as ex:
        await ctx.send(f'"{user_request}" not found in the Compendium. Please check the spelling and try again.')
        return
    
    json_from_api = json.loads(json.dumps(result_json_str_from_api))

    embed_object = discord.Embed(
        title = f"**{json_from_api['name'].title()}**",
        url = 'https://zelda.fandom.com/wiki/The_Legend_of_Zelda:_Breath_of_the_Wild',
        color = 0x60f8fd
    )

    embed_object.set_thumbnail(
        url = json_from_api['image']
    )

    properties_to_not_include = [
        'id',
        'name',
        'image',
        'description']
    
    for prop in json_from_api:
        if prop not in properties_to_not_include:
            formatted_value = await validate_prop_and_get_formatted_value(json_from_api[prop])
            if formatted_value is None:
                print(f"Unexpected type. Type = {type(json_from_api[prop])}")
                await ctx.send("Unexpected error! Please try again.")
                return
            embed_object.add_field(
                name = prop.replace('_', ' ').title(),
                value = formatted_value.title(),
                inline = True
            )

        embed_object.add_field(
            name = "Description",
            value = json_from_api['description'],
            inline = False
        )

        await ctx.send(embed = embed_object)

async def validate_prop_and_get_formatted_value(json_prop_value):
    type_returned_from_prop = type(json_prop_value)

    if type_returned_from_prop == type(None):
        formatted_value = "N/A"
    elif type_returned_from_prop in [int, float, complex]:
        formatted_value = str(json_prop_value)
    elif type_returned_from_prop == list:
        if len(json_prop_value) == 0:
            formatted_value = "N/A"
        else:
            formatted_value = "\n".join(json_prop_value)
    elif type_returned_from_prop == str:
        if json_prop_value == '':
            formatted_value = "N/A"
        else:
            formatted_value = json_prop_value
    
    else:
        formatted_value = None
    
    return formatted_value

if __name__ == "__main__":
    client.run(config.token)