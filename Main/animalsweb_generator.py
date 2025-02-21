import json

def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data("animals_data.json")

def serialize_animal(animal_obj):
    """Serializes a single animal object into HTML."""
    output = f"""
    <li class="cards__item">
        <div class="card__title">{animal_obj['name']}</div>
        <p class="card__text">
            <strong>Diet:</strong> {animal_obj['characteristics'].get('diet')}<br/>
            <strong>Location:</strong> {', '.join(animal_obj['locations'])}<br/>
            <strong>Type:</strong> {animal_obj['characteristics'].get('type')}<br/>
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
    """Reads template, generates HTML, and writes to a new file."""
    with open("animals_template.html", "r") as template_file:
        template_content = template_file.read()

    with open("animals_data.json", "r") as data_file:
        animals_data = json.load(data_file)

    animal_html_list = generate_html_content(animals_data)

    # Replace placeholder with generated HTML
    new_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", animal_html_list)

    with open("animals.html", "w") as output_file:
        output_file.write(new_html_content)

if __name__ == "__main__":
    main()