# app.py - v1.2z

from config import CONFIG
from core.brain import SpriteBrain
from ui.layout import SpriteApp

from transformers import AutoTokenizer, AutoModel

""" def load_model():
    print("Loading DistilBERT model from:", CONFIG["model_path"])
    tokenizer = AutoTokenizer.from_pretrained(CONFIG["model_path"])
    model = AutoModel.from_pretrained(CONFIG["model_path"])
    return tokenizer, model """

if __name__ == "__main__":
    brain = SpriteBrain()
    #tokenizer, model = load_model()
    SpriteApp(brain=brain).run()






