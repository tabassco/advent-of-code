FILE_PATH = "1/input.txt"


def parse_calories_file(file_path: str):
    carried_calories = []
    with open(file_path) as f:
        lines = f.readlines()
        max_current_calories = 0
        for line in lines:
            if line == "\n":
                carried_calories.append(max_current_calories)
                max_current_calories = 0

            else:
                max_current_calories += int(line.strip("\n"))
    return carried_calories


def get_max_calories(file_path: str):
    carried = parse_calories_file(file_path)
    return sorted(carried, reverse=True)[0]


def get_top_three_sum(file_path: str):
    carried = parse_calories_file(file_path)
    top_three = sorted(carried, reverse=True)[:3]

    return sum(top_three)


if __name__ == "__main__":
    max_calories = get_max_calories(FILE_PATH)

    print(f"Maximum Calories: {max_calories}")

    top_three_sum = get_top_three_sum(FILE_PATH)

    print(f"Top three sum: {top_three_sum}")
