import os
import requests

# Building the query dict
QUERYDICT = {
    "api_key": os.getenv('NASS_API_KEY', ''),
    "crop": "CORN",
    "year": 2012, 
    "state": "KS",
    "frequency": "WEEKLY",
    "condition": "CORN - CONDITION, MEASURED IN PCT EXCELLENT"
}

REQUEST_URL = (
        "https://quickstats.nass.usda.gov/api/api_GET/?"
        "key={api_key}&"
        "commodity_desc={crop}&"
        "year__GE={year}&"
        "state_alpha={state}&"
        "freq_desc={frequency}&"
        "short_desc={condition}&"
        "format=JSON"
    ).format(**QUERYDICT)

def fetch_data_and_send_to_db():
    request = requests.get(REQUEST_URL)
    if request.status_code == 200:
        db_rows = request.json()['data']
    
    """ Some data manipulation before sending to db
        removed CV (%) from object and normalized value
        field
    """
    if db_rows:
        for idx in range(len(db_rows)):
            try:
                db_rows[idx]["value"] = db_rows[idx].pop("Value")
                del db_rows[idx]['CV (%)']
            except KeyError:
                pass
