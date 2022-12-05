from collections import deque


class Storage:
    def __init__(self, initial_loadout: list[deque[str]]) -> None:
        self.loadout = initial_loadout

    def handle_change_operation(
        self, amount: int, from_stack: int, to_stack: int
    ) -> None:
        for _ in range(amount):
            move = self.loadout[from_stack - 1].pop()
            self.loadout[to_stack - 1].append(move)

    def handle_multi_move_operations(
        self, amount: int, from_stack: int, to_stack: int
    ) -> None:
        move: list[str] = []
        for _ in range(amount):
            move.append(self.loadout[from_stack - 1].pop())
        move.reverse()
        self.loadout[to_stack - 1].extend(move)

    def get_top_configuration(self) -> list[str]:
        return [lo.pop() for lo in self.loadout]


def parse_initial_loadout(input_lines: list[str]) -> list[deque]:
    loadout: list[deque[str]] = []

    setup_line = input_lines.pop()
    storage_index = setup_line.split()
    for _ in range(int(storage_index[-1])):
        loadout.append(deque())

    input_lines = input_lines[::-1]

    for line in input_lines:
        stacks = list(line)[1::4]
        for index, stack in enumerate(stacks):
            if stack != " ":
                loadout[index].append(stack)

    return loadout


def parse_change_operations(change_operation: str) -> tuple[int, int, int]:
    operations = change_operation.split(" ")
    amount = int(operations[1])
    from_stack = int(operations[3])
    to_stack = int(operations[5])

    return amount, from_stack, to_stack


def parse_input_file(file_path: str) -> tuple[list[str], list[str]]:
    initial_loadout = []
    move_operations = []
    with open(file_path) as f:
        initial_loadout_done = False
        for line in f.readlines():
            if line == "\n":
                initial_loadout_done = True
                continue

            if initial_loadout_done:
                move_operations.append(line.rstrip("\n"))
            else:
                initial_loadout.append(line.rstrip("\n"))

    return initial_loadout, move_operations


def get_last_top_configuration(file_path: str):
    initial_loadout, move_operations = parse_input_file(file_path)
    storage = Storage(parse_initial_loadout(initial_loadout))

    for op in move_operations:
        storage.handle_change_operation(*parse_change_operations(op))

    return storage.get_top_configuration()


def get_last_top_configuration_with_multichange(file_path: str):
    initial_loadout, move_operations = parse_input_file(file_path)
    storage = Storage(parse_initial_loadout(initial_loadout))

    for op in move_operations:
        storage.handle_multi_move_operations(*parse_change_operations(op))

    return storage.get_top_configuration()


if __name__ == "__main__":
    FILE_PATH = "dec_5/input.txt"

    top_config = get_last_top_configuration(FILE_PATH)

    print(f"Final Config: {''.join(top_config)}")

    top_config = get_last_top_configuration_with_multichange(FILE_PATH)

    print(f"Final Multi Move Config: {''.join(top_config)}")
