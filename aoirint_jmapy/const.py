
import importlib.resources as ILR
import json
from pydantic import parse_obj_as
from typing import Dict, List

TelopsData = Dict[str, List[str]]

Telops = parse_obj_as(TelopsData, json.loads(ILR.read_text('aoirint_jmapy.static', 'const_telops.json')))
