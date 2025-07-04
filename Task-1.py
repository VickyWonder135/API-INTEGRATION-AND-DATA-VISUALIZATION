import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# Set seaborn style
sns.set(style="whitegrid")

# Replace with your OpenWeatherMap API key
API_KEY = "f4abcd803f48aa245cec5d4218e3444a"
CITY = "Chennai"
UNITS = "metric"
API_URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units={UNITS}"

def fetch_weather_data():
    response = requests.get(API_URL)
    data = response.json()
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {data.get('message', 'Unknown error')}")
    return data

def process_data(data):
    forecast_list = data['list']
    times = [datetime.datetime.fromtimestamp(entry['dt']) for entry in forecast_list]
    temps = [entry['main']['temp'] for entry in forecast_list]
    humidities = [entry['main']['humidity'] for entry in forecast_list]
    pressures = [entry['main']['pressure'] for entry in forecast_list]

    return times, temps, humidities, pressures

def plot_dashboard(times, temps, humidities, pressures):
    fig, axs = plt.subplots(3, 1, figsize=(12, 10), sharex=True)

    sns.lineplot(x=times, y=temps, ax=axs[0], color='tomato')
    axs[0].set_title('Temperature Forecast (°C)')
    axs[0].set_ylabel('Temperature')

    sns.lineplot(x=times, y=humidities, ax=axs[1], color='dodgerblue')
    axs[1].set_title('Humidity Forecast (%)')
    axs[1].set_ylabel('Humidity')

    sns.lineplot(x=times, y=pressures, ax=axs[2], color='seagreen')
    axs[2].set_title('Pressure Forecast (hPa)')
    axs[2].set_ylabel('Pressure')
    axs[2].set_xlabel('Date and Time')

    plt.tight_layout()
    plt.suptitle(f"5-Day Weather Forecast Dashboard for {CITY}", fontsize=16, y=1.02)
    plt.show()

# Run the app
try:
    weather_data = fetch_weather_data()
    times, temps, humidities, pressures = process_data(weather_data)
    plot_dashboard(times, temps, humidities, pressures)
except Exception as e:
    print("Error:", e)
