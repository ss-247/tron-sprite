# config.py - v1

from pathlib import Path

CONFIG = {
    "model_path": Path("models/distilbert-base-uncased"),
    "refresh_interval": 5,  # seconds between sensor updates
    "memory_file": Path("memory/state.json"),
    "theme": "tron",
}
