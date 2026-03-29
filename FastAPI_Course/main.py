import zoneinfo
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


country_timezones = {
    "MX": "America/Mexico_City",
    "CO": "America/Bogota",
    "BR": "America/Sao_Paulo",
    "PE": "America/Lima",
}


@app.get("/time/{iso_code}")
async def time(iso_code: str):
    iso = iso_code.upper()
    timezone_str = country_timezones.get(iso)
    if timezone_str is None:
        return {"error": "Country code not found"}
    tz = zoneinfo.ZoneInfo(timezone_str)
    return {"timestamp": datetime.now(tz)}
