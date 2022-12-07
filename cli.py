from itertools import cycle
from sys import argv

from rich import print

from lib import dec_to_bin, dec_to_hex

if not argv[1:]:
    quit()

text = " ".join(argv[1:])

COLORS = ["red", "navy_blue", "yellow", "green", "cyan", "bright_magenta"]
color_cycle = cycle(COLORS)

for char, color_cycle in zip(text, color_cycle):
    if char == " ":
        print(f"[{color_cycle} b]_", end="")
    else:
        print(f"[{color_cycle} b]{char}", end="")
print("")

color_cycle = cycle(COLORS)

for char, color_cycle in zip(text, color_cycle):
    print(f"[{color_cycle} b]{dec_to_bin(ord(char))}", end=" ")
print("")

color_cycle = cycle(COLORS)

for char, color_cycle in zip(text, color_cycle):
    print(f"[{color_cycle} b]{dec_to_hex(ord(char))}", end=" ")
