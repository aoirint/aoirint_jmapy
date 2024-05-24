
import importlib.resources as ILR
import json
from pydantic import TypeAdapter
from typing import Dict, List

TelopsData = Dict[str, List[str]]

Telops = TypeAdapter(TelopsData).validate_python(json.loads(ILR.read_text('aoirint_jmapy.static', 'const_telops.json')))
