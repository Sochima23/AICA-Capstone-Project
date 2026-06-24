import requests
import logging

logging.basicConfig(
    filename="api.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
url = "https://api.open-meteo.com/v1/forecast?latitude=4.82&longitude=7.03&current=temperature_2m,relative_humidity_2m"

try:
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        print("Request successful")

        try:
            data = response.json()

            if "current" in data:
                print("Data extracted successfully")

                print("Temperature:", data["current"]["temperature_2m"])
                print("Humidity:", data["current"]["relative_humidity_2m"])

                logging.info("Weather data extracted successfully")

            else:
                print("Invalid response structure")

        except ValueError:
            print("Response is not valid JSON")

    else:
        print(f"Request failed: {response.status_code}")

except requests.exceptions.ConnectionError:
    print("Connection error")

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")

print(data)
