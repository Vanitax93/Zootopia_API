import os
import requests
from dotenv import load_dotenv

load_dotenv()

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    """
    api_key = os.getenv("API_KEY")
    api_url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {"X-Api-Key": api_key}

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return response.json()  # Returns a list of animal objects
    else:
        print(f"Error fetching data: {response.status_code} - {response.text}")
        return []