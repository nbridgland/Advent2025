class Dial:
    def __init__(self):
        self.value = 50

    def turn(self, direction: int, steps: int):
        self.value += direction*steps
        self.value %= 100


if __name__ == "__main__":
    with open("day1_input.txt") as f:
        data = f.read()
        turns = data.split('\n')
        dial = Dial()
        count_zeros = 0
        for turn in turns:
            if turn[0] == 'L':
                dial.turn(-1, int(turn[1:]))
            elif turn[0] == 'R':
                dial.turn(1, int(turn[1:]))
            if dial.value == 0:
                count_zeros += 1
    print(count_zeros)