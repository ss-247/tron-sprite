# core/brain.py - v2
from core.environment import get_environment_snapshot

class SpriteBrain:
    def __init__(self):
        self.state = {}
        self.history = []

    def update(self):
        self.state = get_environment_snapshot()
        self.history.append(self.state)  # log for analysis later

    def respond_to(self, message: str) -> str:
        if "cpu" in message.lower():
            return f"CPU: {self.state.get('cpu', {})}"
        elif "memory" in message.lower():
            return f"Memory: {self.state.get('memory', {})}"
        elif "disk" in message.lower():
            return f"Disk: {self.state.get('disk', {})}"
        elif "network" in message.lower():
            return f"Network: {self.state.get('network', {})}"
        elif "status" in message.lower():
            return "Environment snapshot:\n" + str(self.state)
        else:
            return "🤖 I can only respond to system queries for now (cpu, memory, disk, network, status)."

    def get_state(self):
        return self.state