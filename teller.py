from rich.panel import Panel
from rich.layout import Layout
from rich.box import MINIMAL
import json

layout = Layout()

layout.split_column(
    Layout(name="Text"),
    Layout(name="Options")
)

class Teller():
    def __init__(self):

        self.moment = "Cena 1"
        self.id = 0

        self.text = ""
        self.options = []
        self.optionsTexts = []
        self.optionsIds = []
        self.optionsCommands = []

        with open("./game/strings.json", 'r') as file:
            self.data = json.load(file)

        self.choice = None

    def tell(self):

        try:

            self.text = self.data[self.moment][self.id][0]

            self.options = self.data[self.moment][self.id][1]

            self.optionsTexts = []
            for option in range(len(self.options)):
                self.optionsTexts.append(self.options[option][0])

            self.optionsIds = []
            for option in range(len(self.options)):
                self.optionsIds.append(self.options[option][1])

            self.optionsCommands = []
            for option in range(len(self.options)):
                self.optionsCommands.append(self.options[option][2])

            choices = ""

            for option in range(len(self.options)):
                choices = choices + "\n\n    " + f"[green]{option}[/green] - {self.optionsTexts[option]}"


            layout["Text"].update(
                Panel(self.text)
            )
            layout["Options"].update(
                Panel(choices, title="Choose:", box=MINIMAL)
            )

            return Panel(layout, title="", box=MINIMAL)

        except:
            self.moment = self.data["ERROR"]
            return Panel(self.moment, box=MINIMAL)