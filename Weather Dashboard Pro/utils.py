from datetime import datetime


def clean_city_name(city):
    return " ".join(city.split()).title()


def format_temperature(value, units):
    symbol = " C" if units == "metric" else " F"
    return f"{value:.1f}{symbol}"


def format_wind(speed, units):
    unit = "m/s" if units == "metric" else "mph"
    return f"{speed:.1f} {unit}"


def format_current_weather(data, units):
    weather = data["weather"][0]
    main = data["main"]
    wind = data.get("wind", {})
    return "\n".join([
        f"\nCurrent Weather - {data['name']}, {data['sys']['country']}",
        "-" * 40,
        f"Condition: {weather['description'].title()}",
        f"Temperature: {format_temperature(main['temp'], units)}",
        f"Feels like: {format_temperature(main['feels_like'], units)}",
        f"Humidity: {main['humidity']}%",
        f"Pressure: {main['pressure']} hPa",
        f"Wind: {format_wind(wind.get('speed', 0), units)}",
    ])


def format_forecast(data, units):
    lines = [f"\nFive-Day Forecast - {data['city']['name']}", "-" * 40]
    for item in data["list"]:
        time = datetime.fromtimestamp(item["dt"]).strftime("%a, %d %b %I:%M %p")
        lines.append(
            f"{time}: {format_temperature(item['main']['temp'], units)}, "
            f"{item['weather'][0]['description'].title()}"
        )
    return "\n".join(lines)


def format_aqi(data, city):
    aqi_names = {
        1: "Good",
        2: "Fair",
        3: "Moderate",
        4: "Poor",
        5: "Very Poor",
    }
    details = data["list"][0]
    components = details["components"]
    index = details["main"]["aqi"]
    return "\n".join([
        f"\nAir Quality - {city}",
        "-" * 40,
        f"AQI: {index} ({aqi_names[index]})",
        f"PM2.5: {components['pm2_5']} ug/m3",
        f"PM10: {components['pm10']} ug/m3",
        f"NO2: {components['no2']} ug/m3",
        f"O3: {components['o3']} ug/m3",
    ])
