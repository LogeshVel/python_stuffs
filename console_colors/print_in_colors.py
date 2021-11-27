from rich.console import Console
from rich.color import ANSI_COLOR_NAMES


# to see the available colors
console = Console()
for col in ANSI_COLOR_NAMES:
    console.print(col,style=col,end='\t')
print('\n')

#custom print functions in our program
def print_red(data_to_print: str):
    console = Console()
    console.print(data_to_print,style='red')

print_red("Logesh in Red")

def print_green(data_to_print: str):
    console = Console()
    console.print(data_to_print,style='green')

print_green("Logesh in Green")
