from flask import Flask, render_template
import random
import os

app = Flask(__name__)

color = os.environ['BGCOLOR']

# list of  images
images = [
   "https://i.picsum.photos/id/1025/4951/3301.jpg?hmac=_aGh5AtoOChip_iaMo8ZvvytfEojcgqbCH7dzaz-H8Y",
    "https://i.picsum.photos/id/1062/5092/3395.jpg?hmac=o9m7qeU51uOLfXvepXcTrk2ZPiSBJEkiiOp-Qvxja-k",
    "https://i.picsum.photos/id/1084/4579/3271.jpg?hmac=YblMazviSugJVfZsFPaFI_Vp6lBeQin62qpm8rxHruo",
    "https://i.picsum.photos/id/200/1920/1280.jpg?hmac=-eKjMC8-UrbLMpy1A4OWrK0feVPB3Ka5KNOGibQzpRU"
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url, color=color)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
