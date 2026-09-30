import os
from datetime import datetime, timedelta, timezone

import requests


# ============================================================
# CONFIGURATION
# ============================================================

API_KEY = os.getenv("OPENWEATHER_API_KEY")

GEOCODING_URL = (
    "https://api.openweathermap.org/geo/1.0/direct"
)

CURRENT_WEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/weather"
)

FORECAST_URL = (
    "https://api.openweathermap.org/data/2.5/forecast"
)


# ============================================================
# CHECK API KEY
# ============================================================

def check_api_key():

    if not API_KEY:
        print("\nERROR: OpenWeather API key not found.")
        print(
            "Set the OPENWEATHER_API_KEY "
            "environment variable first."
        )
        return False

    return True


# ============================================================
# GET CITY COORDINATES
# ============================================================

def get_coordinates(city):

    parameters = {
        "q": city,
        "limit": 1,
        "appid": API_KEY
    }

    try:

        response = requests.get(
            GEOCODING_URL,
            params=parameters,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        if not data:
            print("\nCity not found.")
            return None

        location = data[0]

        return {
            "name": location["name"],
            "country": location.get("country", ""),
            "state": location.get("state", ""),
            "latitude": location["lat"],
            "longitude": location["lon"]
        }

    except requests.exceptions.Timeout:

        print("\nRequest timed out.")

    except requests.exceptions.ConnectionError:

        print(
            "\nCould not connect to OpenWeather."
        )

    except requests.exceptions.HTTPError:

        print(
            "\nOpenWeather rejected the request."
        )

    except requests.exceptions.RequestException as error:

        print(f"\nRequest error: {error}")

    return None


# ============================================================
# GET CURRENT WEATHER
# ============================================================

def get_current_weather(location):

    parameters = {
        "lat": location["latitude"],
        "lon": location["longitude"],
        "appid": API_KEY,
        "units": "metric"
    }

    try:

        response = requests.get(
            CURRENT_WEATHER_URL,
            params=parameters,
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as error:

        print(
            f"\nCould not retrieve current weather: {error}"
        )

        return None


# ============================================================
# GET FORECAST
# ============================================================

def get_forecast(location):

    parameters = {
        "lat": location["latitude"],
        "lon": location["longitude"],
        "appid": API_KEY,
        "units": "metric"
    }

    try:

        response = requests.get(
            FORECAST_URL,
            params=parameters,
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as error:

        print(
            f"\nCould not retrieve forecast: {error}"
        )

        return None


# ============================================================
# CONVERT UNIX TIME TO CITY LOCAL TIME
# ============================================================

def format_local_time(timestamp, timezone_offset):

    utc_time = datetime.fromtimestamp(
        timestamp,
        timezone.utc
    )

    local_time = (
        utc_time +
        timedelta(seconds=timezone_offset)
    )

    return local_time.strftime("%H:%M")


# ============================================================
# DISPLAY CURRENT WEATHER
# ============================================================

def display_current_weather(location, weather):

    main = weather["main"]
    wind = weather["wind"]
    system = weather["sys"]

    condition = weather["weather"][0]["description"]

    temperature = main["temp"]
    feels_like = main["feels_like"]
    minimum = main["temp_min"]
    maximum = main["temp_max"]

    humidity = main["humidity"]
    pressure = main["pressure"]

    wind_speed = wind["speed"]

    visibility = (
        weather.get("visibility", 0) / 1000
    )

    timezone_offset = weather["timezone"]

    sunrise = format_local_time(
        system["sunrise"],
        timezone_offset
    )

    sunset = format_local_time(
        system["sunset"],
        timezone_offset
    )

    print("\n" + "=" * 60)
    print(
        f"{location['name'].upper()} WEATHER"
        .center(60)
    )
    print("=" * 60)

    print(f"Temperature    : {temperature:.1f} °C")
    print(f"Feels Like     : {feels_like:.1f} °C")
    print(f"Condition      : {condition.title()}")
    print(f"Minimum        : {minimum:.1f} °C")
    print(f"Maximum        : {maximum:.1f} °C")
    print(f"Humidity       : {humidity}%")
    print(f"Pressure       : {pressure} hPa")
    print(f"Wind Speed     : {wind_speed:.1f} m/s")
    print(f"Visibility     : {visibility:.1f} km")
    print(f"Sunrise        : {sunrise}")
    print(f"Sunset         : {sunset}")

    print("=" * 60)


# ============================================================
# PROCESS FORECAST
# ============================================================

def process_forecast(forecast):

    daily_data = {}

    for item in forecast["list"]:

        date = item["dt_txt"].split(" ")[0]

        temperature = item["main"]["temp"]

        rain_probability = (
            item.get("pop", 0) * 100
        )

        condition = (
            item["weather"][0]["description"]
        )

        if date not in daily_data:

            daily_data[date] = {
                "temperatures": [],
                "rain_probability": [],
                "conditions": []
            }

        daily_data[date]["temperatures"].append(
            temperature
        )

        daily_data[date]["rain_probability"].append(
            rain_probability
        )

        daily_data[date]["conditions"].append(
            condition
        )

    return daily_data


# ============================================================
# DISPLAY 5-DAY FORECAST
# ============================================================

def display_forecast(forecast):

    daily_data = process_forecast(forecast)

    print("\n" + "=" * 70)
    print(
        "5-DAY FORECAST".center(70)
    )
    print("=" * 70)

    for date, data in list(
        daily_data.items()
    )[:5]:

        date_object = datetime.strptime(
            date,
            "%Y-%m-%d"
        )

        day_name = date_object.strftime("%A")

        minimum = min(
            data["temperatures"]
        )

        maximum = max(
            data["temperatures"]
        )

        average = (
            sum(data["temperatures"])
            /
            len(data["temperatures"])
        )

        rain_probability = max(
            data["rain_probability"]
        )

        condition = data["conditions"][
            len(data["conditions"]) // 2
        ]

        print(
            f"\n{day_name} "
            f"({date_object.strftime('%d %b')})"
        )

        print(
            f"  Condition        : "
            f"{condition.title()}"
        )

        print(
            f"  Temperature      : "
            f"{minimum:.1f}°C - {maximum:.1f}°C"
        )

        print(
            f"  Average          : "
            f"{average:.1f}°C"
        )

        print(
            f"  Rain Probability : "
            f"{rain_probability:.0f}%"
        )

    print("\n" + "=" * 70)


# ============================================================
# RAIN CHECK
# ============================================================

def rain_check(forecast):

    daily_data = process_forecast(forecast)

    print("\n" + "=" * 60)
    print(
        "RAIN CHECK".center(60)
    )
    print("=" * 60)

    rain_expected = False

    for date, data in list(
        daily_data.items()
    )[:2]:

        date_object = datetime.strptime(
            date,
            "%Y-%m-%d"
        )

        probability = max(
            data["rain_probability"]
        )

        print(
            f"{date_object.strftime('%A')}: "
            f"{probability:.0f}% chance"
        )

        if probability >= 50:
            rain_expected = True

    print("-" * 60)

    if rain_expected:

        print("☔ Rain is reasonably likely.")
        print("Recommendation: Carry an umbrella.")

    else:

        print("☀ No significant rain expected.")
        print("Recommendation: Umbrella probably unnecessary.")

    print("=" * 60)


# ============================================================
# TEMPERATURE ANALYSIS
# ============================================================

def temperature_analysis(forecast):

    daily_data = process_forecast(forecast)

    all_temperatures = []
    daily_averages = {}

    for date, data in list(
        daily_data.items()
    )[:5]:

        temperatures = data["temperatures"]

        all_temperatures.extend(
            temperatures
        )

        daily_averages[date] = (
            sum(temperatures)
            /
            len(temperatures)
        )

    if not all_temperatures:

        print("\nNo temperature data available.")
        return

    highest = max(all_temperatures)
    lowest = min(all_temperatures)

    overall_average = (
        sum(all_temperatures)
        /
        len(all_temperatures)
    )

    warmest_date = max(
        daily_averages,
        key=daily_averages.get
    )

    coldest_date = min(
        daily_averages,
        key=daily_averages.get
    )

    warmest_day = datetime.strptime(
        warmest_date,
        "%Y-%m-%d"
    ).strftime("%A")

    coldest_day = datetime.strptime(
        coldest_date,
        "%Y-%m-%d"
    ).strftime("%A")

    print("\n" + "=" * 60)
    print(
        "TEMPERATURE ANALYSIS".center(60)
    )
    print("=" * 60)

    print(
        f"Highest Temperature : "
        f"{highest:.1f} °C"
    )

    print(
        f"Lowest Temperature  : "
        f"{lowest:.1f} °C"
    )

    print(
        f"Average Temperature : "
        f"{overall_average:.1f} °C"
    )

    print(
        f"Warmest Day         : "
        f"{warmest_day}"
    )

    print(
        f"Coldest Day         : "
        f"{coldest_day}"
    )

    print(
        f"Temperature Range   : "
        f"{highest - lowest:.1f} °C"
    )

    print("=" * 60)


# ============================================================
# OUTDOOR RECOMMENDATION
# ============================================================

def outdoor_recommendation(
    weather,
    forecast
):

    temperature = weather["main"]["temp"]

    wind_speed = weather["wind"]["speed"]

    condition = weather["weather"][0]["main"]

    daily_data = process_forecast(
        forecast
    )

    rain_probability = 0

    for data in list(
        daily_data.values()
    )[:2]:

        rain_probability = max(
            rain_probability,
            max(data["rain_probability"])
        )

    print("\n" + "=" * 60)
    print(
        "OUTDOOR RECOMMENDATION".center(60)
    )
    print("=" * 60)

    print(
        f"Temperature      : "
        f"{temperature:.1f} °C"
    )

    print(
        f"Wind Speed       : "
        f"{wind_speed:.1f} m/s"
    )

    print(
        f"Rain Probability : "
        f"{rain_probability:.0f}%"
    )

    print(
        f"Condition        : "
        f"{condition}"
    )

    print("-" * 60)

    if rain_probability >= 70:

        print("🔴 Poor conditions.")
        print("Rain is highly likely.")

    elif wind_speed >= 15:

        print("🟠 Very windy.")
        print("Outdoor activity may be uncomfortable.")

    elif temperature >= 35:

        print("🟠 Very hot.")
        print("Avoid prolonged outdoor activity.")

    elif temperature <= 5:

        print("🟠 Very cold.")
        print("Dress appropriately.")

    elif rain_probability >= 40:

        print("🟡 Conditions are uncertain.")
        print("Consider carrying an umbrella.")

    else:

        print("🟢 Good conditions!")
        print("Looks like a reasonable time to go outside.")

    print("=" * 60)


# ============================================================
# MENU
# ============================================================

def display_menu(city):

    print("\n" + "=" * 60)
    print(
        "PERSONAL WEATHER DASHBOARD".center(60)
    )
    print("=" * 60)

    print(f"Location: {city}")

    print("\n1. Current Weather")
    print("2. 5-Day Forecast")
    print("3. Rain Check")
    print("4. Temperature Analysis")
    print("5. Should I Go Outside?")
    print("6. Search Another City")
    print("7. Exit")

    print("=" * 60)


# ============================================================
# MAIN
# ============================================================

def main():

    if not check_api_key():

        return

    print("\n" + "=" * 60)
    print(
        "PERSONAL WEATHER DASHBOARD".center(60)
    )
    print("=" * 60)

    city = input(
        "\nEnter a city: "
    ).strip()

    while not city:

        print(
            "City name cannot be empty."
        )

        city = input(
            "Enter a city: "
        ).strip()

    location = get_coordinates(city)

    if location is None:

        return

    current_weather = get_current_weather(
        location
    )

    forecast = get_forecast(
        location
    )

    if (
        current_weather is None
        or forecast is None
    ):

        print(
            "\nCould not retrieve weather data."
        )

        return

    while True:

        display_menu(
            location["name"]
        )

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":

            display_current_weather(
                location,
                current_weather
            )

        elif choice == "2":

            display_forecast(
                forecast
            )

        elif choice == "3":

            rain_check(
                forecast
            )

        elif choice == "4":

            temperature_analysis(
                forecast
            )

        elif choice == "5":

            outdoor_recommendation(
                current_weather,
                forecast
            )

        elif choice == "6":

            new_city = input(
                "\nEnter another city: "
            ).strip()

            if not new_city:

                print(
                    "City name cannot be empty."
                )

                continue

            new_location = get_coordinates(
                new_city
            )

            if new_location is None:

                continue

            new_current_weather = (
                get_current_weather(
                    new_location
                )
            )

            new_forecast = (
                get_forecast(
                    new_location
                )
            )

            if (
                new_current_weather is not None
                and new_forecast is not None
            ):

                location = new_location

                current_weather = (
                    new_current_weather
                )

                forecast = new_forecast

                print(
                    f"\nWeather updated to "
                    f"{location['name']}."
                )

        elif choice == "7":

            print(
                "\nExiting Weather Dashboard. "
                "Goodbye! 🌤️"
            )

            break

        else:

            print(
                "\nInvalid choice. "
                "Please choose 1-7."
            )

        input(
            "\nPress Enter to continue..."
        )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()