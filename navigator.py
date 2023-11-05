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

    else:
        st.error(f"Error fetching data. Status code: {response.status_code}")

def main():
    st.header("Nautical Navigator")
    lat_input = st.text_input("Enter yer latitude: (-90.000 to 90.000)")
    lon_input = st.text_input("Enter yer longitude: (-180.000 to 180.000)")
    
    if st.button("Submit"):
        try:
            lat = float(lat_input)
            lon = float(lon_input)
            if -90.0 <= lat <= 90.0 and -180.0 <= lon <= 180.0:
                find_current_weather(lat, lon)
            else:
                st.warning("Please enter valid latitude and longitude values within the specified range.")
        except ValueError:
            st.warning("Please enter valid latitude and longitude values.")


if __name__ == '__main__':
    main()