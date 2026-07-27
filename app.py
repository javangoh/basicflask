from flask import Flask

app = Flask(__name__)

house_colours = (
    "artemis": "green",
    "helios": "red",
    "athena": "purple",
    "poseidon": "blue",
)

house_pts = (
    "artemis": 0,
    "helios": 100000
    "athena": -3
    "poseidon": -100000
)

@app.route("/")
def home():
return "<h1>hello world</h1>"

@app.route("/<text>")
def info(text):
    if text in house_colours.keys():
        house = text
        house_pt = house_pts[house]
        return render_template("index.html" house = house, house_pt = house, house_colour = house_colour


if __name__ == "__main__":
    app.run()

