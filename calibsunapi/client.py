from typing import Union, Any, Optional
import os
import logging
from io import BytesIO
import json
from calibsunapi.token import Token
from calibsunapi.endpoints import EndpointRoutes
from calibsunapi.models.listplants import Plant
from calibsunapi.models.uploadmeasurements import UploadMeasurementsFormats, UploadLinkMeasurementsResponse

import requests


class CalibsunApiClient:
    _token: Union[Token, None] = None

    def __init__(self, calibsun_client_id: Union[str, None] = None, calibsun_client_secret: Union[str, None] = None):
        self.calibsun_client_id = os.getenv("CALIBSUN_CLIENT_ID", calibsun_client_id)
        self.calibsun_client_secret = os.getenv("CALIBSUN_CLIENT_SECRET", calibsun_client_secret)
        if self.calibsun_client_id is None:
            logging.warning("CALIBSUN_CLIENT_ID not supplied.")
        if self.calibsun_client_secret is None:
            logging.warning("CALIBSUN_CLIENT_SECRET not supplied.")

    def _authenticate(self):
        response = requests.post(
            EndpointRoutes.TOKEN,
            json={
                "client_id": self.calibsun_client_id,
            },
            headers={"x-api-key": self.calibsun_client_secret}
        )
        response.raise_for_status()
        self._token = Token(**response.json())

    @property
    def _auth_headers(self):
        if self.token.access_token:
            return {"Authorization": f"Bearer {self.token.access_token}"}
        else:
            return {}
    
    @property
    def token(self) -> Token:
        if self._token is None or self._token.is_expired():
            self._authenticate()
        return self._token
    
    def get(self, *args, **kwargs):
        return requests.get(*args, **kwargs, headers=self._auth_headers)
    
    def post(self, *args, **kwargs):
        return requests.post(*args, **kwargs, headers=self._auth_headers)
    
    def list_plants(self) -> list[Plant]:
        response = self.get(EndpointRoutes.LISTPLANT)
        response.raise_for_status()
        return [Plant(site_id=plant, **config) for plant, config in response.json().items()]
    
    def _get_upload_parameters(self, site_id: str, format: UploadMeasurementsFormats) -> UploadLinkMeasurementsResponse:
        response = self.get(EndpointRoutes.UPLOAD.format(site_id=site_id, format=format.value))
        response.raise_for_status()
        return UploadLinkMeasurementsResponse(**response.json())
    
    def push_measurements(self, site_id: str, format: UploadMeasurementsFormats = UploadMeasurementsFormats.JSON,
                          filepath: Optional[str] = None, data: Optional[Any] = None) -> requests.Response:
        if filepath is not None:
            filelike = open(filepath, "r")
        elif data is not None:
            filelike = BytesIO()
            filelike.write(json.dumps(data).encode("utf-8"))
            filelike.seek(0)
        parameters = self._get_upload_parameters(site_id, format)
        reponse = self.post(url=parameters.url, files={"file": filelike}, data=parameters.fields)
        reponse.raise_for_status()
        return reponse

    def get_latest_forecast(self, site_id: str, target: str) -> dict:
        response = self.get(EndpointRoutes.LATESTFORECAST.format(site_id=site_id, target=target))
        response.raise_for_status()
        return response.json()
    
    def get_latest_forecast_probabilistic(self, site_id: str, target: str) -> dict:
        response = self.get(EndpointRoutes.LATESTFORECAST_PROBA.format(site_id=site_id, target=target))
        response.raise_for_status()
        return response.json()
    
    def get_latest_forecast_deterministic(self, site_id: str, target: str) -> dict:
        response = self.get(EndpointRoutes.LATESTFORECAST_DET.format(site_id=site_id, target=target))
        response.raise_for_status()
        return response.json()
    
    def get_latest_forecast_demo(self, target: str) -> dict:
        response = self.get(EndpointRoutes.LATESTFORECASTDEMO.format(target=target))
        response.raise_for_status()
        return response.json()
    
    def get_latest_forecast_demo_probabilistic(self, target: str) -> dict:
        response = self.get(EndpointRoutes.LATESTFORECASTDEMO_PROBA.format(target=target))
        response.raise_for_status()
        return response.json()
    
    def get_latest_forecast_demo_deterministic(self, target: str) -> dict:  
        response = self.get(EndpointRoutes.LATESTFORECASTDEMO_DET.format(target=target))
        response.raise_for_status()
        return response.json()
    
    def get_forecast(self, time: str, site_id: str, target: str) -> dict:
        response = self.get(EndpointRoutes.FIXEDTIMEFORECAST.format(time=time, site_id=site_id, target=target))
        response.raise_for_status()
        return response.json()
    
    def get_deterministic_forecast(self, time: str, site_id: str, target: str) -> dict:
        response = self.get(EndpointRoutes.FIXEDTIMEFORECAST_DET.format(time=time, site_id=site_id, target=target))
        response.raise_for_status()
        return response.json()
    
    def get_probabilistic_forecast(self, time: str, site_id: str, target: str) -> dict:
        response = self.get(EndpointRoutes.FIXEDTIMEFORECAST_PROBA.format(time=time, site_id=site_id, target=target))
        response.raise_for_status()
        return response.json()