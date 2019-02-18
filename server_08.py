from bottle import route, run, view
from datetime import datetime as dt
from random import random
from horoscope import generate_prophecies
import os

cwd = os.getcwd() + os.sep + 'views' + os.sep + 'static_predictions.tpl'
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
  port=8000,
  autoreload=True
)