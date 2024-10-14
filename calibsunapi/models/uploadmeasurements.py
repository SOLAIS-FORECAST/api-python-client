from enum import Enum
from dataclasses import dataclass


class UploadMeasurementsFormats(Enum):
    JSON = "json"
    CSV = "csv"


@dataclass
class UploadLinkMeasurementsResponse:
    url: str
    fields: dict[str, str]
