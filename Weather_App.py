import requests  # Module for making HTTP requests
import numpy as np  # Module for numerical operations
from datetime import datetime, timedelta  # Module for handling date and time
import csv  # Module for reading and writing CSV files
"""Coded by Daniel Van Eyk danielvaneyk@outlook.com for https://mabili.co.za"""

# Weather API Key
API_KEY = "fc230321be3a42b790f210256241202"
BASE_URL = "http://api.weatherapi.com/v1/"


def validate_city_input(city):
    """Validate city input."""
    if not city:
        raise ValueError("City name cannot be empty.")
    return city


def fetch_current_weather(city):
    """Fetch current day weather temperature in Celsius."""
    city = validate_city_input(city)
    # Construct URL for current weather data
    url = f"{BASE_URL}current.json?key={API_KEY}&q={city}"
    # Send HTTP GET request to fetch data with a timeout of 10 seconds
    response = requests.get(url, timeout=10)
    # Convert response to JSON format
    data = response.json()
    # Extract current temperature from JSON response
    temperature = data['current']['temp_c']
    return temperature


def fetch_historical_weather(city):
    """Fetch historical weather data for the last 7 days."""
    city = validate_city_input(city)
    historical_data = []
    # Calculate start and end date for fetching historical data
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
    # Construct URL for historical weather data
    url = f"{BASE_URL}history.json?key={API_KEY}&q={city}&dt={start_date}&end_dt={end_date}"
    # Send HTTP GET request to fetch data
    response = requests.get(url)
    # Convert response to JSON format
    data = response.json()
    # Extract historical data from JSON response
    for forecast in data['forecast']['forecastday']:
        date = forecast['date']
        temperature = forecast['day']['avgtemp_c']
        historical_data.append({'date': date, 'temperature': temperature})
    return historical_data


def calculate_mode_temperature(data):
    """Calculate mode temperature."""
    temperatures = [day['temperature'] for day in data]
    return max(set(temperatures), key=temperatures.count)

def calculate_average_temperature(data):
    """Calculate average temperature."""
    temperatures = [day['temperature'] for day in data]
    return np.mean(temperatures)

def calculate_median_temperature(data):
    """Calculate median temperature."""
    temperatures = [day['temperature'] for day in data]
    return np.median(temperatures)

def save_to_csv(data, filename):
    """Save data to CSV file."""
    with open(filename, 'w', newline='') as file:
        # Create CSV writer object
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        # Write header row to CSV file
        writer.writeheader()
        # Write data rows to CSV file
        writer.writerows(data)


if __name__ == "__main__":
    # Prompt user to enter city name
    city = input("Enter the city name: ")
    try:
        # Fetch and display current weather
        current_temperature = fetch_current_weather(city)
        print(f"Current temperature in {city}: {current_temperature}°C")

        # Fetch and display historical weather data
        historical_data = fetch_historical_weather(city)
        print("Historical weather data for the last 7 days:")
        for day in historical_data:
            print(f"{day['date']}: {day['temperature']}°C")

        # Calculate and display mode, average, and median temperatures
        mode_temp = calculate_mode_temperature(historical_data)
        average_temp = calculate_average_temperature(historical_data)
        median_temp = calculate_median_temperature(historical_data)
        print(f"Mode temperature for the last 7 days: {mode_temp}°C")
        print(f"Average temperature for the last 7 days: {average_temp}°C")
        print(f"Median temperature for the last 7 days: {median_temp}°C")

        # Save historical weather data to CSV file
        save_to_csv(historical_data, 'historical_weather_data.csv')
        print("Historical weather data saved to historical_weather_data.csv")
    except Exception as e:
        # Handle and display any errors
        print(f"Error: {e}")