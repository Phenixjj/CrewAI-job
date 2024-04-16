import json


def filter_json(input_file, output_file):
    with open(input_file, 'r') as file:
        data = json.load(file)

    filtered_data = [item for item in data['items'] if item['nbsal_text'] != '0 salarié' and item['nbsal_text'] != 'Unités non employeuses']
    print(len(filtered_data))
    with open(output_file, 'w') as file:
        json.dump(filtered_data, file, indent=4, ensure_ascii=False)


# Usage example
input_file = 'compagny.json'
output_file = 'output_compagny2.json'
filter_json(input_file, output_file)
