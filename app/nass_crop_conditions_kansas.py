import os
import requests
from __main__ import db
from models import crop_conditions_kansas

def build_request_query(condition, timeframe):
    return {
        "api_key": os.getenv('NASS_API_KEY', ''),
        "crop": "CORN",
        "condition": condition,
        "timeframe": timeframe,
        "state": "KS",
        "frequency": "WEEKLY",
        "description": "CORN - CONDITION, MEASURED IN PCT EXCELLENT"
    }

def format_request_url(query_dict):    
    return (
        "https://quickstats.nass.usda.gov/api/api_GET/?"
        "key={api_key}&"
        "commodity_desc={crop}&"
        "{condition}={timeframe}&"
        "state_alpha={state}&"
        "freq_desc={frequency}&"
        "short_desc={description}&"
        "format=JSON"
    ).format(**query_dict)

def fetch_data_and_send_to_db():
    """This function checks wethere or not the database is up to date
    calls the NASS api by constructing the necesary queries

    :return: param[object]: request
    """

    # Grabbing last record from the database,
    record = crop_conditions_kansas.query.order_by(
                crop_conditions_kansas.week_ending.desc()
            ).first()

    if record is None:
        # Makes request if no record is found
        query = build_request_query('year__GE', '2012')
        request = requests.get(format_request_url(query))

        send_to_db(request)
    else:
        # If record is found checks to add 
        query = build_request_query('week_ending__GT', record.week_ending)
        request = requests.get(format_request_url(query))
        send_to_db(request)
    


def send_to_db(request):
    """This function checks the reqeust code, normalizez the data
    and inserts into the database

    :param param[object] request: The request object from the API
    :return: None
    """

    if request.status_code == 200:
        db_rows = request.json()['data']
        
        # Data manipulation, removed CV (%) from object
        for idx in range(len(db_rows)):
            try:
                db_rows[idx]["value"] = db_rows[idx].pop("Value")
                del db_rows[idx]['CV (%)']
            except KeyError:
                pass

        db.session.bulk_insert_mappings(crop_conditions_kansas, db_rows)   
        db.session.commit()
