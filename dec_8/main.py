from dataclasses import dataclass
from typing import Optional


@dataclass
class Tree:
    height: int
    visible_horizontal: bool = False
    visible_vertical: bool = False


def parse_file(file_name: str) -> list[list[Tree]]:
    tree_lines = []
    with open(file_name) as f:
        for line in f.readlines():
            tree_lines.append([Tree(int(h)) for h in list(line.rstrip("\n"))])

    return tree_lines


def mark_edge(tree_lines: list[list[Tree]]) -> list[list[Tree]]:

    tree_lines[0] = [Tree(tree.height, True, True) for tree in tree_lines[0]]
    tree_lines[-1] = [Tree(tree.height, True, True) for tree in tree_lines[-1]]

    for line in tree_lines:
        line[0].visible_horizontal = True
        line[0].visible_vertical = True
        line[-1].visible_horizontal = True
        line[-1].visible_vertical = True

    return tree_lines


def mark_horizontal(
    tree_lines: list[list[Tree]], reverse: bool = False
) -> list[list[Tree]]:
    for line in tree_lines:
        if reverse:
            for index, tree in reversed(list(enumerate(line))):
                if tree.visible_horizontal:
                    continue
                last_height = get_last_visible_tree_height(
                    line, index, reverse, "horizontal"
                )
                if last_height is not None and last_height < tree.height:
                    tree.visible_horizontal = True
        else:
            for index, tree in enumerate(line):
                if tree.visible_horizontal:
                    continue
                last_height = get_last_visible_tree_height(
                    line, index, reverse, "horizontal"
                )
                if last_height is not None and last_height < tree.height:
                    tree.visible_horizontal = True

    return tree_lines


def mark_vertical(
    tree_lines: list[list[Tree]], reverse: bool = False
) -> list[list[Tree]]:
    for i in range(len(tree_lines[0])):
        if reverse:
            for index, line in reversed(list(enumerate(tree_lines))):
                if line[i].visible_vertical:
                    continue
                last_height = get_last_visible_tree_height(
                    [li[i] for li in tree_lines], index, reverse, "vertical"
                )
                if last_height is not None and last_height < line[i].height:
                    line[i].visible_vertical = True
        else:
            for index, line in enumerate(tree_lines):
                if line[i].visible_vertical:
                    continue
                last_height = get_last_visible_tree_height(
                    [li[i] for li in tree_lines], index, reverse, "vertical"
                )
                if last_height is not None and last_height < line[i].height:
                    line[i].visible_vertical = True

    return tree_lines


def get_last_visible_tree_height(
    line: list[Tree], index: int, reverse: bool, direction: str
) -> Optional[int]:
    if direction == "horizontal":
        if reverse:
            visible_trees = [t for t in line[index:] if t.visible_horizontal]
        else:
            visible_trees = [t for t in reversed(line[:index]) if t.visible_horizontal]
    else:
        if reverse:
            visible_trees = [t for t in line[index:] if t.visible_vertical]
        else:
            visible_trees = [t for t in reversed(line[:index]) if t.visible_vertical]
    if visible_trees:
        return visible_trees[0].height
    else:
        return None


def count_visible_trees(tree_lines: list[list[Tree]]) -> int:
    count = 0

    for tree_line in tree_lines:
        for tree in tree_line:
            if tree.visible_vertical or tree.visible_horizontal:
                count += 1

    return count


if __name__ == "__main__":
    FILE_PATH = "dec_8/input.txt"
    tree_lines = parse_file(FILE_PATH)

    tree_lines = mark_edge(tree_lines)
    tree_lines = mark_horizontal(tree_lines, False)
    tree_lines = mark_horizontal(tree_lines, True)
    tree_lines = mark_vertical(tree_lines, False)
    tree_lines = mark_vertical(tree_lines, True)

    visible_trees = count_visible_trees(tree_lines)

    print(f"visible tree count: {visible_trees}")
