#!/bin/bash

mkdir -p testdata

wget https://www.jma.go.jp/bosai/common/const/area.json -O testdata/area.json
wget https://www.jma.go.jp/bosai/forecast/const/forecast_area.json -O testdata/forecast_area.json
wget https://www.jma.go.jp/bosai/forecast/const/en_amedas.json -O testdata/en_amedas.json

wget https://www.jma.go.jp/bosai/forecast/const/anniversary.json -O testdata/anniversary.json

wget https://www.jma.go.jp/bosai/forecast/const/week_area.json -O testdata/week_area.json

wget https://www.jma.go.jp/bosai/forecast/const/week_area05.json -O testdata/week_area05.json
wget https://www.jma.go.jp/bosai/forecast/const/week_area_name.json -O testdata/week_area_name.json

wget https://www.jma.go.jp/bosai/forecast/data/overview_week/130000.json -O testdata/overview_week.json
wget https://www.jma.go.jp/bosai/forecast/data/overview_forecast/130000.json -O testdata/overview_forecast.json

wget https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json -O testdata/forecast.json
wget https://www.jma.go.jp/bosai/warning/data/warning/130000.json -O testdata/warning.json
