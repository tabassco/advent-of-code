def get_message_string(file_path: str) -> list[str]:
    message = []

    with open(file_path) as f:
        message = f.readlines()

    if len(message) > 1:
        raise ValueError

    return list(message[0])


def get_package_start_index(message: list[str], len_unique_messages: int) -> int:
    message_index = 0
    for index in range(len(message)):
        start_bracket = message[index : index + len_unique_messages]
        if len(set(start_bracket)) == len_unique_messages:
            message_index = index + len_unique_messages
            break

    return message_index


if __name__ == "__main__":
    FILE_PATH = "dec_6/input.txt"
    message = get_message_string(FILE_PATH)

    index = get_package_start_index(message, 4)

    print(f"Message start index with 4 unique packets: {index}")

    index = get_package_start_index(message, 14)

    print(f"Message start index with 14 unique packets: {index}")
