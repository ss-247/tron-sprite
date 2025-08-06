# ui/layout.py - v1.4 clean TRON layout
from pathlib import Path
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Static, Input
from core.brain import SpriteBrain

class BrainDisplay(Static):
    """Widget to show brain state info."""
    def update_state(self, state):
        display = "\n".join(f"[b]{key}:[/b] {value}" for key, value in state.items())
        self.update(display)

class SpriteApp(App):
    CSS_PATH = "styles.css"
    BINDINGS = [("q", "quit", "Quit")]

    def __init__(self, brain: SpriteBrain):
        super().__init__()
        self.brain = brain

    def compose(self) -> ComposeResult:
        yield Static("💠 Sprite Interface - TRON Mode", id="header")

        with Horizontal():
            # LEFT panel: Output + Input (stacked)
            with Vertical(id="output_container"):
                self.sprite_output = Static("Sprite awaits your input...", id="output")
                self.chat_input = Input(placeholder="Type to talk to Sprite...", id="chat")
                yield self.sprite_output
                yield self.chat_input

            # RIGHT panel: Brain status
            self.brain_panel = BrainDisplay(id="brain")
            yield self.brain_panel

    def on_mount(self):
        self.set_interval(5, self.refresh_brain)

    def refresh_brain(self):
        self.brain.update()
        self.brain_panel.update_state(self.brain.get_state())

    def on_input_submitted(self, message: Input.Submitted):
        query = message.value
        response = f"Sprite received: {query}"  # Replace with actual model later
        self.sprite_output.update(response)
        message.input.value = ""
