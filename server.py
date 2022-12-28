from flask import Flask, Response, redirect, render_template, request, url_for

from machinetranslation.translator import english_to_french, french_to_english

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/englishToFrench", methods=["POST"])
def translate_to_french():
    text = request.form["text"]
    result = english_to_french(text)
    return render_template("index.html", en_translated=result, en_src=text)


@app.route("/frenchToEnglish", methods=["POST"])
def translate_to_english():
    text = request.form["text"]
    result = french_to_english(text)
    return render_template("index.html", fr_translated=result, fr_src=text)


if __name__ == "__main__":
    app.run()
