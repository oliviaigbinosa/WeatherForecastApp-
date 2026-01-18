# Implementation (SDLC)
import requests 

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    return response.json()

def main():
    api_key = "YOUR_API_KEY"
    location = input("Enter city: ")
    weather_data = get_weather(api_key, location)
    print(f"Weather in {location}: {weather_data['weather'][0]['description']}")

if __name__ == "__main__":
    main()
