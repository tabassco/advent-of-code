from __future__ import annotations
from dataclasses import dataclass
from enum import Enum


class Moves(Enum):
    ROCK = 1
    PAPER = 2
    SICCORS = 3


@dataclass
class Game:
    choice_p1: Moves
    choice_p2: Moves

    def results(self) -> tuple[int, int]:
        points_p1 = self.choice_p1.value
        points_p2 = self.choice_p2.value

        if self.choice_p1 == self.choice_p2:
            return points_p1 + 3, points_p2 + 3

        match self.choice_p1:
            case Moves.ROCK:
                if self.choice_p2 == Moves.PAPER:
                    return points_p1, points_p2 + 6
                else:
                    return points_p1 + 6, points_p2
            case Moves.PAPER:
                if self.choice_p2 == Moves.SICCORS:
                    return points_p1, points_p2 + 6
                else:
                    return points_p1 + 6, points_p2
            case Moves.SICCORS:
                if self.choice_p2 == Moves.ROCK:
                    return points_p1, points_p2 + 6
                else:
                    return points_p1 + 6, points_p2


def get_choice_from_character(choice: str) -> Moves:
    match choice:
        case "A" | "X":
            return Moves.ROCK
        case "B" | "Y":
            return Moves.PAPER
        case "C" | "Z":
            return Moves.SICCORS


def get_choice_from_character_2(choice: str, choice_p1: Moves) -> Moves:
    if choice == "Y":
        return choice_p1
    match (choice, choice_p1):
        case ("X", Moves.ROCK):
            return Moves.SICCORS
        case ("X", Moves.PAPER):
            return Moves.ROCK
        case ("X", Moves.SICCORS):
            return Moves.PAPER

        case ("Z", Moves.ROCK):
            return Moves.PAPER
        case ("Z", Moves.PAPER):
            return Moves.SICCORS
        case ("Z", Moves.SICCORS):
            return Moves.ROCK


def parse_input(file_path: str) -> list[Game]:
    games = []
    with open(file_path) as f:
        lines = f.readlines()
        for line in lines:
            choice_p1, choice_p2 = line.strip("\n").split(" ")

            games.append(
                Game(
                    get_choice_from_character(choice_p1),
                    get_choice_from_character_2(
                        choice_p2, get_choice_from_character(choice_p1)
                    ),
                )
            )

    return games


if __name__ == "__main__":
    games = parse_input("dec_2/input.txt")

    score_1 = 0
    score_2 = 0

    for game in games:
        g_1, g_2 = game.results()

        score_1 += g_1
        score_2 += g_2

    print(f"Scores: {score_1}, {score_2}")
