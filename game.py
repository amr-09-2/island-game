class IslandGame:

    def __init__(self):
        print("Game started...")

    def start(self):
        print("WELCOME TO MY ISLAND ☠️")
        print("You see 2 doors: red 🚪 and blue 🚪")

        door = input("choose a door: ").lower()

        if door == "red":
            self.red_room()
        elif door == "blue":
            print("you enter a room with crocodiles 🐊")
            print("Game Over")
        else:
            print("wrong choice bro ❌")

    def red_room(self):
        print("Nice you choose red door")
        box = input("choose a box (white, black, green): ").lower()

        if box == "green":
            print("you win the treasure 💰")
        elif box == "black":
            print("snakes everywhere 🐍 you lose")
        elif box == "white":
            print("spiders attack 🕷️")
        else:
            print("invalid box")

game = IslandGame()
game.start()
