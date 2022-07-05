


class Bank:
    def __init__(self, start = None):
        self.start = start
        self.animals = []
        if self.start:
            self.animals = ["l","l","l","w","w","w"]
    def __str__(self):
        return "{} lions and {} wildebeest \n".format(self.animals.count("l"), self.animals.count("w"))
    
    def check_state(self) -> bool:
        if self.animals.count("w") == 0:
            return True
        if self.animals.count("l") == 0:
            return True
        return self.animals.count("w") >= self.animals.count("l")
    
    def check_win(self) -> bool:
        return len(self.animals) == 6

class Boat:
    def __init__(self, side=True, num=0):
        self.side=side
        self.num=num
        self.right_bank = Bank(True)
        self.left_bank = Bank()
        self.curr_bank = self.right_bank
    
    def get_state(self):
        w = self.curr_bank.animals.count("w")
        l = self.curr_bank.animals.count("l")
        print(f"On the current bank there are {w} wildebeest and {l} lions")

        w = self.other_side().animals.count("w")
        l = self.other_side().animals.count("l")
        print(f"On the other bank there are {w} wildebeest and {l} lions")
    
    def other_side(self):
        if self.curr_bank == self.right_bank:
            return self.left_bank
        else:
            return self.right_bank

    def print_river(self):
        if self.side:
            print("|        <_>|")
            self.side = not self.side
            self.curr_bank = self.right_bank
        elif not self.side:
            print("| <_>       |")
            self.side = not self.side
            self.curr_bank = self.left_bank
        else:
            raise Exception("Unreachable")

    
boat = Boat()
rbank = Bank(start=True)
lbank = Bank()
l=["w","l"]
turns = 0
while True:
    print("")
    boat.print_river()
    print("")
    print(boat.curr_bank)
    get_input = True
    while get_input:
        get_input = False
        inp = str(input("> "))
        if len(inp.split()) > 2 or len(inp.split()) == 0:
            print("bad input, try again")
            get_input = True
        
        elif inp == "state":
            boat.get_state()
            get_input = True

        elif len(inp.split()) == 2:
            for animal in inp.split():
                if animal not in boat.curr_bank.animals:
                    print("bad input, try again")
                    get_input = True
                    break
                else:
                    boat.curr_bank.animals.remove(animal)
                    boat.other_side().animals.append(animal)
        else:
            if inp not in boat.curr_bank.animals:
                print("bad input, try again")
                get_input = True
            else:
                boat.curr_bank.animals.remove(inp)
                boat.other_side().animals.append(inp)
    if not boat.curr_bank.check_state():
        print(boat.curr_bank)
        raise ValueError("Game over you lost")
    if not boat.other_side().check_state():
        print(boat.other_side())
        raise ValueError("Game over, you lost")
    if boat.left_bank.check_win():
        print("You win")
        break
            
