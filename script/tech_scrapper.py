from bs4 import BeautifulSoup
import json

# Open the HTML file and read its content
with open('nice_tech.html', 'r') as file:
    html_content = file.read()

# Create a BeautifulSoup object and parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the elements with class 'post-heading' and extract the 'href' attribute from each
post_headings = soup.find_all(class_='post-heading')
links = [tag.a.get('href') for tag in post_headings if tag.a and tag.a.get('href')]

# Find all the elements with class 'meta-excerpt' and extract the text from each
meta_excerpts = soup.find_all(class_='meta-excerpt')
descriptions = [tag.get_text(strip=True) for tag in meta_excerpts]

# Store all the extracted links and descriptions in a list of dictionaries, each having 'link' and 'desc' keys
data = [{'link': link, 'desc': desc} for link, desc in zip(links, descriptions)]

# Convert the list to a JSON object
json_data = json.dumps(data)

# Write the JSON object to a file
with open('data.json', 'w') as file:
    file.write(json_data)