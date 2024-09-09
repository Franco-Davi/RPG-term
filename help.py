from rich.panel import Panel

cmd = {
    "help": Panel("""This is the [green]help menu[/green]. To use it more effectively, type '[bright_black]help <desired command>[/bright_black]' to learn more about the command. For a complete list of usable commands by game mechanics, type '[bright_black]help <desired mechanic>[/bright_black]'. For a full list of game mechanics for reference, type '[bright_black]help mechanics[/bright_black]' or consult the manual.""", title="[green]Welcome to help menu![/green]"),
    
    # help for mechanics

    # help commands

    "echo": Panel("""The [bright_black]echo[/bright_black] command simply echoes whatever you type and can also accept formatting from the Rich library.

[cyan]Arguments:[/cyan]""", title="[green]echo[/green]"),
    "screen": Panel(""" """),
    "save": Panel(""" """),
    "load": Panel(""" """),
    "quit": Panel(""" """),

    # help for moments

}
class Help():
    def __init__(slef):
        ...

    def help(self, command):
        return cmd[command]