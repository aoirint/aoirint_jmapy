import requests
from typing import List, Dict, Any, Optional, Union, Literal
from pydantic import BaseModel, parse_obj_as

def get_json(url) -> Dict[str, Any]:
  headers = {
    'User-Agent': 'aoirint_jmapy 0.0.0',
  }

  res = requests.get(url, headers=headers)
  res.raise_for_status()

  data = res.json()
  return data

# Area
class AreaDataCenter(BaseModel):
  name: str
  enName: str
  officeName: str
  parent: Optional[str]
  children: List[str]

class AreaDataClass20s(BaseModel):
  name: str
  enName: str
  kana: str
  parent: Optional[str]

class AreaData(BaseModel):
  centers: Dict[str, AreaDataCenter]
  class20s: Dict[str, AreaDataClass20s]

# Forecast Area
class ForecastAreaDataValueItem(BaseModel):
  class10: str
  amedas: List[str]
  class20: str

ForecastAreaData = Dict[str, List[ForecastAreaDataValueItem]]

# EN Amedas
EnAmedasData = Dict[str, Optional[str]]

# Anniversary
AnniversaryData = List[str]

# Weeb Area
class WeekAreaDataItem(BaseModel):
  srf: str
  week: str
  amedas: str

WeekAreaData = Dict[str, List[WeekAreaDataItem]]

# Weeb Area 05
WeekArea05Data = Dict[str, List[str]]

# Weeb Area Name
class WeekAreaNameDataValue(BaseModel):
  jp: str
  en: str

WeekAreaNameData = Dict[str, WeekAreaNameDataValue]

# Overview Forecast
class OverviewForecastData(BaseModel):
  publishingOffice: str
  reportDatetime: str
  targetArea: str
  headlineText: str
  text: str

# Overview Week
class OverviewWeekData(BaseModel):
  publishingOffice: str
  reportDatetime: str
  headTitle: str
  text: str

# Forecast
class ForecastDataTimeSeriesItemArea(BaseModel):
  name: str
  code: str

class ForecastDataShortTimeSeriesItemAreaForecast(BaseModel):
  area: ForecastDataTimeSeriesItemArea
  weatherCodes: List[str]
  weathers: List[str]
  winds: List[str]
  waves: List[str]

class ForecastDataShortTimeSeriesItemAreaPop(BaseModel):
  area: ForecastDataTimeSeriesItemArea
  pops: List[str]

class ForecastDataShortTimeSeriesItemAreaTemp(BaseModel):
  area: ForecastDataTimeSeriesItemArea
  temps: List[str]

class ForecastDataShortTimeSeriesItem(BaseModel):
  timeDefines: List[str]
  areas: List[Union[ForecastDataShortTimeSeriesItemAreaForecast, ForecastDataShortTimeSeriesItemAreaPop, ForecastDataShortTimeSeriesItemAreaTemp]]

class ForecastDataShort(BaseModel):
  publishingOffice: str
  reportDatetime: str
  timeSeries: List[ForecastDataShortTimeSeriesItem]

class ForecastDataWeeklyTimeSeriesItemAreaPop(BaseModel):
  area: ForecastDataTimeSeriesItemArea
  weatherCodes: List[str]
  pops: List[str]
  reliabilities: List[str]

class ForecastDataWeeklyTimeSeriesItemAreaTemp(BaseModel):
  area: ForecastDataTimeSeriesItemArea
  tempsMin: List[str]
  tempsMinUpper: List[str]
  tempsMinLower: List[str]
  tempsMax: List[str]
  tempsMaxUpper: List[str]
  tempsMaxLower: List[str]

class ForecastDataWeeklyTimeSeriesItem(BaseModel):
  timeDefines: List[str]
  areas: List[Union[ForecastDataWeeklyTimeSeriesItemAreaPop, ForecastDataWeeklyTimeSeriesItemAreaTemp]]

class ForecastDataWeeklyTempAverageArea(BaseModel):
  area: ForecastDataTimeSeriesItemArea
  min: str
  max: str

class ForecastDataWeeklyTempAverage(BaseModel):
  areas: List[ForecastDataWeeklyTempAverageArea]

class ForecastDataWeeklyPrecipAverageArea(BaseModel):
  area: ForecastDataTimeSeriesItemArea
  min: str
  max: str

class ForecastDataWeeklyPrecipAverage(BaseModel):
  areas: List[ForecastDataWeeklyPrecipAverageArea]

class ForecastDataWeekly(BaseModel):
  publishingOffice: str
  reportDatetime: str
  timeSeries: List[ForecastDataWeeklyTimeSeriesItem]
  tempAverage: ForecastDataWeeklyTempAverage
  precipAverage: ForecastDataWeeklyPrecipAverage

ForecastData = List[Union[ForecastDataShort, ForecastDataWeekly]]

# Warning
class WarningDataAreaTypeAreaWarning(BaseModel):
  code: str
  status: str

class WarningDataAreaTypeArea(BaseModel):
  code: str
  warnings: List[WarningDataAreaTypeAreaWarning]

class WarningDataAreaType(BaseModel):
  areas: List[WarningDataAreaTypeArea]

# 雷危険度
class WarningDataTimeSeriesItemAreaWarningLevelLightningLocalArea(BaseModel):
  values: List[str]
  additions: List[str]

class WarningDataTimeSeriesItemAreaWarningLevelLightning(BaseModel):
  type: Literal['雷危険度']
  localAreas: List[WarningDataTimeSeriesItemAreaWarningLevelLightningLocalArea]

class WarningDataTimeSeriesItemAreaWarningLevelLightningContinueLevelLocalArea(BaseModel):
  value: str

class WarningDataTimeSeriesItemAreaWarningLevelLightningContinueLevel(BaseModel):
  type: Literal['雷危険度']
  localAreas: List[WarningDataTimeSeriesItemAreaWarningLevelLightningContinueLevelLocalArea]

# 風危険度
class WarningDataTimeSeriesItemAreaWarningLevelWindLocalArea(BaseModel):
  localAreaName: Optional[str]
  values: List[str]

class WarningDataTimeSeriesItemAreaWarningLevelWind(BaseModel):
  type: Literal['風危険度']
  localAreas: List[WarningDataTimeSeriesItemAreaWarningLevelWindLocalArea]

class WarningDataTimeSeriesItemAreaWarningLevelWindContinueLevelLocalArea(BaseModel):
  value: str

class WarningDataTimeSeriesItemAreaWarningLevelWindContinueLevel(BaseModel):
  type: Literal['風危険度']
  localAreas: List[WarningDataTimeSeriesItemAreaWarningLevelWindContinueLevelLocalArea]

# 波危険度
class WarningDataTimeSeriesItemAreaWarningLevelWaveLocalArea(BaseModel):
  localAreaName: Optional[str]
  values: List[str]

class WarningDataTimeSeriesItemAreaWarningLevelWave(BaseModel):
  type: Literal['波危険度']
  localAreas: List[WarningDataTimeSeriesItemAreaWarningLevelWaveLocalArea]

class WarningDataTimeSeriesItemAreaWarningLevelWaveContinueLevelLocalArea(BaseModel):
  value: str

class WarningDataTimeSeriesItemAreaWarningLevelWaveContinueLevel(BaseModel):
  type: Literal['波危険度']
  localAreas: List[WarningDataTimeSeriesItemAreaWarningLevelWaveContinueLevelLocalArea]

# 風向
class WarningDataTimeSeriesItemAreaWarningWindPropertyWindDirectionLocalAreaWindDirection(BaseModel):
  condition: Optional[str]
  value: Optional[str]

class WarningDataTimeSeriesItemAreaWarningWindPropertyWindDirectionLocalArea(BaseModel):
  localAreaName: Optional[str]
  windDirections: List[WarningDataTimeSeriesItemAreaWarningWindPropertyWindDirectionLocalAreaWindDirection]

class WarningDataTimeSeriesItemAreaWarningWindPropertyWindDirection(BaseModel):
  type: Literal['風向']
  localAreas: List[WarningDataTimeSeriesItemAreaWarningWindPropertyWindDirectionLocalArea]

# 最大風速
class WarningDataTimeSeriesItemAreaWarningWindPropertyMaxWindSpeedLocalArea(BaseModel):
  localAreaName: Optional[str]
  values: List[str]

class WarningDataTimeSeriesItemAreaWarningWindPropertyMaxWindSpeed(BaseModel):
  type: Literal['最大風速']
  localAreas: List[WarningDataTimeSeriesItemAreaWarningWindPropertyMaxWindSpeedLocalArea]

# 波危険度
class WarningDataTimeSeriesItemAreaWarningWindPropertyWaveLocalArea(BaseModel):
  localAreaName: Optional[str]
  values: List[str]

class WarningDataTimeSeriesItemAreaWarningWindPropertyWave(BaseModel):
  type: Literal['波危険度']
  localAreas: List[WarningDataTimeSeriesItemAreaWarningWindPropertyWaveLocalArea]

# 波高
class WarningDataTimeSeriesItemAreaWarningWindPropertyWaveHeightLocalArea(BaseModel):
  localAreaName: Optional[str]
  values: List[str]

class WarningDataTimeSeriesItemAreaWarningWindPropertyWaveHeight(BaseModel):
  type: Literal['波高']
  localAreas: List[WarningDataTimeSeriesItemAreaWarningWindPropertyWaveHeightLocalArea]

# class WarningDataTimeSeriesItemAreaWarning(BaseModel):
#   code: str
#   levels: List[Union[WarningDataTimeSeriesItemAreaWarningLevelLightning, WarningDataTimeSeriesItemAreaWarningLevelWind, WarningDataTimeSeriesItemAreaWarningLevelWave]]
#   continueLevels: Optional[List[Union[WarningDataTimeSeriesItemAreaWarningLevelLightningContinueLevel, WarningDataTimeSeriesItemAreaWarningLevelWindContinueLevel, WarningDataTimeSeriesItemAreaWarningLevelWaveContinueLevel]]]
#   properties: Optional[List[Union[WarningDataTimeSeriesItemAreaWarningWindPropertyWindDirection, WarningDataTimeSeriesItemAreaWarningWindPropertyMaxWindSpeed, WarningDataTimeSeriesItemAreaWarningWindPropertyWave, WarningDataTimeSeriesItemAreaWarningWindPropertyWaveHeight]]]

class WarningDataTimeSeriesItemAreaWarningLightning(BaseModel):
  code: str
  levels: List[WarningDataTimeSeriesItemAreaWarningLevelLightning]
  continueLevels: Optional[List[WarningDataTimeSeriesItemAreaWarningLevelLightningContinueLevel]]

class WarningDataTimeSeriesItemAreaWarningWind(BaseModel):
  code: str
  levels: List[WarningDataTimeSeriesItemAreaWarningLevelWind]
  continueLevels: Optional[List[WarningDataTimeSeriesItemAreaWarningLevelWindContinueLevel]]
  properties: Optional[List[Union[WarningDataTimeSeriesItemAreaWarningWindPropertyWindDirection, WarningDataTimeSeriesItemAreaWarningWindPropertyMaxWindSpeed]]]

class WarningDataTimeSeriesItemAreaWarningWave(BaseModel):
  code: str
  levels: List[WarningDataTimeSeriesItemAreaWarningLevelWave]
  properties: Optional[List[Union[WarningDataTimeSeriesItemAreaWarningWindPropertyWaveHeight]]]

WarningDataTimeSeriesItemAreaWarning = Union[WarningDataTimeSeriesItemAreaWarningWind, WarningDataTimeSeriesItemAreaWarningLightning, WarningDataTimeSeriesItemAreaWarningWave]

class WarningDataTimeSeriesItemAreaTypeArea(BaseModel):
  code: str
  warnings: List[WarningDataTimeSeriesItemAreaWarning]

class WarningDataTimeSeriesItemAreaType(BaseModel):
  areas: List[WarningDataTimeSeriesItemAreaTypeArea]

class WarningDataTimeSeriesItem(BaseModel):
  timeDefines: List[str]
  areaTypes: List[WarningDataTimeSeriesItemAreaType]

class WarningData(BaseModel):
  publishingOffice: str
  reportDatetime: str
  headlineText: str
  notice: str
  areaTypes: List[WarningDataAreaType]
  timeSeries: List[WarningDataTimeSeriesItem]

class JmaApi:
  def area(self,
    url='https://www.jma.go.jp/bosai/common/const/area.json',
    data=None,
  ) -> AreaData:
    if data is None:
      data = get_json(url)
    area = parse_obj_as(AreaData, data)
    return area

  def forecast_area(self,
    url='https://www.jma.go.jp/bosai/forecast/const/forecast_area.json',
    data=None,
  ) -> ForecastAreaData:
    if data is None:
      data = get_json(url)
    forecast_area_data = parse_obj_as(ForecastAreaData, data)
    return forecast_area_data

  def en_amedas(self,
    url='https://www.jma.go.jp/bosai/forecast/const/en_amedas.json',
    data=None,
  ) -> EnAmedasData:
    if data is None:
      data = get_json(url)
    en_amedas_data = parse_obj_as(EnAmedasData, data)
    return en_amedas_data

  def anniversary(self,
    url='https://www.jma.go.jp/bosai/forecast/const/anniversary.json',
    data=None,
  ) -> AnniversaryData:
    if data is None:
      data = get_json(url)
    anniversary_data = parse_obj_as(AnniversaryData, data)
    return anniversary_data

  def week_area(self,
    url='https://www.jma.go.jp/bosai/forecast/const/week_area.json',
    data=None,
  ) -> WeekAreaData:
    if data is None:
      data = get_json(url)
    week_area_data = parse_obj_as(WeekAreaData, data)
    return week_area_data

  def week_area05(self,
    url='https://www.jma.go.jp/bosai/forecast/const/week_area05.json',
    data=None,
  ) -> WeekArea05Data:
    if data is None:
      data = get_json(url)
    week_area05_data = parse_obj_as(WeekArea05Data, data)
    return week_area05_data

  def week_area_name(self,
    url='https://www.jma.go.jp/bosai/forecast/const/week_area_name.json',
    data=None,
  ) -> WeekAreaNameData:
    if data is None:
      data = get_json(url)
    week_area_name_data = parse_obj_as(WeekAreaNameData, data)
    return week_area_name_data

  def overview_forecast(self,
    area_id: str=None,
    base_url='https://www.jma.go.jp/bosai/forecast/data/overview_forecast/{area_id}.json',
    data=None,
  ) -> OverviewForecastData:
    if data is None:
      assert area_id is not None
      url = base_url.format(**{
        'area_id': area_id,
      })
      data = get_json(url)
    overview_forecast_data = parse_obj_as(OverviewForecastData, data)
    return overview_forecast_data

  def overview_week(self,
    area_id: str=None,
    base_url='https://www.jma.go.jp/bosai/forecast/data/overview_week/{area_id}.json',
    data=None,
  ) -> OverviewWeekData:
    if data is None:
      assert area_id is not None
      url = base_url.format(**{
        'area_id': area_id,
      })
      data = get_json(url)
    overview_week_data = parse_obj_as(OverviewWeekData, data)
    return overview_week_data

  def forecast(self,
    area_id: str=None,
    base_url='https://www.jma.go.jp/bosai/forecast/data/forecast/{area_id}.json',
    data=None,
  ) -> ForecastData:
    if data is None:
      assert area_id is not None
      url = base_url.format(**{
        'area_id': area_id,
      })
      data = get_json(url)
    forecast_data = parse_obj_as(ForecastData, data)
    return forecast_data

  def warning(self,
    area_id: str=None,
    base_url='https://www.jma.go.jp/bosai/warning/data/warning/{area_id}.json',
    data=None,
  ) -> WarningData:
    if data is None:
      assert area_id is not None
      url = base_url.format(**{
        'area_id': area_id,
      })
      data = get_json(url)
    warning_data = parse_obj_as(WarningData, data)
    return warning_data
