from os import system
from datetime import datetime
from art import text2art
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text

console = Console()
console = Console(
    width=console.size.width,
    height=console.size.height-1
)
layout = Layout()

class Screen():
    def __init__(self):
        self.ticks = None
        self.logs = []
        self.command = None
        self.printmenu = ""


    def log(self, output=None):
        log_time = datetime.now()
        log_time = log_time.strftime("%Y-%m-%d %H:%M:%S")
        line = "[bright_black][{:05} {}]: [/bright_black]".format(self.ticks, log_time) + f'[bright_black]{self.command}[/bright_black]'
        if output is not None:
            self.logs.insert(0, output)
        self.logs.insert(0, line)


    def update(self, layout_type="DEBUG"):
        match layout_type:
            case "DEBUG":
                layout.split(
                    Layout(name="Main")
                )
                layout["Main"].split_column(
                    Layout(name="Header",size=3),
                    Layout(name="Body"),
                    Layout(name="Footer",size=3)
                )
                layout["Body"].split_row(
                    Layout(name="Left", ratio=3),
                    Layout(name="Right", ratio=1)
                )
                layout["Left"].split_column(
                    Layout(name="Menu", size=20),
                    Layout(name="Console")
                )
                layout["Header"].update(
                    Panel(Text("DEBUG", justify="center"))
                )
                layout["Footer"].update(
                    Panel(Text(justify="right"), title="Status")
                )
                layout["Right"].update(
                    Panel(Text(justify="center"), title="Status")
                )
                layout["Menu"].update(
                    Panel(self.printmenu, title="Menu")
                )
                layout["Console"].update(
                    Panel("\n".join(self.logs), title="Console")
                )

            case "MAIN_MENU":
                layout.split(
                    Layout(name="Main")
                )
                layout["Main"].split_column(
                    Layout(name="Header",size=3),
                    Layout(name="Body"),
                    Layout(name="Footer",size=3)
                )
                layout["Body"].split_row(
                    Layout(name="Left", ratio=3),
                    Layout(name="Right", ratio=1)
                )
                layout["Header"].update(
                    Panel(Text("Main", justify="center"))
                )
                layout["Footer"].update(
                    Panel(Text(justify="right"), title="Status")
                )
                layout["Right"].update(
                    Panel(Text(justify="center"), title="Status")
                )
                layout["Left"].update(
                    Panel(self.printmenu, title="Menu")
                )

            case "START_SCREEN":
                layout.split_column(
                    Layout(name="Header", size=3),
                    Layout(name="Body")
                )
                layout["Header"].update(
                    Panel(Text("W E L C O M E", justify="center", style="bold blue"), border_style="blue")
                )
                layout["Body"].update(
                    Panel("\n  [blue]Welcome to the [reverse]terminal RPG![/][/blue]\n\n\n\n\n      To start a new game, type: '[bright_black]begin[/bright_black]'\n\n      To load an existing game, type: '[bright_black]load <slot>[/bright_black]'\n\n\n      To quit the game, type: '[bright_black]quit[/bright_black]'")
                )

            case "QUIT":
                layout.split(
                    Layout(name="Title")
                )
                layout["Title"].update(
                    Panel(Text(text2art("Quit\nScreen"), style="yellow"), border_style="yellow")
                )

            case "ERROR":
                layout.split(
                    Layout(name="Title")
                )
                layout["Title"].update(
                    Panel(Text(text2art("Error"), style="red"), border_style="red")
                )

            case _:
                layout.split(
                    Layout(name="Title")
                )
                layout["Title"].update(
                    Panel(Text(text2art("Screen\nError"), style="red"), border_style="red")
                )
                
        system('clear') or None
        console.print(layout)