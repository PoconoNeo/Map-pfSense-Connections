from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    # Read the geolocation data from the JSON file
    with open("D:\\WebServer\\dst_ip_geotag.json", "r") as file:
        data = json.load(file)
    # Pass the data to the template
    return render_template('index.html', data=json.dumps(data))

@app.route('/data')
def data():
    # Serve the contents of the JSON file
    with open("D:\\WebServer\\dst_ip_geotag.json", "r") as file:
        json_data = json.load(file)
    # jsonify will set the correct content-type headers for JSON
    return jsonify(json_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
