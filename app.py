from flask import Flask, jsonify
import datetime
import os
import pytz

app = Flask(__name__)

@app.route('/')
def get_info():
    now_utc = datetime.datetime.now(pytz.utc)
    azure_region = os.environ.get('LOCATION', 'Unknown Azure Region')

    response = {
        "current_time_utc": now_utc.strftime("%Y-%m-%d %H:%M:%S UTC"),
        "location_region": azure_region,
        "message": "Hello from Azure Container Apps via Azure Portal!"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
