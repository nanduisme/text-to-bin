from textual.app import App
from textual.binding import Binding
from textual.widgets import Footer, Input

from lib import BinOutput, HexOutput
from pyperclip import copy


class TextToBinApp(App):
    CSS_PATH = "./main.css.txt"
    BINDINGS = [
        Binding("escape", "quit", "Quit", key_display="ESC"),
        Binding("ctrl+b", "copyb", "Copy binary to clipboard"),
        Binding("ctrl+x", "copyx", "Copy hexadecimal to clipboard"),
    ]

    def action_quit(self):
        self.exit()

    def action_copyb(self):
        copy(self.bin_out.bin)

    def action_copyx(self):
        copy(self.hex_out.hex)

    @property
    def bin_out(self) -> BinOutput:
        return self.query_one(BinOutput)

    @property
    def hex_out(self) -> HexOutput:
        return self.query_one(HexOutput)

    def on_input_changed(self) -> None:
        self.bin_out.text = self.query_one(Input).value
        self.hex_out.text = self.query_one(Input).value

    def compose(self):
        yield Input(placeholder="Enter text to convert")
        yield BinOutput(classes="output")
        yield HexOutput(classes="output")
        yield Footer()


if __name__ == "__main__":
    TextToBinApp().run()
