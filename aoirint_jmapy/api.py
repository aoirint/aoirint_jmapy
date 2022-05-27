import requests
from typing import List, Dict, Any, Optional, Union, Literal
from pydantic import BaseModel, parse_obj_as
from urllib.parse import urljoin
from dataclasses import dataclass
from . import __VERSION__ as VERSION

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

@dataclass
class JmaApi:
  jma_url: str = 'https://www.jma.go.jp'
  app_name: Optional[str] = None
  app_version: Optional[str] = None
  useragent: Optional[str] = None

  def get_json(self, url) -> Dict[str, Any]:
    useragent = f'aoirint_jmapy {VERSION}'

    if self.useragent is not None:
      useragent = self.useragent
    elif self.app_name is not None and self.app_version:
      useragent = f'{self.app_name} {self.app_version} / {useragent}'
    elif self.app_name is not None:
      useragent = f'{self.app_name} / {useragent}'

    headers = {
      'User-Agent': useragent,
    }

    res = requests.get(url, headers=headers)
    res.raise_for_status()

    data = res.json()
    return data

  @property
  def area_url(self):
    return urljoin(self.jma_url, 'bosai/common/const/area.json')

  def area(self,
    url: str=None,
    data=None,
  ) -> AreaData:
    if data is None:
      if url is None:
        url = self.area_url
      data = self.get_json(url)
    area = parse_obj_as(AreaData, data)
    return area

  @property
  def forecast_area_url(self):
    return urljoin(self.jma_url, 'bosai/forecast/const/forecast_area.json')

  def forecast_area(self,
    url: str=None,
    data=None,
  ) -> ForecastAreaData:
    if data is None:
      if url is None:
        url = self.forecast_area_url
      data = self.get_json(url)
    forecast_area_data = parse_obj_as(ForecastAreaData, data)
    return forecast_area_data

  @property
  def en_amedas_url(self):
    return urljoin(self.jma_url, 'bosai/forecast/const/en_amedas.json')

  def en_amedas(self,
    url: str=None,
    data=None,
  ) -> EnAmedasData:
    if data is None:
      if url is None:
        url = self.en_amedas_url
      data = self.get_json(url)
    en_amedas_data = parse_obj_as(EnAmedasData, data)
    return en_amedas_data

  @property
  def anniversary_url(self):
    return urljoin(self.jma_url, 'bosai/forecast/const/anniversary.json')

  def anniversary(self,
    url: str=None,
    data=None,
  ) -> AnniversaryData:
    if data is None:
      if url is None:
        url = self.anniversary_url
      data = self.get_json(url)
    anniversary_data = parse_obj_as(AnniversaryData, data)
    return anniversary_data

  @property
  def week_area_url(self):
    return urljoin(self.jma_url, 'bosai/forecast/const/week_area.json')

  def week_area(self,
    url: str=None,
    data=None,
  ) -> WeekAreaData:
    if data is None:
      if url is None:
        url = self.week_area_url
      data = self.get_json(url)
    week_area_data = parse_obj_as(WeekAreaData, data)
    return week_area_data

  @property
  def week_area05_url(self):
    return urljoin(self.jma_url, 'bosai/forecast/const/week_area05.json')

  def week_area05(self,
    url: str=None,
    data=None,
  ) -> WeekArea05Data:
    if data is None:
      if url is None:
        url = self.week_area05_url
      data = self.get_json(url)
    week_area05_data = parse_obj_as(WeekArea05Data, data)
    return week_area05_data

  @property
  def week_area_name_url(self):
    return urljoin(self.jma_url, 'bosai/forecast/const/week_area_name.json')

  def week_area_name(self,
    url: str=None,
    data=None,
  ) -> WeekAreaNameData:
    if data is None:
      if url is None:
        url = self.week_area_name_url
      data = self.get_json(url)
    week_area_name_data = parse_obj_as(WeekAreaNameData, data)
    return week_area_name_data

  @property
  def overview_forecast_url(self):
    return urljoin(self.jma_url, 'bosai/forecast/data/overview_forecast/{area_id}.json')

  def overview_forecast(self,
    area_id: str=None,
    base_url: str=None,
    data=None,
  ) -> OverviewForecastData:
    if data is None:
      assert area_id is not None
      if base_url is None:
        base_url = self.overview_forecast_url
      url = base_url.format(**{
        'area_id': area_id,
      })
      data = self.get_json(url)
    overview_forecast_data = parse_obj_as(OverviewForecastData, data)
    return overview_forecast_data

  @property
  def overview_week_url(self):
    return urljoin(self.jma_url, 'bosai/forecast/data/overview_week/{area_id}.json')

  def overview_week(self,
    area_id: str=None,
    base_url: str=None,
    data=None,
  ) -> OverviewWeekData:
    if data is None:
      assert area_id is not None
      if base_url is None:
        base_url = self.overview_forecast_url
      url = base_url.format(**{
        'area_id': area_id,
      })
      data = self.get_json(url)
    overview_week_data = parse_obj_as(OverviewWeekData, data)
    return overview_week_data

  @property
  def forecast_url(self):
    return urljoin(self.jma_url, 'bosai/forecast/data/forecast/{area_id}.json')

  def forecast(self,
    area_id: str=None,
    base_url: str=None,
    data=None,
  ) -> ForecastData:
    if data is None:
      assert area_id is not None
      if base_url is None:
        base_url = self.forecast_url
      url = base_url.format(**{
        'area_id': area_id,
      })
      data = self.get_json(url)
    forecast_data = parse_obj_as(ForecastData, data)
    return forecast_data

  @property
  def warning_url(self):
    return urljoin(self.jma_url, 'bosai/warning/data/warning/{area_id}.json')

  def warning(self,
    area_id: str=None,
    base_url: str=None,
    data=None,
  ) -> WarningData:
    if data is None:
      assert area_id is not None
      if base_url is None:
        base_url = self.warning_url
      url = base_url.format(**{
        'area_id': area_id,
      })
      data = self.get_json(url)
    warning_data = parse_obj_as(WarningData, data)
    return warning_data
