#!/usr/bin/python
from flask import Flask, render_template, request
import numpy

app = Flask(__name__)


@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html", result=None)


@app.route("/analyze", methods=["POST"])
def analyze():
    input_text = request.form["text"]
    return render_template("index.html", result="No results yet!")


def find_words(input_text):
    freqs = []
    important_words = ["make", "address", "all", "3d", "our", "over", "remove", "internet", "order", "mail", "receive",
                       "will", "people", "report", "addresses", "free", "business", "email", "you", "credit", "your",
                       "font", "000", "money", "hp", "hpl", "george", "650", "lab", "labs", "telnet", "857", "data",
                       "415", "85", "technology", "1999", "parts", "pm", "direct", "cs", "meeting", "original",
                       "project", "re", "edu", "table", "conference"]
    non_alphanum = ["#", "@", "-", ".", "$", "*", "(", ")", "+", ";", "~", ":", "'", "/", "%", "_", "?", ",", "=", "&", "!"]

    for s in non_alphanum:
        input_text = input_text.split(s)
        input_text = " ".join(input_text)
    input_text = input_text.split(" ")
    for t in important_words:
        word_count = input_text.count(t)
        freqs.append(round((word_count/len(input_text))*100, 2))
    return freqs


def find_chars(input_text):
    freqs = []
    important_chars = [";", "(", "[", "!", "$", "#"]
    for i in important_chars:
        char_count = input_text.count(i)
        freqs.append(round((char_count/len(input_text))*100, 2))
    return freqs


def capital_run(input_text):
    capital_lengths = []
    length = 0
    for i in input_text:
        if not i.islower():
            length += 1
        else:
            capital_lengths.append(length)
            length = 0
    return numpy.mean(capital_lengths)

def find_capitals(input_text):
    capitals = []
    capital_lengths = []
    length = 0
    for i in input_text:
        if not i.islower():
            length += 1
        elif i.islower():
            if length != 0:
                capital_lengths.append(length)
            length = 0
    if length != 0:
        capital_lengths.append(length)
    capitals.append(round(sum(capital_lengths)/len(capital_lengths), 2))
    capitals.append(max(capital_lengths))
    capitals.append(len(capital_lengths))
    return capitals


if __name__ == '__main__':
    app.run(debug=True)
