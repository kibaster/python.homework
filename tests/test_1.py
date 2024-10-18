import pytest
from Solutions.task_1 import pull


@pytest.mark.parametrize(
    "input_n,expected",
    [
        (0, (0, 0)),
        (10, (1, 0)),
        (20, (2, 0)),
        (29, (2, 0)),
        (30, (3, 0)),
        (31, (3, 0)),
        (39, (3, 0)),
        (80, (8, 0)),
        (89, (8, 0)),
        (90, (8, 1)),
        (91, (9, 1)),
        (100, (9, 1)),
        (101, (10, 1)),
        (180, (17, 2)),
        (181, (18, 2)),
        (1080, (107, 12)),
        (1081, (108, 12)),
        (2150, (214, 23)),
        (2151, (215, 23)),
        (2152, (215, 23)),
        (2158, (215, 23)),
        (2160, (215, 24)),
        (2161, (216, 24)),
    ],
)
def test_pull(input_n: Literal[0] | Literal[10] | Literal[20] | Literal[29] | Literal[30] | Literal[31] | Literal[39] | Literal[80] | Literal[89] | Literal[90] | Literal[91] | Literal[100] | Literal[101] | Literal[180] | Literal[181] | Literal[1080] | Literal[1081] | Literal[2150] | Literal[2151] | Literal[2152] | Literal[2158] | Literal[2160] | Literal[2161], expected: tuple[int, int]):
    assert pull(input_n) == expected
