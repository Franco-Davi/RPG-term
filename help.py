from rich.panel import Panel
from rich.box import SIMPLE

cmd = {
    "help": Panel("This is the [green]help menu[/green]. To use it more effectively, type '[bright_black]help <desired command>[/bright_black]' to learn more about the command. For a complete list of usable commands by game mechanics, type '[bright_black]help <desired mechanic>[/bright_black]'. For a full list of game mechanics for reference, type '[bright_black]help mechanics[/bright_black]' or consult the manual.\n\nType '[bright_black]help basic[/bright_black]' to see the basic game commands.", title="[green]Welcome to help menu![/green]", box=SIMPLE),
    
    # help for mechanics

    "basic": Panel("This is the list of basic commands:\n\n - [bright_blue]quit[/bright_blue]\n - [bright_blue]save[/bright_blue]\n - [bright_blue]load[/bright_blue]", title="[green]basic commands[/green]", box=SIMPLE),
    "debug": Panel("This is the list of debug commands:\n\n - [bright_blue]echo[/bright_blue]\n - [bright_blue]screen[/bright_blue]", title="[green]basic commands[/green]", box=SIMPLE),

    # help for commands

    "quit": Panel("The '[bright_black]quit[/bright_black]' command is used to exit the game.", title="[green]quit help[/green]", box=SIMPLE),
    "save": Panel("The '[bright_black]save[/bright_black]' command savas the game.\n\n[cyan]Arguments:[/cyan]\n\n    [bright_blue]file[/bright_blue]: Determines the slot that will save the game; not specifying this argument will generate a quick save.", title="[green]save help[/green]", box=SIMPLE),
    "load": Panel("The '[bright_black]load[/bright_black]' command loads the game.\n\n[cyan]Arguments:[/cyan]\n\n    [bright_blue]file[/bright_blue]: Determines the slot that will load the game; not specifying this argument will load the quick save.", title="[green]load help[/green]", box=SIMPLE),
    
    "echo": Panel("The '[bright_black]echo[/bright_black]' command simply echoes whatever you type and can also accept formatting from the Rich library.\n\n[cyan]Arguments:[/cyan]\n\n    [bright_blue]-m[/bright_blue], --message: Defines the message to be sent.", title="[green]echo help[/green]", box=SIMPLE),
    "screen": Panel("The '[bright_black]screen[/bright_black]' command is a debug mode command used to switch between screens.\n\n[cyan]Arguments:[/cyan]\n\n    [bright_blue]select[/bright_blue]: This command requires an input, which is the ID of the desired screen.", title="[green]screen help[/green]", box=SIMPLE),
}


class Help():
    def __init__(slef):
        pass

    def help(self, command):
        return cmd[command]