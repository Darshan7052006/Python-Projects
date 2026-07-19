from api import WeatherAPIError, get_air_quality, get_current_weather, get_five_day_forecast
from database import (initialize_database, add_favourite_city, view_favourite_cities,
                      delete_favourite_city, save_history, view_search_history)
from logger import logger
from utils import clean_city_name, format_aqi, format_current_weather, format_forecast

def menu():
    print("\n================================\n")
    print("Welcome to the Weather Dashboard Pro!")
    print("\n================================\n")
    print("Please select an option:")
    print("1) Get Current Weather")
    print("2) Get Five-Day Forecast")
    print("3) Get Air Quality Index (AQI)")
    print("4) Handle Favourite Cities")
    print("5) Search History")
    print("6) Settings")
    print("7) Exit")

def menu2():
    print("\nFAVOURITE LIST AND OPERATIONS\n")
    print("1) Add Favourite City")
    print("2) Delete Favourite City")
    print("3) View Favourite List")
    print("4) Exit from Favourite Corner")


def get_city_from_user():
    city = clean_city_name(input("Enter a city name: "))
    if not city:
        print("City name cannot be empty.")
        return None
    return city


def show_api_error(error):
    print(f"\nError: {error}\n")
    logger.warning("Weather request failed: %s", error)

def main():
    initialize_database()
    units = "metric"

    while True:
        menu()
        try:
            user_choice = int(input("Enter the choice from (1-7): ").strip())
        except ValueError:
            print("Please Enter a valid option from 1 to 7.")
            continue

        if user_choice not in range(1,8) :
            print("Please Enter a valid option from 1 to 7.")
            continue

        print(f"\nYou have selected option {user_choice}\n")
        
        match user_choice:
            case 1:
                city = get_city_from_user()
                if city:
                    try:
                        print(format_current_weather(get_current_weather(city, units), units))
                        save_history(city)
                    except WeatherAPIError as error:
                        show_api_error(error)

            case 2:
                city = get_city_from_user()
                if city:
                    try:
                        print(format_forecast(get_five_day_forecast(city, units), units))
                        save_history(city)
                    except WeatherAPIError as error:
                        show_api_error(error)

            case 3:
                city = get_city_from_user()
                if city:
                    try:
                        print(format_aqi(get_air_quality(city), city))
                        save_history(city)
                    except WeatherAPIError as error:
                        show_api_error(error)

            case 4:
                while True:
                    menu2()
                    try: 
                       choice = int(input("Enter the choice from (1-4): ").strip())
                    except ValueError:
                        print("Please print a valid option from 1 to 4!!")
                        continue

                    if choice not in range(1,5):
                        print("Enter a choice between 1 to 4")
                        continue

                    print(f"{choice} is selected by user")

                    match choice:
                        case 1:
                            city = input("Enter the city which you want to add in your favourite list: ").strip()
                            print("\n")
                            if not city:
                                print("City name cannot be empty!!")

                            elif add_favourite_city(city.title()):
                                print(f"{city.title()} has been added to your favourite list.")
                            
                            else:
                                print(f"{city} is already present in the favourite Cities list")
                        
                        case 2:
                            city = input("Enter the city you want to delete from your favourite list: ").strip()
                            print("\n")
                            if not city:
                                print("City name cannot not be empty")
                            elif delete_favourite_city(city.title()):
                                print(f"{city} has been deleted from your favourite list")

                            else:
                                print(f"{city} is not present in your favourite list")

                        case 3:
                            favourite_cities = view_favourite_cities()
                            if not favourite_cities:
                                print("The List of favourite cities is empty, Please add one!!")
                            else:
                                print("Your Favourite Cities:")
                                for number,city in enumerate(favourite_cities, start =1):
                                    print(f"{number}. {city[0]}")

                        case 4:
                            print("You are being directed out from the favourite Corner")
                            break

            case 5:
                search_history = view_search_history()

                if not search_history:
                    print("No search history found.")
                else:
                    print("\nRecent Search History:")
                    for number, record in enumerate(search_history, start=1):
                        city, searched_at = record
                        print(f"{number}. {city} - {searched_at}")

            case 6:
                print("\nSettings")
                print("1) Celsius (metric)")
                print("2) Fahrenheit (imperial)")
                setting = input("Choose temperature unit (1-2), or press Enter to keep current: ").strip()
                if setting == "1":
                    units = "metric"
                    print("Units set to Celsius.")
                elif setting == "2":
                    units = "imperial"
                    print("Units set to Fahrenheit.")
                elif setting:
                    print("No setting was changed.")

            case 7:
                print("\nThank you for using Weather Dashboard Pro!\n")
                break

        
if __name__ == "__main__":
    main()
                
