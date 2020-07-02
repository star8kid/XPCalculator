# XPCalculator

### A Tkinter Application that can be used to calculate various actions in the game *Minecraft* and return how long or how much exp is needed to reach certain levels. This will be useful for figuring out:

- How many *Bottle O' Enchantment* bottles are needed to raise you to a certain level
- Average range of time needed at a grinder to raise up to a certain level
- Many other features! ~~As suggested by peers~~

## Enjoy!

# Current Features

- `Calculate From Level Zero` is a feature that will calculate the total amount of experience needed when a player has a starting level of `0`. Though this feature isn't overally useful, it should still be included as an option because **math**.
- **No longer will you wonder, 'How long do I have to grind for?'**.`Grinding Duration` is a feature that will calculate the average of time needed to achieve a target level from a current level. This calculation will also require an input of an average exp gain rate, which will be measured in `ExperiencePoints/Second`. In order to get this number, use the following equation:
```
    Average Exp Gain = Total Amount of Exp Earned / Amount of Seconds that passed
```
- **Ever wonder how many exp bottles you'll need to take you to another level?** `XP Bottle Counter` is a feature that will take your current level and a target level and calculate how many Bottles o' Enchanting that you would need to reach the target level. *Note:* Bottles o' Enchanting have experience worth 3 to 11 points, meaning that there is a range of exp that a single Bottle o' Enchanting can dispense. Because of this there will be three calculations:

    - `Maximum Amount`: This is the amount of exp bottles that are required if you want to ***guarantee*** that you'll reach the target level. Because you want to be sure you'll reach the target, this number will always be the highest of the three.
    - `Average Amount`: This is the amount of exp bottles that you should be *expected* to accquire to reach the target level. However, there is no ***guarantee*** that you'll reach the target with the `Average Amount` of exp bottles, but if you want to risk it a little bit, this is the amount you'll need. 
    - `Minimum Amount`: This is the amount of exp bottles that you would need if each bottle gave the ***maximum*** amount of exp every smash. There is *no* reason to think you'd need this few amount of bottles, however, if you're willing to risk it, this is the smallest amount you could *possibly* get away with.


