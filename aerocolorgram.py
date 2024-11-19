import rich
from rich.console import Console

console = Console()
printconsole = console.print
cin = console.input

supported_colors = (
    "bright_red",
    "bright_green",
    "bright_yellow",
    "bright_blue",
    "bright_magenta",
)

printconsole("[bold]Welcome to AeroColorgram!\n" "Supported colors:[/bold]")

for color in supported_colors:
    printconsole(f"[{color}]{color}[/{color}]")

printconsole(
    "[bold]For more colors visit https://rich.readthedocs.io/en/stable/appendix/colors.html[/bold]"
)

items_num = int(cin("How much items do you want to include? "))
items = []
items_colors = []

for idx in range(items_num):
    items.append(int(cin(f"Insert percent for item {idx} (don't type '%'): ")))
    items_colors.append(cin(f"Insert color for item {idx}: "))

printconsole("What i understood:")
items_length = list(range(len(items)))

printconsole(items_length)  # debug

for idx in items_length:
    printconsole(
        f"Percent: {items[idx]}% Color: [{items_colors[idx]}]{items_colors[idx]}[/{items_colors[idx]}]"
    )

item_data = list(zip(items, items_colors))
listona = []
for p, c in item_data:
    for j in range(p):
        listona.append(f"[{c}]■[/{c}]")

for i in range(0, 100, 10):
    printconsole("".join(listona[i : i + 10]))

cin("Press ENTER to quit. ")
