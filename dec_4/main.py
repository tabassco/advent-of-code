from __future__ import annotations


class SuppliesCategories:
    def __init__(
        self, categories_1: tuple[str, str], categories_2: tuple[str, str]
    ) -> None:
        self.categories_1 = self.get_responsible_categories(
            int(categories_1[0]), int(categories_1[1])
        )
        self.categories_2 = self.get_responsible_categories(
            int(categories_2[0]), int(categories_2[1])
        )

    @classmethod
    def from_line_string(cls, line_string: str) -> SuppliesCategories:
        cat_1, cat_2 = line_string.rstrip("\n").split(",")
        cat_1 = tuple(cat_1.split("-"))
        cat_2 = tuple(cat_2.split("-"))
        return SuppliesCategories(cat_1, cat_2)

    @staticmethod
    def get_responsible_categories(lower: int, upper: int) -> set[int]:
        return set(range(lower, upper + 1))

    @property
    def has_complete_overlap(self) -> bool:
        if len(self.categories_1) > len(self.categories_2):
            return (
                self.categories_1.intersection(self.categories_2) == self.categories_2
            )
        else:
            return (
                self.categories_1.intersection(self.categories_2) == self.categories_1
            )

    @property
    def has_overlap(self) -> bool:
        return len(self.categories_1.intersection(self.categories_2)) > 0


def parse_categories(file_path: str) -> list[SuppliesCategories]:
    supplies = []
    with open(file_path) as f:
        lines = f.readlines()
        for line in lines:
            supplies.append(SuppliesCategories.from_line_string(line))

    return supplies


def get_complete_overlap_count(supplies: list[SuppliesCategories]) -> int:
    overlap_count = 0
    for supply in supplies:
        if supply.has_complete_overlap:
            overlap_count += 1

    return overlap_count


def get_overlap_count(supplies: list[SuppliesCategories]) -> int:
    overlap_count = 0
    for supply in supplies:
        if supply.has_overlap:
            overlap_count += 1

    return overlap_count


if __name__ == "__main__":
    FILE_PATH = "dec_4/input.txt"
    supplies = parse_categories(FILE_PATH)
    overlap_count = get_complete_overlap_count(supplies)

    print(f"complete overlap count: {overlap_count}")

    overlap_count = get_overlap_count(supplies)
    print(f"partial overlap count: {overlap_count}")
