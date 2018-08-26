import os
from flask import Flask
from dotenv import load_dotenv

# Load env variables to app scope
load_dotenv()

# Flask app config dict
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
        user=os.getenv('DBUSER', ''),
        passwd=os.getenv('DBPASS', ''),
        host=os.getenv('DBHOST', ''),
        port=os.getenv('DBPORT', ''),
        db=os.getenv('DBNAME', ''))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secretkey'

# Importing the database after the app has been created
from models import db
from nass_crop_conditions_kansas import fetch_data_and_send_to_db

if __name__ == '__main__':
    db_flag = False
    while db_flag == False:
        try:
            db.create_all()
        except:
            time.sleep(2)
        else:
            db_flag = True
    app.run(debug=True, host='0.0.0.0')