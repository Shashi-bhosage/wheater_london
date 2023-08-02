import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"  

def get_weather_data():
    date = input("Enter the date (YYYY-MM-DD): ")
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        main_data=data["list"]
        
        for i in main_data:
          if (i["dt_txt"].split(" ")[0]==date):
            weather_data=i['main']
            return weather_data["temp"]
        return None

def get_wind_speed_data():
    date = input("Enter the date (YYYY-MM-DD): ")
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        main_data=data["list"]
        
        for i in main_data:
          if (i["dt_txt"].split(" ")[0]==date):
              weather_data=i['wind']
              return weather_data["speed"]
        return None
          
          
      


def get_pressure_data():
    date = input("Enter the date (YYYY-MM-DD): ")
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        main_data=data["list"]
        
        for i in main_data:
          if (i["dt_txt"].split(" ")[0]==date):
              weather_data=i['main']
              return weather_data["pressure"]
        return None
          

def main():
    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            temp = get_weather_data()
            if temp:
                print(f"Temperature: {temp} °C")
            else:
                print("Data not found for the specified date.")
        elif choice == "2":
            wind_speed = get_wind_speed_data()
            if wind_speed:
                print(f"Wind Speed: {wind_speed} km/h")
            else:
                print("Data not found for the specified date.")
        elif choice == "3":
            pressure = get_pressure_data()
            if pressure:
                print(f"Pressure: {pressure} hPa")
            else:
                print("Data not found for the specified date.")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")


main()
