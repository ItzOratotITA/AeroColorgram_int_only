import rich
from rich.console import Console

console = Console()
printconsole = console.print
cin = console.input

supported_colors = ("bright_red", "bright_green", "bright_yellow", "bright_blue", "bright_magenta")

printconsole("""[bold]Welcome to AeroColorgram!
Supported colors:[/bold]""")

for color in supported_colors:
    printconsole(f"[{color}]{color}[/{color}]")

items_num = range(1, int(cin("How much items do you want to include? ")) + 1 )
items = []
items_colors = []

for num in items_num:
    items.append(int(cin(f"Insert percent for item {num} (don't type '%'): ")))
    items_colors.append(cin(f"Insert color for item {num}: "))

printconsole("What i understood:")
items_length = list(range(len(items)))

printconsole(items_length) #debug

for num in items_length:
    printconsole(f"Percent: {items[num]}% Color: [{items_colors[num]}]{items_colors[num]}[/{items_colors[num]}]")
