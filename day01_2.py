class Dial:
    def __init__(self):
        self.value = 50
        self.clicks = 0

    def turn(self, direction: int, steps: int):
        if direction == 1:
            self.value += steps
            while self.value >= 100:
                self.clicks += 1
                self.value -= 100
        if direction == -1:
            if self.value == 0:
                self.clicks -= 1 # cause I'm about to count an extra click
            self.value -= steps
            while self.value < 0:
                self.value += 100
                self.clicks += 1
            if self.value == 0:
                self.clicks += 1

if __name__ == "__main__":
    with open("day1_input.txt") as f:
        data = f.read()
        turns = data.split('\n')
        dial = Dial()
        for turn in turns:
            if turn[0] == 'L':
                dial.turn(-1, int(turn[1:]))
            elif turn[0] == 'R':
                dial.turn(1, int(turn[1:]))
    print(dial.clicks)