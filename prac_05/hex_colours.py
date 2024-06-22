COLOURS = {"cerise": "#de3163", "carolina blue": "#56a0d3", "carrot orange": "#ed9121", "castleton green": "#00563f", "cedar chest": "#c95a49", "celadon": "#ace1af", "celeste": "#b2ffff", "celtic blue": "#246bce", "cerulean frost": "#6d9bc3", "cg blue": "	#007aa5"}
print(COLOURS)
colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    print(f"The code for \"{colour_name}\" is {COLOURS.get(colour_name)}")
    colour_name = input("Enter a colour name: ").lower()

