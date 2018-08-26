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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')