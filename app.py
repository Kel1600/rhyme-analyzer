from flask import Flask, render_template, request
from rhyme_analyzer import rhyme_pattern, count_line_syllables

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        lyrics = request.form["lyrics"]
        lyrics = lyrics.lower().split("\n")
        lyrics = [lyric.strip() for lyric in lyrics if lyric.strip() != ""]
        print(lyrics)

        pattern = rhyme_pattern(lyrics)
        syllables = [count_line_syllables(line) for line in lyrics]

    return render_template("index.html", pattern=pattern, syllables=syllables, lines=lyrics)

if __name__ == "__main__":
    app.run(debug=True)