# aoirint_jmapy

Unofficial JMA weather forecast API wrapper in Python

```shell
pip3 install aoirint_jmapy
```

```python
from aoirint_jmapy import JmaApi

# 東京地方
forecast = JmaApi().forecast(area_id='130000')
print(forecast)
```

## Development

```shell
python3 -m venv venv
pip3 install -r requirements.test.txt

mypy aoirint_jmapy/

pytest tests/
```
