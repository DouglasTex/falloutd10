class PlayerCharacter:

    def __init__(self, body=3, mind=3, spirit=3, skills=None, perks=None):
        # base stats
        self.body = body
        self.mind = mind
        self.spirit = spirit

        # life
        self.max_life = 5 + self.body
        self.current_life = self.max_life

        # posture
        self.max_posture = 5 + self.mind
        self.current_posture = self.max_posture

        # will
        self.max_will = 5 + self.spirit
        self.current_will = self.max_will

        self.caps = mind * 50
        self.hungry = 0
        self.radiation = 0

        if perks is None:
            self.perks = []
        else:
            self.perks = perks
        if skills is None:
            self.skills = []
        else:
            self.skills = skills

    # getters
    def get_caps(self):
        return self.caps

    def spend_caps(self, value):
        if value > self.caps or value < 0:
            return False
        self.caps -= value
        return True

    def receive_caps(self, value):
        if value < 0:
            self.caps += value

    def get_max_life(self):
        return self.max_life

    def get_current_life(self):
        return self.current_life

    def get_max_posture(self):
        return self.max_posture

    def get_current_posture(self):
        return self.current_posture

    def get_max_will(self):
        return self.max_will

    def get_current_will(self):
        return self.current_will

    # heal method
    def heal(self, value, attribute):
        if attribute == "life":
            self.current_life += value
            if self.current_life > self.max_life:
                self.current_life = self.max_life
        elif attribute == "posture":
            self.current_posture += value
            if self.current_posture > self.max_posture:
                self.current_posture = self.max_posture
        elif attribute == "will":
            self.current_will += value
            if self.current_will > self.max_will:
                self.current_will = self.max_will

    # Damage method
    def take_damage(self, damage, attribute):
        if attribute == "life":
            self.current_life -= damage
            if self.current_life < 0:
                self.current_life = 0
        elif attribute == "posture":
            self.current_posture -= damage
            if self.current_posture < 0:
                self.current_posture = 0
        elif attribute == "will":
            self.current_will -= damage
            if self.current_will < 0:
                self.current_will = 0

    # hungry methods
    def hungry_status(self):
        if self.hungry < self.body:
            return 'ok'
        elif self.hungry < self.max_life:
            return 'critical'
        else:
            return 'dead'

    def hungry_increase(self):
        self.hungry += 1

    def hungry_decrease(self):
        if self.hungry > 0:
            self.hungry -= 1

    # radiation methods
    def radiation_status(self):
        if self.radiation < self.mind:
            return 'ok'
        elif self.radiation < self.max_will:
            return 'critical'
        else:
            return 'dead'

    def radiation_increase(self, value=1):
        self.radiation += value

    def radiation_decrease(self, value=1):
        self.radiation -= value
        if self.radiation < 0:
            self.radiation = 0

    def to_string(self):
        return f"Corpo:    {self.body}   | Vida:    {self.max_life} \n" \
               f"Mente:    {self.mind}   | Postura: {self.max_posture} \n" \
               f"Espírito: {self.spirit}   | Vontade: {self.max_will} \n" \
               f"Perícias: {self.skills} \n" \
               f"Perks:    {self.perks} \n"
