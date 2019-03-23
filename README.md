# Weatheria
A simple web application that provides weather information of queried city using OpenMapWeather API.

## Getting Started

### Installing
* Create a virtual environment with python3 and pip3 (recommended)
* Change to project root directory (with manage.py file)
* Install required python dependencies 
```
pip3 install -r requirements.txt
```
* Get your own OpenMapWeather API Key and update API_KEY variable in views.py file located in 'shorten' module
* Run the local server
```
python3 manage.py runserver
```
* Access the website in your browser at ```http://localhost:8000```
