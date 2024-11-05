from dataclasses import dataclass
from enum import Enum


class UploadMeasurementsFormats(Enum):
    JSON = "json"
    CSV = "csv"


@dataclass
class UploadLinkMeasurementsResponse:
    url: str
    fields: dict[str, str]
