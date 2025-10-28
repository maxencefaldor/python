class Monster:
    def __init__(self):
        print("Initialising Monster.")

    def roar(self):
        return "roaring"

    def kick(self):
        return "kicking"

    def move(self):
        return "moving"

    def sleep(self):
        return "sleeping"

    def attack(self):
        print(self.move())
        print(self.roar())
        print(self.kick())
        print(self.roar())
        print(self.sleep())


if __name__ == "__main__":
    monster = Monster()
    monster.attack()
