from flask import Flask, jsonify
from dotenv import load_dotenv
import requests
import os
import xml.etree.ElementTree as ET


# Load configuration values from a .env file
load_dotenv()

# Retrieve the API_KEY value from the dictionary
API_KEY = os.environ.get("API_KEY")

app = Flask(__name__)

@app.route('/')
def hello_world(): 
    return jsonify(find_current_weather(40.7128, 74.0060))

@app.route("/<id>")
def getId(id):
    return f'Your id is: {id}'

"""
Fetches current marine weather data based on latitude and longitude.

Args:
    lat (float): Latitude value (-90 to 90 degrees).
    lon (float): Longitude value (-180 to 180 degrees).

Returns:
    None
"""
def find_current_weather(lat, lon):
    base_url = f"http://api.worldweatheronline.com/premium/v1/marine.ashx?key={API_KEY}&format=json&q={lat},{lon}"

    # Send the API request
    response = requests.get(base_url)

    print("code:", response.status_code, "content:", response.content)

    # Check if the API request was successful (status code 200)
    if response.status_code == 200:
        # Parse the XML response content
        root = ET.fromstring(response.content)
        meta_data = {}

        print("root:", root)
        
        # Iterate over each 'weather' element in the XML response
        for weather_elem in root.findall(".//weather"):
            # Extract and display date, max temperature, and min temperature
            meta_data["date"] = weather_elem.find("date").text
            meta_data["max_temp_C"] = weather_elem.find(".//maxtempC").text
            meta_data["min_temp_C"] = weather_elem.find(".//mintempC").text

            print("date:", weather_elem.find("date").text)

            # Extract and display hourly weather data
            hourly_data = weather_elem.findall(".//hourly")
            for hour_data in hourly_data:
                # Extract various weather attributes for each hour
                meta_data["time"] = hour_data.find("time").text
                meta_data["temp_C"] = hour_data.find(".//tempC").text
                meta_data["temp_F"] = hour_data.find(".//tempF").text
                meta_data["windspeed_Miles"] = hour_data.find(".//windspeedMiles").text
                meta_data["windspeed_Kmph"] = hour_data.find(".//windspeedKmph").text
                meta_data["weather_desc"] = hour_data.find(".//weatherDesc").text
                meta_data["humidity"] = hour_data.find(".//humidity").text
                meta_data["visibility"] = hour_data.find(".//visibility").text
                meta_data["pressure"] = hour_data.find(".//pressure").text
                meta_data["cloudcover"] = hour_data.find(".//cloudcover").text
                meta_data["sigHeight_m"] = hour_data.find(".//sigHeight_m").text
                meta_data["swellHeight_m"] = hour_data.find(".//swellHeight_m").text
                meta_data["swellHeight_ft"] = hour_data.find(".//swellHeight_ft").text
                meta_data["swellDir16Point"] = hour_data.find(".//swellDir16Point").text
                meta_data["uvIndex"] = hour_data.find(".//uvIndex").text
                meta_data["winddir16Point"] = hour_data.find(".//winddir16Point").text
                meta_data["weatherCode"] = hour_data.find(".//weatherCode").text

            # Extract and display astronomy data (sunrise and sunset)
            astronomy_data = weather_elem.find(".//astronomy")
            meta_data["sunrise"] = astronomy_data.find("sunrise").text
            meta_data["sunset"] = astronomy_data.find("sunset").text
         
            # Extract and display tide data (tide type)
            tide_data = weather_elem.find(".//tide")
            if tide_data is not None:
                meta_data["tide_type"] = tide_data.find(".//tide_type").text
            else:
                print("No tide data available")
    else:
        print(f"Error fetching data. Status code: {response.status_code}")
    
    print("len of meta_data:", len(meta_data))
    return meta_data

if __name__ == '__main__':
    app.run(debug=True)