# Pilkki Booster

Boost your Propilkki 2 reaction time. **Useful for DIRTY cheaters like you!** 
Only works with default fishing tool.


Table of contents
=================
* [Process](#process)
* [Troubleshooting](#troubleshooting)


Process
============
1. Window frame must be defined in Pilkki.py using Mouse.py to get points
game = game.Game(x=166, y=187, x2=1441, y2=904, strategy=None)

2. Feature matcher detects fishing tool tip and adds offset.  
![tip](./images/detect_tool_tip.png) 

3. Handle part is detected /or are of it to be able to control pulling.  
![handle](./images/detect_tool_handle.png) 


Troubleshooting
============
* Game and script both needs administrator privileges to control mouse properly.
    * Clicks dont work without permissions.
* There might be some accessibility related permissions required to capture screen.

