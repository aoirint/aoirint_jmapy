import sys
import os
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from aoirint_jmapy import JmaApi

def test_area():
  with open('testdata/area.json', 'r', encoding='utf-8') as fp:
    JmaApi().area(data=json.load(fp))

def test_forecast_area():
  with open('testdata/forecast_area.json', 'r', encoding='utf-8') as fp:
    JmaApi().forecast_area(data=json.load(fp))

def test_en_amedas():
  with open('testdata/en_amedas.json', 'r', encoding='utf-8') as fp:
    JmaApi().en_amedas(data=json.load(fp))

def test_anniversary():
  with open('testdata/anniversary.json', 'r', encoding='utf-8') as fp:
    JmaApi().anniversary(data=json.load(fp))

def test_week_area():
  with open('testdata/week_area.json', 'r', encoding='utf-8') as fp:
    JmaApi().week_area(data=json.load(fp))

def test_week_area05():
  with open('testdata/week_area05.json', 'r', encoding='utf-8') as fp:
    JmaApi().week_area05(data=json.load(fp))

def test_week_area_name():
  with open('testdata/week_area_name.json', 'r', encoding='utf-8') as fp:
    JmaApi().week_area_name(data=json.load(fp))

def test_overview_forecast():
  with open('testdata/overview_forecast.json', 'r', encoding='utf-8') as fp:
    JmaApi().overview_forecast(data=json.load(fp))

def test_overview_week():
  with open('testdata/overview_week.json', 'r', encoding='utf-8') as fp:
    JmaApi().overview_week(data=json.load(fp))

def test_forecast():
  with open('testdata/forecast.json', 'r', encoding='utf-8') as fp:
    JmaApi().forecast(data=json.load(fp))

def test_warning():
  with open('testdata/warning.json', 'r', encoding='utf-8') as fp:
    JmaApi().warning(data=json.load(fp))
