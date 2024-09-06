from read import Read
from screen import Screen
from player import Player

from rich.console import Console
from time import sleep

console = Console()
screen = Screen()
player = Player()

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
            exit()

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
                case _:
                    screen.log(f"[red]Command not recognized[/red]")
        except ValueError as e:
            screen.log(f"[red]Argument error:[/red] [bright_black]{e}[/bright_black]")

        print("sim, roda!")