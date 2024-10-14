from dataclasses import dataclass


@dataclass
class Plant:
    site_id: str
    image: str
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

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
    