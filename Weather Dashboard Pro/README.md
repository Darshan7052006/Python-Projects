# 🌦️ Weather Dashboard Pro

A modular Python command-line weather application that provides real-time weather information, five-day forecasts, air quality data, favourite city management, local caching, and persistent search history using the OpenWeather API.

This project was built to practice real-world Python software engineering concepts including API integration, modular programming, SQLite databases, JSON caching, logging, exception handling, environment variable management, and clean project architecture.

---

## ✨ Features

- 🌤️ Current weather information
- 📅 Five-day weather forecast
- 🌫️ Air Quality Index (AQI)
- ⭐ Favourite city management
- 🗂️ Search history tracking
- ⚡ Local response caching
- 📝 Application logging
- 🌡️ Metric and Imperial unit support
- 🔒 Secure API key management using environment variables
- 💾 SQLite database for persistent storage

---

## 🛠 Technologies Used

- Python 3.x
- OpenWeather API
- SQLite3
- Requests
- python-dotenv
- JSON
- Logging Module
- pathlib

---

## 📂 Project Structure

```
Weather Dashboard Pro/
│
├── api.py
├── cache.py
├── config.py
├── database.py
├── logger.py
├── main.py
├── models.py
├── menu.py
├── utils.py
├── requirements.txt
├── .env
├── .gitignore
│
├── data/
│   ├── weather.db
│   ├── cache.json
│   └── logs.txt
│
└── README.md
```

---

## 🚀 Features Overview

### Current Weather

- Current temperature
- Weather condition
- Feels-like temperature
- Humidity
- Pressure
- Wind speed

---

### Five-Day Forecast

Displays weather forecast at regular intervals including:

- Temperature
- Weather condition
- Date & time

---

### Air Quality

Displays:

- AQI Index
- PM2.5
- PM10
- NO₂
- O₃

---

### Favourite Cities

- Add favourite city
- Delete favourite city
- View saved cities

Stored permanently using SQLite.

---

### Search History

Automatically stores successful weather searches.

Displays the latest search records with timestamps.

---

### Smart Caching

Recently requested weather data is stored locally.

Benefits:

- Faster response
- Fewer API requests
- Reduced network usage

---

### Logging

Application events and errors are stored inside

```
data/logs.txt
```

making debugging easier.

---

## 🔐 Environment Variables

Create a `.env` file in the project root.

```
OPENWEATHER_API_KEY=YOUR_API_KEY
```

The API key is intentionally kept outside the source code.

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Python-Core-Projects.git
```

Move into the project directory

```bash
cd "Weather Dashboard Pro"
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create the `.env` file

```text
OPENWEATHER_API_KEY=YOUR_API_KEY
```

Run the application

```bash
python main.py
```

---

## 🧠 Concepts Practiced

This project demonstrates practical implementation of:

- Modular Programming
- API Integration
- SQLite Database Operations
- JSON Serialization
- File Handling
- Environment Variables
- Exception Handling
- Logging
- Response Caching
- Python Packages
- Project Structure
- Clean Code Practices

---

## 🔮 Possible Future Improvements

- Graphical User Interface (Tkinter / PyQt)
- Weather maps
- Geolocation support
- Weather alerts
- Multiple language support
- Weather charts
- Export reports as PDF
- Docker support
- Unit testing
- CI/CD pipeline

---

## 👨‍💻 Author

Developed as part of my Python learning journey to strengthen backend development, API integration, modular programming, and software engineering fundamentals.

---

## 📄 License

This project is intended for educational and portfolio purposes.