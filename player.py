class Player():

    class c_atr():
        def __init__(self):
            self.str = 0
            self.dex = 0
            self.con = 0
            self.int = 0
            self.wis = 0
            self.cha = 0


    class c_skill():
        def __init__(self):
            self.acrobatics = None
            self.animal_handing = None
            self.arcana = None
            self.athletics = None
            self.deception = None
            self.history = None
            self.insight = None
            self.intimidation = None
            self.investigation = None
            self.medicine = None
            self.nature = None
            self.perception = None
            self.performance = None
            self.persuasion = None
            self.religion = None
            self.sleight_of_hand = None
            self.stealth = None
            self.survival = None


    def __init__(self):
        self.name = ""
        self.race = ""
        self.background = ""
        self.level = 0
        self.exp = 0
        self.bonus = 0
        self.inventory = []
        self.spells = []

        self.atr = self.c_atr()
        self.skill = self.c_skill()


    def save(self):
        data = {
            "atr": self.atr.__dict__,
            "skill": self.skill.__dict__
        }
        return {**self.__dict__, **data}


    def mod(self, atr):
        mod = (atr - 10)/2
        return mod