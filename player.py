
class Player():

    class atr():
        def __init__(self):
            self.str = 0
            self.dex = 0
            self.con = 0
            self.int = 0
            self.wis = 0
            self.cha = 0

    class skill():
        def __init__(self):
            self.acrobatics = 0
            self.anima_handing = 0
            self.arcana = 0
            self.athletics = 0
            self.deception = 0
            self.history = 0
            self.insight = 0
            self.intimidation = 0
            self.investigation = 0
            self.medicine = 0
            self.nature = 0
            self.perception = 0 
            self.performance = 0
            self.persuasion = 0
            self.religion = 0
            self.sleight_of_hand = 0
            self.stealth = 0
            self.survival = 0

    def __init__(self):
        self.name = ""
        self.race = ""
        self.background = ""
        self.level = 0
        self.exp = 0
        self.bonus = 0

    def mod(self, atr):
        mod = (atr - 10)/2
        return mod