# PfSense Connection Report Viewer v1.0

## Overview

This project processes logs from a PfSense firewall to create a report that includes geolocation data for IP addresses. The data is then visualized on an interactive map using a Flask web server.

## Features

- Processes PfSense firewall logs.
- Generates a JSON report with IP geolocation data.
- Visualizes active connections on an interactive map.
- Easy to set up and run with minimal configuration.

## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.x: The programming language used for both scripts.
- Flask: A micro web framework for Python, used to serve the web application.
- Requests: A Python library used for making HTTP requests (if your scripts require external API calls).

Install Python and pip, then use pip to install the required packages:

	pip install flask requests

Installation
- To set up the project on your local machine:
	- Clone the repository from GitHub or download the project files.
	- Navigate to the project directory.
	- Install the required dependencies.
Configuration
- - Edit pfsense_connection_report.py and app.py as needed to point to the correct file paths and configure any necessary credentials for accessing the PfSense firewall.

Running the Application
- For Unix-like systems, use the provided shell script:

	./run_reports.sh

- For Windows, execute the batch file:

	run_reports.bat

The Flask server will start, and the web application will be available at http://localhost:81

Usage
Once the web server is running, access http://localhost:81 in your web browser to view the interactive map. 
Pins on the map represent active connections.

Click on a pin to see detailed information about the connection, such as the IP address and geolocation data.

File Descriptions
pfsense_connection_report.py: Python script that parses the PfSense firewall logs and generates a JSON file containing the geolocation data.
app.py: The Flask application that reads the JSON data and serves the web page to display the map.
run_reports.sh/run_reports.bat: Scripts to automate the execution of pfsense_connection_report.py and start the Flask web server.
Contributing
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change. 
Please ensure to update tests as appropriate.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Leaflet.js for the interactive map visualization.
ip-api for providing IP geolocation data.
