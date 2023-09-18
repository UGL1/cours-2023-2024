"""
This module does this and that.
"""

_total = [0]


def this(a: int) -> None:
    """
    does this
    :param a: int
    :return: None
    """
    _total[0] += a
    _display()


def that(a: int) -> None:
    """
    does that
    :param a: int
    :return: None
    """
    _total[0] -= a
    _display()


def _display():
    print(f'total value is :', _total[0])
