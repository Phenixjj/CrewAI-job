from bs4 import BeautifulSoup
import json

def extract_data(html_file, output_file):
    with open(html_file, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')

    data = []
    for item in soup.find_all('li'):
        name = item.find(class_='annonce_titre').text if item.find(class_='annonce_titre') else None
        type_ = item.find(class_='fa fa-bookmark').parent.text if item.find(class_='fa fa-bookmark') else None
        address = item.find(class_='fa fa-map-marker').parent.text if item.find(class_='fa fa-map-marker') else None
        data.append({'name': name, 'type': type_, 'address': address})

    with open(output_file, 'w', encoding='utf8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# Usage example
html_file = 'nice_it.html'
output_file = 'output_nice.json'
extract_data(html_file, output_file)