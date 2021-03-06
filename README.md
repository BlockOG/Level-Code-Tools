## This tool is deprecated, please use [BlockOG/cell_machine_levels](https://github.com/BlockOG/cell_machine_levels) instead.

# Level Code Tools
This is github repository contains a couple useful Cell Machine Mystic Mod tools

If you find any issue report them in the [Issues Tab](https://github.com/BlockOG/Level-Code-Tools/issues)

To use the tools [download python](https://www.python.org/downloads/) if you're on windows

Then download the code

![Screenshot from 2021-07-14 14-55-10](https://user-images.githubusercontent.com/68442822/125618377-cadd57ed-22d8-4cbc-a933-216afa529ddb.png)

Extract the zip file, then open the directory you extracted it to in cmd/terminal and type

```
python toolName.py
```

On some OSes it's `python3` so try that too

If you want to have colored text that I built into it then do

```
pip install termcolor
pip install colorama
```

It may be `pip3` on some OSes

And if you want a GUI for the encoder tool you can do

```
pip install pysimplegui
```

And if you don't already have numpy for some reason, install it

```
pip install numpy
```

## Level Code Optimizer
A Mystic Mod level code optimizer

Changes all rotators, push cells, walls, enemies and trash cells to be their default rotation and changes the rotation of slide cells a bit

There might at some point be V2 support

## Level Code Converter
A Mystic Mod level code converter

Converts V1 codes to V3 codes

## V3 Code Compresses
This tool isn't so useful for V3 codes it's mostly used in the other tools

## Encoder/Decoder
Encodes a number into base 74

Decodes a string from base 74
