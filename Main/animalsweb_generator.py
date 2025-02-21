import requests
import json

def fetch_animal_data(animal_name, api_key):
    """Fetches animal data from API Ninjas for a given animal name."""
    api_url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {"X-Api-Key": api_key}

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return response.json()  # Returns a list of animal objects
    else:
        print(f"Error fetching the data: {response.status_code} - {response.text}")
        return []


def serialize_animal(animal_obj):
    """Serializes a single animal object into HTML."""
    output = f"""
    <li class="cards__item">
        <div class="card__title">{animal_obj['name']}</div>
        <p class="card__text">
            <strong>Diet:</strong> {animal_obj['characteristics'].get('diet', 'Unknown')}<br/>
            <strong>Location:</strong> {', '.join(animal_obj['locations'])}<br/>
            <strong>Type:</strong> {animal_obj['characteristics'].get('type', 'Unknown')}<br/>
        </p>
    </li>
    """
    return output


def generate_html_content(animals):
    """Generates the complete HTML string for all animals."""
    html_list = ""
    for animal in animals:
        html_list += serialize_animal(animal)
    return html_list


def main():
    """Fetches data from API, generates HTML, and writes to a new file."""
    api_key = "z1EMZU9Yktqwq35KPmNhTA==N5PxYyir0NkRNKlC"
    animal_name = "Fox"
    animals_data = fetch_animal_data(animal_name, api_key)

    if not animals_data:
        print("Cannot get animals data.")
        return

    # Read the HTML template
    with open("animals_template.html", "r") as template_file:
        template_content = template_file.read()

    # Generate the animal list HTML
    animal_html_list = generate_html_content(animals_data)

    # Replace placeholder with generated HTML
    new_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", animal_html_list)

    # Write to output file
    with open("animals.html", "w") as output_file:
        output_file.write(new_html_content)
    print("HTML file generated as 'animals.html'")


if __name__ == "__main__":
    main()