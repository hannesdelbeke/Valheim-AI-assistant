![image](https://github.com/hannesdelbeke/Valheim-AI-assistant/assets/3758308/750607ec-c725-4895-8694-9eea2073b664)

# Valheim-AI-assistant
Ask AI (Google Bard) questions what to make next in Valheim, by parsing your save data to Bard

## Instructions
This assumes you have a working python environment.
- point at your `.fch` save file
- ask a question
- add your bard token in the `.ini` file

### dependencies
- https://github.com/hannesdelbeke/valheim-character-editor-python
- [bardapi](https://github.com/dsdanielpark/Bard-API) (contains instructions on how to get a token)
- a Google account with access to [bard.google.com](https://bard.google.com/)

### Example
Asking Bard
```python
question = "I have the following items in the game valheim, what should i make next?"
question += " " + " ".join(inventory)
```
results in 
```
> Based on the items you have, here are some suggestions for what you could craft next:

**Flint Spear**: This is a simple but effective weapon that can be crafted with the materials you already have. It will be a big upgrade over your Club, and it will help you take down larger creatures.  
**Stone Axe**: This is a more powerful axe than your Flint Axe, and it will allow you to chop down trees and mine rocks more quickly.  
**Wooden Shield**: This will provide you with some protection from enemy attacks. It's a good idea to have one, especially if you're planning on exploring the Black Forest or the Swamp.  
**Workbench**: This is a crafting station that will allow you to craft more advanced items. You'll need to gather some more materials, but it's a worthwhile investment.  
**Raft**: This will allow you to explore the ocean. It's a good way to find new islands and resources.  

Ultimately, the best thing to craft next depends on your playstyle and what you're trying to achieve. But these are a few suggestions that will help you progress in the game.

...
Process finished with exit code 0  
```
⚠️ stone axe isn't better than flint, so you can't trust it to be always correct 


