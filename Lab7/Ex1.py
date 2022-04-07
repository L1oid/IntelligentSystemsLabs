class BigBell:
    def __init__(self):
        self.check = True
    def sound(self):
        if self.check:
            print("ding")
            self.check = False
        else:
            print("dong")
            self.check = True

bell = BigBell()
bell.sound()
bell.sound()
bell.sound()
