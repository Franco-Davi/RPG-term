from read import Read
from screen import Screen
from help import Help
from teller import Teller
from player import Player

from rich.console import Console
from time import sleep
import json
import os

console = Console()
screen = Screen()
player = Player()
help = Help()
teller = Teller()

class Game():
    def __init__(self):
        self.debug = False
        self.running = True
        self.ticks = 0
        self.command = ""
        self.screen = ""
        self.debug = True
        self.gameState = "START"
    

    def run(self):
        self.start()
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

    def start(self):
        self.screen = "START_SCREEN"
        screen.update(self.screen)

    def command_read(self):
        try:
            args = Read.parser.parse_args(self.command.split())

            match args.command:
                
                case "help":
                    try:
                        self.gameState = "HELP"
                        screen.printmenu = help.help(args.cmd)
                        screen.log(f"Showing {args.cmd} help")
                    except:
                        screen.log(f"No help for {args.cmd}")

                case "quit":
                    screen.log("Exiting the game")
                    screen.update("QUIT")
                    # Criar função de End()
                    self.running = False

                case "echo":
                    if args.message:
                        screen.log(" ".join(args.message))
                    else:
                        screen.log("No message provided.")

                case "screen":
                    if self.debug == True:
                        screen.log(f"Alterando para {args.select}")
                        self.screen = args.select
                        screen.update(self.screen)
                    else:
                        screen.log("You are not on debug mode")

                case "save":
                    if self.gameState != "START":
                        if args.file >= 1 and args.file <= 10:
                            self.save(args.file)
                        elif args.file == 0:
                            self.save("quick")
                        else:
                            screen.log("Slots on between 1 and 10")
                    else:
                        screen.log("Can't save on start screen")

                case "load":
                    if args.file >= 1 and args.file <= 10:
                        self.load(args.file)
                    elif args.file == 0:
                        self.load("quick")
                    else:
                        screen.log("Slots on between 1 and 10")

                case "continue":
                    screen.printmenu = teller.tell()
                    screen.log("Showing story menu")
                    self.gameState = "STORY"

                case "choose":
                    if self.gameState == "STORY":
                        teller.id = teller.options[args.choice][1]
                        screen.printmenu = teller.tell()
                        screen.log(f"Choosed {args.choice} option")
                    else:
                        screen.log("Can't choose out of story screen")

                case "begin":
                    if self.gameState == "START":
                        self.screen = "MAIN_MENU"
                        self.gameState = "STORY"
                        screen.log("Begining a new game")
                        # Levar para a criação de personagem
                        screen.printmenu = teller.tell()
                    else:
                        screen.log("Can't begin a new game now")

                case _:
                    screen.log(f"[red]Command not recognized[/red]")

        except ValueError as e:
            screen.log(f"[red]Argument error:[/red] [bright_black]{e}[/bright_black]")


    def save(self, slot):
        try:
            os.mkdir("save")
        except:
            pass

        screen.printmenu = ""
        data_teller = [teller.data]
        teller.data = ""

        save = {
            "game": self.__dict__,
            "screen": screen.__dict__,
            "player": player.save(),
            "teller": teller.__dict__
        }
        with open(f"./save/save-{slot}.json", 'w') as file:
            json.dump(save, file, indent=4)
        screen.log(f"Saved in slot {slot}")

        teller.data = data_teller[0]

        screen.printmenu = f"\n    Game Saved on slot {slot}, type '[bright_black]continue[/bright_black]' to continue"
    

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
            self.debug = load["debug"]
            self.gameState = load["gameState"]

            load = data["screen"]

            screen.ticks = load["ticks"] + 1
            screen.logs = load["logs"]
            screen.command = load["command"]
            screen.printmenu = load["printmenu"]
    
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

            load = data["teller"]

            teller.moment = load["moment"]
            teller.id = load["id"]
            teller.text = load["text"]
            teller.options = load["options"]
            teller.optionsTexts = load["optionsTexts"]
            teller.optionsIds = load["optionsIds"]
            teller.optionsCommands = load["optionsCommands"]

            screen.log(f"Loaded from slot {slot}")
            screen.printmenu = f"\n    Game loaded from slot {slot}, type '[bright_black]continue[/bright_black]' to continue"

        except:
            screen.log(f"[red]Error: slot {slot} not found[/red]")