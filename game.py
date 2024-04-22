from style import *
from player import *
from collections import *

prompts = {
    "intro0": "this is a game demo",
    "intro1": "Let's first show you how to play!",
    "intro2": "In this fantasy world, magic circles have their own logic",
    "intro3": "You, an inexperienced wind-type wizard is on an journey to explore the Great Forrest",
    "intro4": "In the Great Forrest, there are thousands of monsters and threats awaiting for you",
    "intro5": "In order to protect yourself, you must make your own magic",
    "intro6": "Magic circles requires both careful calculations and experience",
    "intro7": "Let's cook a magic circle"
}

outputs_stack = deque(["intro" + str(i) for i in range(7)])

def output_handler(*inputs):
    print(*inputs, end=" ")

def start():
    name = input("Enter your name to start: ")
    player = Player(name)
    while outputs_stack:
        output_handler(prompts[outputs_stack.popleft()])
        _ = input()
    circle_tutorial(player)

def circle_tutorial(player):
    output_handler("You have", styles["mana"](f"{player.mana} mana"))

def create_circle(player):
    return

