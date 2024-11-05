from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from calibsunapi.client import CalibsunApiClient


@dataclass
class Plant:
    site_id: str
    name: str
    latitude: str
    longitude: str
    elevation: str
    peakpower: str
    tilt: str
    azimut: str
    tilt_gti: str
    azimut_gti: str
    rendement_stc: str
    coefficient_temperature: str
    DC_AC: str
    tracker: str
    backtracking: str
    maxangle: str
    entraxe: str
    L_panel: str
    gti: str
    ghi: str
    resolution: str
    frequency: str
    production: str
    horizon: str
    subscription_type: str
    activated: str

    client: Optional["CalibsunApiClient"] = None

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Plant({self.name.capitalize()})"

    def push_measurements(self, format: str, data: dict[str, str] = None, filepath: str = None):
        return self.client.push_measurements(self.site_id, format, data=data, filepath=filepath)

    def get_latest_forecast(self, target: str):
        return self.client.get_latest_forecast(self.site_id, target)

    def get_latest_forecast_probabilistic(self, target: str):
        return self.client.get_latest_forecast_probabilistic(self.site_id, target)

    def get_latest_forecast_deterministic(self, target: str):
        return self.client.get_latest_forecast_deterministic(self.site_id, target)

    def get_forecast(self, time: str, target: str):
        return self.client.get_forecast(self.site_id, target, time)

    def get_probabilistic_forecast(self, time: str, target: str):
        return self.client.get_probabilistic_forecast(self.site_id, target, time)

    def get_deterministic_forecast(self, time: str, target: str):
        return self.client.get_deterministic_forecast(self.site_id, target, time)
