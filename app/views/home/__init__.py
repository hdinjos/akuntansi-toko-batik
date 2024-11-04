from app import server
from flask import render_template, session

@server.route("/")
def index():
    return render_template("form/index.html", title="Forms")

@server.route("/forms/add")
def add():
    return render_template("form/add.html", title="Forms Add")


@server.route("/forms")
def forms():
  return render_template("form/index.html", title="Forms")