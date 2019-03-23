# Weatheria
A simple web application that provides weather information of queried city using OpenMapWeather API.

## Getting Started

### Installing
* Create a virtual environment with python3 and pip3 (recommended)
* Install required python dependencies 
  ```
    pip3 install -r requirements.txt
  ```
* Change to project root directory (with manage.py file)
  ```
    cd src
  ```
* Get your own OpenMapWeather API Key and update API_KEY variable in views.py file in shorten module
* Run the local server from project root directory
  ```
    python3 manage.py runserver
  ```
* Access the website in your browser at ```http://localhost:8000```
