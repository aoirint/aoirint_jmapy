# aoirint_jmapy

Unofficial JMA weather forecast API wrapper in Python

気象庁天気予報データの非公式Pythonラッパー

2022-05-27時点のAPIに対応

- 気象庁の天気予報ページ: <https://www.jma.go.jp/bosai/forecast/>

## Install
```shell
pip3 install aoirint_jmapy
```

## Usage
### 東京都 東京地方のデータを見る例

```python
from aoirint_jmapy import JmaApi

# UserAgentに含めるため、あなたのアプリケーション名、バージョンを設定することを推奨
# UserAgentは次のようになります: MyWeatherApp 0.1.0 / aoirint_jmapy 20220527.4
# アプリケーションを一般に配布する場合、不具合等により不特定多数の端末から
# 気象庁のサーバに負荷をかけることがないように、自分でキャッシュサーバを立てること等を推奨
jmaApi = JmaApi(
  app_name='MyWeatherApp',
  app_version='0.1.0',
)

# 東京都
forecast = jmaApi.forecast(area_id='130000')
print(forecast)

## 東京地方
print(forecast[0])

### 3日間予報
print(forecast[0].timeSeries[0])

### 週間予報
print(forecast[0].timeSeries[1])

### 3日間天気概況
overview_forecast = jmaApi.overview_forecast(area_id='130000')
print(overview_forecast.text)

### 週間天気概況
overview_week = jmaApi.overview_week(area_id='130000')
print(overview_week.text)
```

### area_idを調べる

- ※ 単一の地点のみでいい場合、気象庁の天気予報ページから手動で選択して実際のリクエストURLから抽出する方が簡単

```python
# エリアリスト
area = jmaApi.area()

## センターリスト（気象台リスト）
print(area.centers)

### 北海道地方: center_id=010100
#### 宗谷地方: area_id=011000
#### 上川・留萌地方: area_id=012000
print(area.centers['010100'])

### 関東甲信地方: center_id=010300
#### 東京都: area_id=130000
#### 神奈川県: area_id=140000
print(area.centers['010300'])
```

## Development

## Environment

```shell
python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt
```

## Lock dependencies

```shell
pip3 install pip-tools

pip-compile requirements.in
pip-compile requirements.test.in
```

## Test

```shell
# Download some JMA API response for test
./get_testdata.sh

pip3 install -r requirements.test.txt

mypy aoirint_jmapy/

pytest tests/
```

### Release

GitHub Releaseを作成するとGitHub Actionsにより自動でPyPIにリリースされる。
