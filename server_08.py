import os
from datetime import datetime as dt
from random import random, randrange
from bottle import route, run, static_file, view
from horoscope import generate_prophecies

cwd = os.getcwd() + os.sep + 'views' + os.sep + 'home.tpl'
@route("/")
@view(cwd)
def index():
  now = dt.now()

  x = random()

  special_date = x > 0.5

  return {
    "date": f"{now.year}-{now.month}-{now.day}",
    #"predictions": generate_prophecies(6, 2),#[
    #   "После обеда ожидайте неожиданного праздника.",
    #   "Днем остерегайтесь неожиданного праздника.",
    #   "Утром ожидайте гостей из забытого прошлого.",
    # ],
    "special_date": x > 0.5,
    "x": x,
  }

@route('/css/<filename>')
def send_css(filename):
    return static_file(filename, root='static/css')

@route("/api/test")
def api_test():
    return {"test_passed": True}

# @route("/api/forecasts")
# def api_forecasts():
# 	now = dt.now()
# 	x = random()
# 	special_date = x > 0.5
# 	return {
# 	"date": f"{now.year}-{now.month}-{now.day}",
# 	"prophecies": generate_prophecies(6, 2),
# 	"special_date": special_date,
# 	"x": x,
# 	}

run(
  host="localhost",
  port=8080,
  autoreload=True
)