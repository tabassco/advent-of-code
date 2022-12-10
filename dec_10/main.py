class Machine:
    def __init__(self) -> None:
        self.X = 1
        self.cycle_count = 0
        self.signal_strengths = []
        self.console = []

    def check_signal_strength(self):
        if (self.cycle_count - 20) % 40 == 0:
            self.signal_strengths.append((self.X * self.cycle_count, self.cycle_count))

    def add_console_print(self):
        self.console.append(self.create_current_position()[(self.cycle_count) % 40])

    def check_new_line(self):
        if (self.cycle_count) % 40 == 0 and self.cycle_count != 0:
            self.console.append("\n")

    def create_current_position(self):
        line = list("." * 40)
        for pos in range(self.X - 1, self.X + 2):
            line[pos] = "#"

        return line

    def next_cycle(self):
        self.add_console_print()
        self.cycle_count += 1
        self.check_signal_strength()
        self.check_new_line()

    def process_op(self, op: str):
        self.next_cycle()
        if op.startswith("addx"):
            _, value = op.rstrip("\n").split(" ")
            self.add_x(int(value))

    def add_x(self, value: int):
        self.next_cycle()
        self.X += value
        return None


if __name__ == "__main__":
    FILE_PATH = "dec_10/input.txt"

    machine = Machine()
    with open(FILE_PATH) as f:
        for line in f.readlines():
            machine.process_op(line)

    print(f"Signal Strength {sum([x for x, y in machine.signal_strengths])}")

    print("".join(machine.console))
