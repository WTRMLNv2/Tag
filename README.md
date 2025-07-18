# Tag Game
[Tag Logo](assets/TagLogo.png)

### This is a **Tag game** where there are two players - Red and Blue.
The players move with **WASD** and **Arrow Keys** (explained in the game's controls screen)
The player with the red arrow is **IT** and must touch the other player to remove the arrow.
The person with the IT Arrow at the end of the timer loses.

#### What libraries are required?
  1. PyGame

#### How to run?
Make sure the file structure stays intact and run **main.py**


#### Feature:
  1. 2 maps available: the snowy map and the savanna map
  2. Pressing T makes the Red player move faster for 10 seconds. Pressing M makes the Blue player move faster for 10 seconds
  3. Portals appear every 30 seconds, teleporting the players.
  4. Hidden platform in both maps.

#### Features in progress:
  1. Random Buff spawning every 30 seconds. It can be good like (speed, jump-boost, immunity to being it, etc) or bad like (slowness, get it without the other person touching, etc)
  2. More maps

#### Bugs:  
  1. No barriers on the side wall
  2. Touching the side of a platform makes your character go above the platform or below the platform
  3. When walking off the platform, the game thinks you are still on the ground and lets you jump midair (but the player is still affected by gravity)


Made with ❤️, debugged with 😭 by Ansh
