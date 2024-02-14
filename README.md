# weatherapp
A Python application that can fetch, process, and display weather data for any city provided. The application should allow users to input a city and retrieve its current weather as well as the last seven days' historical data and save the results to a .csv file.

A detailed and descriptive analysis of the Python Weather App
The code provided is well-structured and adheres to the PEP8 guidelines for Python code style. Here's a detailed explanation of each part of the code:
Imports:
•
requests: This module is used for making HTTP requests.
•
numpy as np: Numpy is a library for numerical operations, and it's aliased as np for convenience.
•
datetime, timedelta: These are modules for handling dates and times.
•
csv: This module is for reading and writing to CSV files.
Constants:
•
API_KEY and BASE_URL: These are constants used for accessing the weather API. API_KEY stores the API key required for authentication, and BASE_URL stores the base URL of the weather API.
Functions:
1.
validate_city_input(city): This function validates the input city name. If the city name is empty, it raises a ValueError.
2.
fetch_current_weather(city): This function fetches the current weather temperature in Celsius for the given city using the weather API. It constructs a URL with the provided city and API key, sends an HTTP GET request, and returns the current temperature.
3.
fetch_historical_weather(city): This function fetches historical weather data for the last 7 days for the given city. It constructs a URL with the city, start date (7 days ago), end date (today), and API key, sends an HTTP GET request, and returns a list of dictionaries containing date and temperature for each day.
4.
calculate_mode_temperature(data): This function calculates the mode temperature from the historical weather data. It extracts temperatures from the data, finds the most frequently occurring temperature, and returns it.
5.
calculate_average_temperature(data): This function calculates the average temperature from the historical weather data using NumPy's np.mean() function.
6.
calculate_median_temperature(data): This function calculates the median temperature from the historical weather data using NumPy's np.median() function.
7.
save_to_csv(data, filename): This function saves the historical weather data to a CSV file. It opens the file in write mode, creates a CSV writer object, writes the header row, and then writes the data rows
