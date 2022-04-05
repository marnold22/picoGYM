# Speeds-and-feeds

## FLAG: picoCTF{}

## Status: Incomplete

Category: Reverse-Engineering

Description: There is something on my shop network running at nc mercury.picoctf.net 20301, but I can't tell what it is. Can you?

> nc mercury.picoctf.net 20301
> nc mercury.picoctf.net 20301 > gcode.g

G Code Basics: (Credit to Dejan at <https://howtomechatronics.com/tutorials/g-code-explained-list-of-most-important-g-code-commands/>)

EXAMPLE:

G01 X247.951560 Y11.817060 Z-1.000000 F400.000000
G## X## Y## Z## F##

- First is the G-code command and in this case that’s the G01 which means “move in straight line to a specific position”
- Declare the position or the coordinates with the X, Y and Z values.
- F value we set the feed rate, or the speed at which the move will be executed

So we need to visualize the plotted points (ie use a g code visualizer)
I used this visualizer <https://ncviewer.com/> and pasted the g code from the file I generated earlier `gcode.g`

After plotting the image was the print of the flag:
picoCTF{num3r1cal_c0ntr0l_68a8fe29}