from termcolor import colored

styles = {
    "default": lambda x: x,
    "wind": lambda x: colored(x, "green"),
    "mana": lambda x: colored(x, "magenta")
}

