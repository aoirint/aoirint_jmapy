# aoirint_jmapy

Unofficial JMA weather forecast API wrapper in Python

```shell
pip3 install aoirint_jmapy
```

## 東京都 東京地方のデータを見る例

```python
from aoirint_jmapy import JmaApi

# 東京都
forecast = JmaApi().forecast(area_id='130000')
print(forecast)

## 東京地方
print(forecast[0])

### 3日間予報
print(forecast[0].timeSeries[0])

### 週間予報
print(forecast[0].timeSeries[1])

### 3日間天気概況
overview_forecast = JmaApi().overview_forecast(area_id='130000')
print(overview_forecast.text)

### 週間天気概況
overview_week = JmaApi().overview_week(area_id='130000')
print(overview_week.text)
```

## area_idを調べる

```
# エリアリスト
area = JmaApi().area()

## センターリスト（気象台リスト）
print(area.centers)

### 北海道地方: center_id=010100
#### 宗谷地方: area_id=011000
#### 上川・留萌地方: area_id=012000
print(area.centers['010100'])

### 関東甲信地方: centerid=010300
#### 東京都: area_id=130000
#### 神奈川県: area_id=140000
print(area.centers['010300'])
```

## Development

```shell
# Download some JMA API response for test
./get_testdata.sh

python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.test.txt

mypy aoirint_jmapy/

pytest tests/
```
