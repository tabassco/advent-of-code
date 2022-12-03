from __future__ import annotations
import string


class Rucksack:
    def __init__(self, compartment_1: set[str], compartment_2: set[str]) -> None:
        self.compartment_1 = compartment_1
        self.compartment_2 = compartment_2

    @classmethod
    def from_total_content(cls, total_content: str) -> Rucksack:
        total_content = list(total_content)
        split_point = len(total_content) // 2
        comp_1 = total_content[:split_point]
        comp_2 = total_content[split_point:]
        return Rucksack(set(comp_1), set(comp_2))

    def get_overlap(self):
        return self.compartment_1.intersection(self.compartment_2)

    @property
    def total_content(self):
        return self.compartment_1.union(self.compartment_2)


def parse_file(file_path: str) -> list[Rucksack]:
    rucksacks = []

    with open(file_path) as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip("\n")
            rucksacks.append(Rucksack.from_total_content(line))

    return rucksacks


def parse_triple_rucksacks(file_path: str) -> list[list[Rucksack]]:
    rucksacks = []

    with open(file_path) as f:
        lines = f.readlines()
        tmp_rucksacks = []
        for i, line in enumerate(lines, start=1):
            line = line.rstrip("\n")
            tmp_rucksacks.append(Rucksack.from_total_content(line))
            if i % 3 == 0:
                rucksacks.append(tmp_rucksacks.copy())
                tmp_rucksacks.clear()

    return rucksacks


def get_triple_overlaps(rucksacks: list[list[Rucksack]]) -> int:
    overlap_sum = 0
    for rucksack_set in rucksacks:
        values = rucksack_set[0].total_content

        for r in rucksack_set[1:]:
            values = values.intersection(r.total_content)

        if len(values) != 1:
            raise ValueError

        overlap_sum += get_valuation(values.pop())

    return overlap_sum


def get_valuation(char: str) -> int:
    if char == char.lower():
        start_value = 1
    else:
        start_value = 27
    index = string.ascii_lowercase.index(char.lower())

    return start_value + index


def get_overlap_valuation(rucksacks: list[Rucksack]):
    overlap_sum = 0
    for rucksack in rucksacks:
        overlap = rucksack.get_overlap()
        if len(overlap) != 1:
            raise ValueError
        overlap_sum += get_valuation(overlap.pop())

    return overlap_sum


if __name__ == "__main__":
    FILE_PATH = "dec_3/input.txt"
    rucksacks = parse_file(FILE_PATH)
    overlap_sum = get_overlap_valuation(rucksacks)
    print(f"Total valuation: {overlap_sum}")

    triple_rucksacks = parse_triple_rucksacks(FILE_PATH)
    triple_sum = get_triple_overlaps(triple_rucksacks)
    print(f"Total valuations in triples: {triple_sum}")
