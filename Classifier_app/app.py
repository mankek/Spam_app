#!/usr/bin/python
from flask import Flask, render_template, request, redirect, url_for
import numpy
import pickle
import os
import sqlite3
from update import update_model

app = Flask(__name__)

cur_dir = os.path.dirname(__file__)
clf = pickle.load(open(os.path.join(cur_dir, 'pkl_objects', 'classifier.pkl'), 'rb'))
scaler = pickle.load(open(os.path.join(cur_dir, 'pkl_objects', 'scaler.pkl'), 'rb'))
db_path = r"spam.sqlite"


def find_words(input_text):
    freqs = []
    important_words = ["make", "address", "all", "3d", "our", "over", "remove", "internet", "order", "mail", "receive",
                       "will", "people", "report", "addresses", "free", "business", "email", "you", "credit", "your",
                       "font", "000", "money", "hp", "hpl", "george", "650", "lab", "labs", "telnet", "857", "data",
                       "415", "85", "technology", "1999", "parts", "pm", "direct", "cs", "meeting", "original",
                       "project", "re", "edu", "table", "conference"]
    non_alphanum = ["#", "@", "-", ".", "$", "*", "(", ")", "+", ";", "~", ":", "'", "/", "%", "_", "?", ",", "=", "&",
                    "!"]

    for s in non_alphanum:
        input_text = input_text.split(s)
        input_text = " ".join(input_text)
    input_text = input_text.lower().split(" ")
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
    if not capital_lengths:
        capitals.extend([0, 0, 0])
    else:
        capitals.append(round(sum(capital_lengths)/len(capital_lengths), 2))
        capitals.append(max(capital_lengths))
        capitals.append(len(capital_lengths))
    return capitals


def classify(params_in):
    params_in = scaler.transform([params_in])
    classes = {1: "spam", 0: "not spam"}
    y = clf.predict(params_in)[0]
    proba = numpy.max(clf.predict_proba(params_in))
    return classes[y], str(round(proba * 100, 2))


def train(parameters, y):
    parameters = [parameters]
    parameters = scaler.transform(parameters)
    clf.partial_fit(parameters, [y])


def sqlite_entry(parameters, y):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''INSERT INTO spam_db
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
              (parameters[0], parameters[1], parameters[2], parameters[3], parameters[4], parameters[5],
               parameters[6], parameters[7], parameters[8], parameters[9], parameters[10], parameters[11],
               parameters[12], parameters[13], parameters[14], parameters[15], parameters[16], parameters[17],
               parameters[18], parameters[19], parameters[20], parameters[21], parameters[22], parameters[23],
               parameters[24], parameters[25], parameters[26], parameters[27], parameters[28], parameters[29],
               parameters[30], parameters[31], parameters[32], parameters[33], parameters[34], parameters[35],
               parameters[36], parameters[37], parameters[38], parameters[39], parameters[40], parameters[41],
               parameters[42], parameters[43], parameters[44], parameters[45], parameters[46], parameters[47],
               parameters[48], parameters[49], parameters[50], parameters[51], parameters[52], parameters[53],
               parameters[54], parameters[55], parameters[56], y))
    conn.commit()
    conn.close()


@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html", label=None, prob=None)


@app.route("/analyze", methods=["POST"])
def analyze():
    global params
    params = []
    input_text = request.form["text"]
    if input_text == "":
        return redirect(url_for("index"))
    params.extend(find_words(input_text))
    params.extend(find_chars(input_text))
    params.extend(find_capitals(input_text))
    label, probability = classify(params)
    return render_template("index.html", label=label, prob=probability)


@app.route("/storage", methods=["POST"])
def store():
    in_label = request.form["label_in"]
    labels = {"spam": 1, "not spam": 0}
    train(params, labels[in_label])
    sqlite_entry(params, labels[in_label])
    return redirect(url_for("index"))


if __name__ == '__main__':
    clf = update_model(db_path, clf)
    app.run(debug=True)
