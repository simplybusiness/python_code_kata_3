
class Turnstile:
    def __init__(self):
        self.state = False

    def turnstile(self):
        return 

    def cross(self):
        current_state = self.state
        self.state = False
        return current_state

    def insert_coin(self):
        self.state = True