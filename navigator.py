from dotenv import dotenv_values
import streamlit as st
import requests
import xml.etree.ElementTree as ET

# Load configuration values from a .env file into a dictionary
config = dotenv_values()

# Retrieve the API_KEY value from the dictionary
API_KEY = config.get('API_KEY')

def prediction_forecast(lat, lon):
    # Construct the API URL for marine weather data
    base_url = f"http://api.worldweatheronline.com/premium/v1/marine.ashx?key={API_KEY}&format=xml&q={lat},{lon}"

    # Send a GET request to the API
    response = requests.get(base_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the XML response
        root = ET.fromstring(response.content)

        # Iterate over each 'weather' element in the XML response
        for weather_elem in root.findall(".//weather"):
            # Extract and display date, max temperature, and min temperature
            date = weather_elem.find("date").text
            max_temp_C = weather_elem.find(".//maxtempC").text
            min_temp_C = weather_elem.find(".//mintempC").text

            # Display date and temperature information
            st.subheader(f"Weather Forecast for {date}:")
            st.write(f"- Max Temperature: {max_temp_C}°C")
            st.write(f"- Min Temperature: {min_temp_C}°C")

            # Extract and display hourly weather data
            hourly_data = weather_elem.findall(".//hourly")
            for hour_data in hourly_data:
                # Extract various weather attributes for each hour
                time = hour_data.find("time").text
                temp_C = hour_data.find(".//tempC").text
                temp_F = hour_data.find(".//tempF").text
                windspeed_Miles = hour_data.find(".//windspeedMiles").text
                windspeed_Kmph = hour_data.find(".//windspeedKmph").text
                weather_desc = hour_data.find(".//weatherDesc").text
                humidity = hour_data.find(".//humidity").text
                visibility = hour_data.find(".//visibility").text
                pressure = hour_data.find(".//pressure").text
                cloudcover = hour_data.find(".//cloudcover").text
                sigHeight_m = hour_data.find(".//sigHeight_m").text
                swellHeight_m = hour_data.find(".//swellHeight_m").text
                swellHeight_ft = hour_data.find(".//swellHeight_ft").text
                swellDir16Point = hour_data.find(".//swellDir16Point").text
                uvIndex = hour_data.find(".//uvIndex").text
                winddir16Point = hour_data.find(".//winddir16Point").text
                weatherCode = hour_data.find(".//weatherCode").text

                # Display hourly weather data
                st.subheader(f"Hourly Forecast for {date}, {time}:")
                st.write(f"- Temperature: {temp_C}°C ({temp_F}°F)")
                st.write(f"- Wind Speed: {windspeed_Miles} mph ({windspeed_Kmph} km/h)")
                st.write(f"- Wind Direction (16-point): {winddir16Point}")
                st.write(f"- Weather Code: {weatherCode}")
                st.write(f"- Weather Description: {weather_desc}")
                st.write(f"- Humidity: {humidity}%")
                st.write(f"- Visibility: {visibility} km")
                st.write(f"- Pressure: {pressure} mb")
                st.write(f"- Cloud Cover: {cloudcover}%")
                st.write(f"- Significant Wave Height: {sigHeight_m} meters")
                st.write(f"- Swell Height: {swellHeight_m} meters ({swellHeight_ft} feet)")
                st.write(f"- Swell Direction: {swellDir16Point}")
                st.write(f"- UV Index: {uvIndex}")
    else:
        st.error(f"Error fetching data. Status code: {response.status_code}")


def get_current_weather_data(lat, lon):
    # Construct the API URL for current weather data
    base_url = f"http://api.worldweatheronline.com/premium/v1/weather.ashx?key={API_KEY}&format=xml&q={lat},{lon}"
    
    # Send a GET request to the API
    response = requests.get(base_url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        
        # Parse the XML response
        root = ET.fromstring(response.content)
        
        # Extract current condition data
        current_condition = root.find(".//current_condition")
        observation_time = current_condition.find("observation_time").text
        temp_C = current_condition.find("temp_C").text
        temp_F = current_condition.find("temp_F").text
        windspeedMiles = current_condition.find("windspeedMiles").text
        windspeedKmph = current_condition.find("windspeedKmph").text
        winddir16Point = current_condition.find("winddir16Point").text
        weatherCode = current_condition.find("weatherCode").text
        weatherDesc = current_condition.find("weatherDesc").text
        humidity = current_condition.find("humidity").text
        visibility = current_condition.find("visibility").text
        visibilityMiles = current_condition.find("visibilityMiles").text
        pressure = current_condition.find("pressure").text
        pressureInches = current_condition.find("pressureInches").text
        cloudcover = current_condition.find("cloudcover").text
        
        # Extract weather information
        weather = root.find(".//weather")
        date = weather.find("date").text
        uvIndex = weather.find("uvIndex").text
       
        # Extract astronomy information
        astronomy = root.find(".//astronomy")
        sunrise = astronomy.find("sunrise").text
        sunset = astronomy.find("sunset").text
        
        # Display current condition data
        st.subheader("Current Condition:")
        st.write(f"- Observation Time: {observation_time} UTC")
        st.write(f"- Temperature: {temp_C}°C ({temp_F}°F)")
        st.write(f"- Wind Speed: {windspeedMiles} mph ({windspeedKmph} km/h)")
        st.write(f"- Wind Direction (16-point): {winddir16Point}")
        st.write(f"- Weather Code: {weatherCode}")
        st.write(f"- Weather Description: {weatherDesc}")
        st.write(f"- Humidity: {humidity}%")
        st.write(f"- Visibility: {visibility} km ({visibilityMiles} miles)")
        st.write(f"- Pressure: {pressure} mb ({pressureInches} inches)")
        st.write(f"- Cloud Cover: {cloudcover}%")
       
        # Display weather information
        st.subheader("Weather Information:")
        st.write(f"- Date: {date}")
        st.write(f"- UV Index: {uvIndex}")
        
        # Display astronomy information
        st.subheader("Astronomy Information:")
        st.write(f"- Sunrise: {sunrise}")
        st.write(f"- Sunset: {sunset}")
    else:
        st.error(f"Error fetching data. Status code: {response.status_code}")

def main():
    st.set_page_config(page_title="Nautical Navigator")
    st.title("Ahoy, matey! This here application be fer 'elpin' the Cap'n navigate the seas by givin' 'im the forecast an' wave data.")
    
    # Radio button to select weather data option
    data_option = st.radio("Select Weather Data Option", ["Current Weather Data", "Prediction Forecast"])

    if data_option == "Current Weather Data":
        lat_input = st.text_input("Enter yer latitude: (-90 to 90)")
        lon_input = st.text_input("Enter yer longitude: (-180 to 180)")
        if st.button("Submit"):
            try:
                lat = float(lat_input)
                lon = float(lon_input)
                if -90.0 <= lat <= 90.0 and -180.0 <= lon <= 180.0:
                    get_current_weather_data(lat, lon)
                else:
                    st.warning("Please enter valid latitude 'n longitude values within the specified range.")
            except ValueError:
                st.warning("Please enter valid latitude 'n longitude values.")
    else:
        lat_input = st.text_input("Enter yer latitude: (-90 to 90)")
        lon_input = st.text_input("Enter yer longitude: (-180 to 180)")
        if st.button("Submit"):
            try:
                lat = float(lat_input)
                lon = float(lon_input)
                if -90.0 <= lat <= 90.0 and -180.0 <= lon <= 180.0:
                    prediction_forecast(lat, lon)
                else:
                    st.warning("Please enter valid latitude 'n longitude values within the specified range.")
            except ValueError:
                st.warning("Please enter valid latitude 'n longitude values.")

if __name__ == '__main__':
    main()