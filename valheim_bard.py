fch_path = r"C:\Program Files (x86)\Steam\userdata\31752593\892970\remote\characters\mr angie cgson.fch"





from valheim_char_parser import Character
from pathlib import Path
character = Character(Path(fch_path))

# for skill in character.skills:
#     print(skill.name, skill.level)

inventory = []
for item in character.inventory:
    inventory.extend([str(item.stack), str(item.name)])


# get token from config
import configparser
config = configparser.ConfigParser()
config.read('settings.ini')
token = config.get('API', 'bard_token')
print(token)

# ask question to bard
from bardapi import Bard
bard = Bard(token=token)
question = "I have the following items in the game valheim, what should i make next?"
# add inventory to question
question += " " + " ".join(inventory)
answer = bard.get_answer(question)['content']
print(answer)

