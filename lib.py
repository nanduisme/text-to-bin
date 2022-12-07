from rich.panel import Panel
from textual.reactive import Reactive
from textual.widget import Widget


def dec_to_bin(num: int) -> str:
    byte = [0 for _ in range(8)]
    pos = 1
    while num:
        num, remainder = divmod(num, 2)
        byte[-pos] = remainder
        pos += 1

    return "".join(map(lambda x: str(x), byte))


def dec_to_hex(num: int) -> str:
    byte = ["0" for _ in range(2)]
    chars = list("0123456789abcdef")
    pos = 1
    while num:
        num, r = divmod(num, 16)
        byte[-pos] = chars[r]
        pos += 1

    return "".join(byte)


def bin_to_dec(num: str) -> str:
    return sum(int(digit) * 2**pos for pos, digit in enumerate(num[::-1]))


# Widgets


class BinOutput(Widget):
    text = Reactive("")

    @property
    def bin(self) -> str:
        return " ".join(map(lambda x: dec_to_bin(ord(x)), self.text))

    def render(self):
        return Panel(
            self.bin,
            title="Binary",
            border_style="b green",
            padding=1,
        )


class HexOutput(Widget):
    text = Reactive("")

    @property
    def hex(self) -> str:
        return " ".join(map(lambda x: dec_to_hex(ord(x)), self.text))

    def render(self):
        return Panel(
            self.hex,
            title="Hexadecimal",
            border_style="b magenta",
            padding=1,
        )
