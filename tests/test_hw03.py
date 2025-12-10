import os
import sys
import pytest

# Ensure we can import main.py from the homework folder.
# Put the homework folder first on sys.path so it takes precedence
# and remove any previously-imported top-level `main` to avoid
# importing a different project's `main.py` from a cached module.
project_root = os.path.dirname(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
import os
import sys
import pytest

# Ensure we can import main.py from the homework folder
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import count_power_groups


@pytest.mark.parametrize(
    "stations, lines, expected",
    [
        ([], [], 0),
        (["A"], [], 1),
        (["A", "B"], [("A", "B")], 1),
        (["A", "B"], [], 2),
    ],
)
def test_basic_cases(stations, lines, expected):
    assert count_power_groups(stations, lines) == expected


@pytest.mark.parametrize(
    "stations, lines, expected",
    [
        (
            ["A", "B", "C", "D"],
            [("A", "B"), ("B", "C")],
            2,  # {A,B,C} and {D}
        ),
        (
            ["A", "B", "C", "D", "E"],
            [("A", "B"), ("C", "D")],
            3,  # {A,B}, {C,D}, {E}
        ),
        (
            ["A", "B", "C"],
            [("A", "B"), ("B", "C"), ("A", "C")],
            1,  # fully connected triangle
        ),
        (
            ["A", "B", "C", "D"],
            [("A", "B"), ("B", "C"), ("C", "A"), ("C", "D")],
            1,  # D attached, all connected
        ),
    ],
)
def test_connected_and_disconnected(stations, lines, expected):
    assert count_power_groups(stations, lines) == expected


@pytest.mark.parametrize(
    "stations, lines, expected",
    [
        (
            ["S" + str(i) for i in range(6)],
            [("S0", "S1"), ("S1", "S2"), ("S3", "S4")],
            3,  # {S0,S1,S2}, {S3,S4}, {S5}
        ),
        (
            ["X1", "X2", "X3", "X4", "X5", "X6"],
            [
                ("X1", "X2"),
                ("X2", "X3"),
                ("X4", "X5"),
                ("X5", "X6"),
                ("X1", "X3"),  # extra line
                ("X4", "X6"),  # extra line
            ],
            2,
        ),
        (
            ["A", "B", "C", "D", "E", "F"],
            [("A", "B"), ("B", "C"), ("D", "E"), ("E", "F"), ("D", "F")],
            2,
        ),
    ],
)
def test_larger_graphs(stations, lines, expected):
    assert count_power_groups(stations, lines) == expected
from main import count_power_groups


@pytest.mark.parametrize(
    "stations, lines, expected",
    [
        ([], [], 0),
        (["A"], [], 1),
        (["A", "B"], [("A", "B")], 1),
        (["A", "B"], [], 2),
    ],
)
def test_basic_cases(stations, lines, expected):
    assert count_power_groups(stations, lines) == expected


@pytest.mark.parametrize(
    "stations, lines, expected",
    [
        (
            ["A", "B", "C", "D"],
            [("A", "B"), ("B", "C")],
            2,  # {A,B,C} and {D}
        ),
        (
            ["A", "B", "C", "D", "E"],
            [("A", "B"), ("C", "D")],
            3,  # {A,B}, {C,D}, {E}
        ),
        (
            ["A", "B", "C"],
            [("A", "B"), ("B", "C"), ("A", "C")],
            1,  # fully connected triangle
        ),
        (
            ["A", "B", "C", "D"],
            [("A", "B"), ("B", "C"), ("C", "A"), ("C", "D")],
            1,  # D attached, all connected
        ),
    ],
)
def test_connected_and_disconnected(stations, lines, expected):
    assert count_power_groups(stations, lines) == expected


@pytest.mark.parametrize(
    "stations, lines, expected",
    [
        (
            ["S" + str(i) for i in range(6)],
            [("S0", "S1"), ("S1", "S2"), ("S3", "S4")],
            3,  # {S0,S1,S2}, {S3,S4}, {S5}
        ),
        (
            ["X1", "X2", "X3", "X4", "X5", "X6"],
            [
                ("X1", "X2"),
                ("X2", "X3"),
                ("X4", "X5"),
                ("X5", "X6"),
                ("X1", "X3"),  # extra line
                ("X4", "X6"),  # extra line
            ],
            2,
        ),
        (
            ["A", "B", "C", "D", "E", "F"],
            [("A", "B"), ("B", "C"), ("D", "E"), ("E", "F"), ("D", "F")],
            2,
        ),
    ],
)
def test_larger_graphs(stations, lines, expected):
    assert count_power_groups(stations, lines) == expected
