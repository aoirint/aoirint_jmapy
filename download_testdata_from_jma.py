import logging
import json
import time
import requests
from logging import getLogger
from pathlib import Path
from typing import List
from pydantic import BaseModel
from aoirint_jmapy import JmaApi

logger = getLogger(__name__)


class DownloadFileEntry(BaseModel):
    url: str
    output_path: Path


def download_text_file(url: str, output_path: Path, output_encoding: str) -> None:
    res = requests.get(url)
    res.raise_for_status()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(res.text, encoding=output_encoding)


def download_test_data_from_jma(test_data_dir: Path) -> None:
    test_data_area_path = test_data_dir / "area.json"
    sleep_interval = 1

    download_file_entries: List[DownloadFileEntry] = [
        DownloadFileEntry(
            url="https://www.jma.go.jp/bosai/common/const/area.json",
            output_path=test_data_area_path,
        ),
        DownloadFileEntry(
            url="https://www.jma.go.jp/bosai/forecast/const/forecast_area.json",
            output_path=test_data_dir / "forecast_area.json",
        ),
        DownloadFileEntry(
            url="https://www.jma.go.jp/bosai/forecast/const/en_amedas.json",
            output_path=test_data_dir / "en_amedas.json",
        ),
        DownloadFileEntry(
            url="https://www.jma.go.jp/bosai/forecast/const/anniversary.json",
            output_path=test_data_dir / "anniversary.json",
        ),
        DownloadFileEntry(
            url="https://www.jma.go.jp/bosai/forecast/const/week_area.json",
            output_path=test_data_dir / "week_area.json",
        ),
        DownloadFileEntry(
            url="https://www.jma.go.jp/bosai/forecast/const/week_area05.json",
            output_path=test_data_dir / "week_area05.json",
        ),
        DownloadFileEntry(
            url="https://www.jma.go.jp/bosai/forecast/const/week_area_name.json",
            output_path=test_data_dir / "week_area_name.json",
        ),
    ]

    for download_file_entry in download_file_entries:
        logger.info(f"Downloading {download_file_entry.output_path} from {download_file_entry.url}.")
        download_text_file(
            url=download_file_entry.url,
            output_path=download_file_entry.output_path,
            output_encoding="utf-8",
        )
        time.sleep(sleep_interval)

    area_data = json.loads(test_data_area_path.read_text(encoding="utf-8"))
    area = JmaApi().area(data=area_data)

    area_download_file_entries: List[DownloadFileEntry] = []
    office_codes: list[str] = []
    for office_code in area.offices.keys():
        office_codes.append(office_code)

    logger.info(f"Found {len(office_codes)} office codes.")

    for office_code in office_codes:
        # TODO: overview_week
        area_download_file_entries.append(
            DownloadFileEntry(
                url=f"https://www.jma.go.jp/bosai/forecast/data/overview_week/{office_code}.json",
                output_path=test_data_dir / f"overview_week/{office_code}.json",
            ),
        )
        area_download_file_entries.append(
            DownloadFileEntry(
                url=f"https://www.jma.go.jp/bosai/forecast/data/overview_forecast/{office_code}.json",
                output_path=test_data_dir / f"overview_forecast/{office_code}.json",
            ),
        )
        area_download_file_entries.append(
            DownloadFileEntry(
                url=f"https://www.jma.go.jp/bosai/forecast/data/forecast/{office_code}.json",
                output_path=test_data_dir / f"forecast/{office_code}.json",
            ),
        )
        area_download_file_entries.append(
            DownloadFileEntry(
                url=f"https://www.jma.go.jp/bosai/warning/data/warning/{office_code}.json",
                output_path=test_data_dir / f"warning/{office_code}.json",
            ),
        )

    for download_file_entry in area_download_file_entries:
        logger.info(f"Downloading {download_file_entry.output_path} from {download_file_entry.url}.")
        download_text_file(
            url=download_file_entry.url,
            output_path=download_file_entry.output_path,
            output_encoding="utf-8",
        )
        time.sleep(sleep_interval)


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s : %(message)s",
    )

    test_data_dir = Path("testdata")

    download_test_data_from_jma(test_data_dir=test_data_dir)


if __name__ == "__main__":
    main()
