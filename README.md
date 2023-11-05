# Project Title: Nautical Navigators

### Team Members:
* Mohammad-Shamel Agha
* Darien Miller
* Habeebat Jeneen Elwalily

### The Idea:
* The original plan was to develop a weather forecast application to help navigate the seas and know when storms are approaching.
* The weather prediction provides a 7-day forecast that includes the Wind Speed, Swell Data, visibility, and other information for increments of 3 hours.
* The current weather function provides the current temperature, weather forecast, wind data, etc., and is expected to be updated every hour.

Project is deployed on streamlit here: https://hacknjit2023-landsharks.streamlit.app/

### Built With

* [Svelte](https://reactjs.org)
* [Python](https://www.python.org/)
* [Streamlit](https://streamlit.io/)
* [Google Cloud](https://cloud.google.com/?hl=en)
* [Netlify](https://bit.ly/3q4pcJz)
* [Docker](https://www.docker.com/)
* [Jupyter Notebook](https://jupyter.org/)
* [Maritime weather API](http://api.worldweatheronline.com)

### Requirements
* Clone the repository using `git clone https://github.com/darienmiller88/HackNJIT2023-Landsharks`
* Assuming that Python is installed, run pip install streamlit, requests, and python-dotenv
* Have the required API KEY in the env file to call the API
* Run `streamlit run navigator.py` to run the program

### Known Issues
* There is a range issue when plugging in the latitude and longitude
* We tried to implement our project on Google App Engine, but there were permission issues between it and Docker

<p align="right">(<a href="#top">back to top</a>)</p>
