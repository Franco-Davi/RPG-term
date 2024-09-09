from rich.panel import Panel
from rich.layout import Layout

full = Layout()
two_col = Layout()
two_row = Layout()


cmd = {
    # help for commands
    "help": Panel("""This is the [green]help menu[/green]. To use it more effectively, type '[bright_black]help <desired command>[/bright_black]' to learn more about the command. For a complete list of usable commands by game mechanics, type '[bright_black]help <desired mechanic>[/bright_black]'. For a full list of game mechanics for reference, type '[bright_black]help mechanics[/bright_black]' or consult the manual.""", title="[green]Welcome to help menu![/green]"),
    "echo": Panel(""" OI"""),
    "screen": Panel(""" """),
    "save": Panel(""" """),
    "load": Panel(""" """),
    "quit": Panel(""" """),
    # help for mechanics

    # help for moments

}
class Help():
    def __init__(slef):
        ...

    def help(self, command):
        return cmd[command]