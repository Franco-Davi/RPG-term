from read import Read
from screen import Screen
from player import Player
from help import Help

from rich.console import Console
from time import sleep
import json
import os

console = Console()
screen = Screen()
player = Player()
help = Help()

class Game():
    def __init__(self):
        self.debug = False
        self.running = True
        self.ticks = 0
        self.command = ""
        self.screen = "DEBUG"
    
    def run(self):
        self.screen = "START_SCREEN"
        screen.update(self.screen)
        sleep(2)
        self.screen = "DEBUG"
        while self.running:    
            self.tick()

    def promt(self):
        try:
            self.command = console.input("  >>>> ")
        except:
            screen.update("ERROR")
            sleep(1)

    def tick(self):
        screen.ticks = self.ticks
        screen.update(self.screen)
        self.promt()
        screen.command = self.command
        self.command_read()
        self.ticks = self.ticks + 1
        self.command = ""

    def command_read(self):
        try:
            args = Read.parser.parse_args(self.command.split())
            match args.command:
                case "help":
                    screen.printmenu = help.help(args.cmd)
                    screen.log("Showing help")
                case "quit":
                    screen.update("QUIT")
                    # Criar função de End()
                    exit()
                case "echo":
                    if args.message:
                        screen.log(" ".join(args.message))
                    else:
                        screen.log("No message provided.")
                case "screen":
                    screen.log(f"Alterando para {args.select}")
                    self.screen = args.select
                    screen.update(self.screen)
                case "save":
                    if args.file >= 1 and args.file <= 10:
                        self.save(args.file)
                    elif args.file == 0:
                        self.save("quick")
                    else:
                        screen.log("Slots on between 1 and 10")
                case "load":
                    if args.file >= 1 and args.file <= 10:
                        self.load(args.file)
                    elif args.file == 0:
                        self.load("quick")
                    else:
                        screen.log("Slots on between 1 and 10")
                case _:
                    screen.log(f"[red]Command not recognized[/red]")
        except ValueError as e:
            screen.log(f"[red]Argument error:[/red] [bright_black]{e}[/bright_black]")

    def save(self, slot):
        try:
            os.mkdir("save")
        except:
            pass
        save = {
            "game": self.__dict__,
            "screen": screen.__dict__,
            "player": player.save()
        }
        with open(f"./save/save-{slot}.json", 'w') as file:
            json.dump(save, file, indent=4)
        screen.log(f"Saved in slot {slot}")
    
    def load(self, slot):
        try:
            with open(f"./save/save-{slot}.json", 'r') as file:
                data = json.load(file)
            load = data["game"]

            self.debug = load["debug"]
            self.running = load["running"]
            self.ticks = load["ticks"] + 1
            self.command = load["command"]
            self.screen = load["screen"]

            load = data["screen"]

            screen.logs = load["logs"]
            screen.ticks = load["ticks"] + 1

            load = data["player"]

            player.name = load["name"]
            player.race = load["race"]
            player.background = load["background"]
            player.level = load["level"]
            player.exp = load["exp"]
            player.bonus = load["bonus"]
            player.inventory = load["inventory"]
            player.spells = load["spells"]

            load = data["player"]["atr"]

            player.atr.str = load["str"]
            player.atr.dex = load["dex"]
            player.atr.con = load["con"]
            player.atr.int = load["int"]
            player.atr.wis = load["wis"]
            player.atr.cha = load["cha"]

            load = data["player"]["skill"]

            player.skill.acrobatics = load["acrobatics"]
            player.skill.animal_handing = load["animal_handing"]
            player.skill.arcana = load["arcana"]
            player.skill.athletics = load["athletics"]
            player.skill.deception = load["deception"]
            player.skill.history = load["history"]
            player.skill.insight = load["insight"]
            player.skill.intimidation = load["intimidation"]
            player.skill.investigation = load["investigation"]
            player.skill.medicine = load["medicine"]
            player.skill.nature = load["nature"]
            player.skill.perception = load["perception"]
            player.skill.performance = load["performance"]
            player.skill.persuasion = load["persuasion"]
            player.skill.religion = load["religion"]
            player.skill.sleight_of_hand = load["sleight_of_hand"]
            player.skill.stealth = load["stealth"]
            player.skill.survival = load["survival"]
            screen.log(f"Loaded from slot {slot}")
        except:
            screen.log(f"[red]Error: slot {slot} not found[/red]")
