from flask import Flask, render_template, request
from rhyme_analyzer import rhyme_pattern, count_line_syllables
from livereload import Server

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    pattern = None
    syllables = None
    lyrics = None

    if request.method == "POST":
        lyrics = request.form["lyrics"]
        lyrics = lyrics.lower().split("\n")
        lyrics = [lyric.strip() for lyric in lyrics if lyric.strip() != ""]
        print(lyrics)

        pattern = rhyme_pattern(lyrics)
        syllables = [count_line_syllables(line) for line in lyrics]

    return render_template("index.html", pattern=pattern, syllables=syllables, lines=lyrics)

if __name__ == "__main__":
    # app.run(debug=True)
    app.debug = True
    server = Server(app.wsgi_app)
    server.watch("templates/*.html")
    server.watch("static/*.css")
    server.serve(port=5000)