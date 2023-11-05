from dotenv import dotenv_values
import streamlit as st
import requests
import xml.etree.ElementTree as ET

# Load configuration values from a .env file into a dictionary
config = dotenv_values()

# Retrieve the API_KEY value from the dictionary
API_KEY = config.get('API_KEY')


def find_current_weather(lat, lon):
    """
    Fetches current marine weather data based on latitude and longitude.

    Args:
        lat (float): Latitude value (-90 to 90 degrees).
        lon (float): Longitude value (-180 to 180 degrees).

    Returns:
        None
    """
    # Construct the URL for the API request
    base_url = f"http://api.worldweatheronline.com/premium/v1/marine.ashx?key={API_KEY}&format=xml&q={lat},{lon}"

    # Send the API request
    response = requests.get(base_url)

    # Check if the API request was successful (status code 200)
    if response.status_code == 200:
        # Parse the XML response content
        root = ET.fromstring(response.content)

        # Iterate over each 'weather' element in the XML response
        for weather_elem in root.findall(".//weather"):
            # Extract and display date, max temperature, and min temperature
            date = weather_elem.find("date").text
            max_temp_C = weather_elem.find(".//maxtempC").text
            min_temp_C = weather_elem.find(".//mintempC").text
            st.write(f"Date: {date}, Max Temp: {max_temp_C}°C, Min Temp: {min_temp_C}°C")

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
                st.write(f"Time: {time}, Temp: {temp_C}°C ({temp_F}°F), Wind Speed: {windspeed_Miles} mph ({windspeed_Kmph} km/h),  Wind Direction (16-point): {winddir16Point}")
                st.write(f"Weather Code: {weatherCode}, Weather: {weather_desc}")
                st.write(f"Humidity: {humidity}%, Visibility: {visibility} km, Pressure: {pressure} mb, Cloud Cover: {cloudcover}%")
                st.write(f"Significant Wave Height: {sigHeight_m} meters, Swell Height: {swellHeight_m} meters ({swellHeight_ft} feet), Swell Direction: {swellDir16Point}")
                st.write(f"UV Index: {uvIndex}")
                st.write("")  # Add an empty line for better readability

            # Extract and display astronomy data (sunrise and sunset)
            astronomy_data = weather_elem.find(".//astronomy")
            sunrise = astronomy_data.find("sunrise").text
            sunset = astronomy_data.find("sunset").text
            
            st.write(f"Sunrise: {sunrise}, Sunset: {sunset}")
            st.write("")
            
    else:
        st.error(f"Error fetching data. Status code: {response.status_code}")

def main():
    st.set_page_config(page_title="Nautical Navigator")
    st.title("Ahoy, matey! This here application be fer 'elpin' the Cap'n navigate the seas by givin' 'im the forecast an' wave data.")
    lat_input = st.text_input("Enter yer latitude: (-90.000 to 90.000)")
    lon_input = st.text_input("Enter yer longitude: (-180.000 to 180.000)")
    
    if st.button("Submit"):
        try:
            lat = float(lat_input)
            lon = float(lon_input)
            if -90.0 <= lat <= 90.0 and -180.0 <= lon <= 180.0:
                find_current_weather(lat, lon)
            else:
                st.warning("Please enter valid latitude 'n longitude values within the specified range.")
        except ValueError:
            st.warning("Please enter valid latitude 'n longitude values.")


if __name__ == '__main__':
    main()