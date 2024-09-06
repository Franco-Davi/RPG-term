import os
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
        self.logs = []
        self.command = None
        self.ticks = None

    def log(self, output=None):
        line = "[bright_black][{:05}]: [/bright_black]".format(self.ticks) + f'[bright_black]{self.command}[/bright_black]'
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
                    Layout(name="Menu", minimum_size=20),
                    Layout(name="Console", size=21)
                )
                layout["Header"].update(
                    Panel(Text("DEBUG", justify="center"))
                )
                layout["Footer"].update(
                    Panel(Text("Status", justify="right"))
                )
                layout["Right"].update(
                    Panel(Text("Satus Bar", justify="center"))
                )
                layout["Menu"].update(
                    Panel(Text("Menu", justify="left"))
                )
                layout["Console"].update(
                    Panel("Console\n" + "\n".join(self.logs))
                )
            case "START_SCREEN":
                layout.split(
                    Layout(name="Title")
                )
                layout["Title"].update(
                    Panel(Text(text2art("Start\nScreen"), style="blue"), border_style="blue")
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
        console.print("\n".join(self.logs))
        os.system('clear') or None
        console.print(layout)