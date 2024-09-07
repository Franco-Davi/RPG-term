class Player():

    class c_atr():
        def __init__(self):
            self.str = 0
            self.dex = 0
            self.con = 0
            self.int = 0
            self.wis = 0
            self.cha = 0

        @classmethod
        def from_dict(cls, data):
            # Constrói um objeto da classe `c_atr` usando o dicionário `data`
            return cls(**data)

    class c_skill():
        def __init__(self):
            self.acrobatics = 0
            self.animal_handing = 0
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
    
        @classmethod
        def from_dict(cls, data):
            # Constrói um objeto da classe `c_atr` usando o dicionário `data`
            return cls(**data)

    def __init__(self):
        self.name = ""
        self.race = ""
        self.background = ""
        self.level = 0
        self.exp = 0
        self.bonus = 0

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