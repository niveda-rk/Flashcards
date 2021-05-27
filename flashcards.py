from flask import Flask, render_template, abort, jsonify, request, redirect, url_for

from model import *

app = Flask(__name__)


# view function
@app.route("/")
def welcome():
    db = load_db()
    return render_template(
        "welcome.html",
        cards=db  # jinja variable
    )


# if u leave out the int, then the value that comes as a parameter will be of type string by default
@app.route("/card/<int:index>")  # parameters in urls
def card_view(index):
    db = load_db()
    try:
        card = db[index]
        return render_template("card.html", card=card, index=index, max_index=len(db) - 1)
    except IndexError:
        abort(404)


@app.route("/add_card", methods=["GET", "POST"])
def add_card():
    if request.method == "GET":
        return render_template("add_card.html")

    # this is when the method is POST. Over here the dat from the form is gonna be processed
    insert_into_db(request.form['question'], request.form['answer'])
    db = load_db()
    return redirect(url_for('card_view', index=len(db)-1))


@app.route("/delete_card/<int:index>", methods=["GET", "POST"])
def delete_card(index):
    try:
        if request.method == "GET":
            db = load_db()
            return render_template("delete_card.html", card=db[index])
        delete_row_db(index)
        return redirect(url_for('welcome'))
    except IndexError:
        abort(404)


# rest api is where data in the for of json is returned instead of html files
@app.route("/api/card")
def api_cards():
    db = load_db()
    return jsonify(db)
    # for some security reasons, it doesnt allow us to return a list of objects. But can return it once jsonified.


@app.route("/api/card/<int:index>")
def api_card(index):
    try:
        db = load_db()
        return db[index]
    except IndexError:
        abort(404)
