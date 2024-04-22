# import requests
# from bs4 import BeautifulSoup

# # Send a GET request to the website
# url = 'https://levillagebyca.com/les-start-up/'
# response = requests.get(url)

# print("RESPPONSE : ", response.status_code)
# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the HTML content
#     soup = BeautifulSoup(response.content, 'html.parser')
    
#     # Find the elements containing the startup information
#     startup_elements = soup.find_all('div', class_='col-lg-3 col-md-4 col-sm-6 col-12 mb-4')
    
#     # Iterate over each startup element and extract relevant information
#     for startup in startup_elements:
#         # Extract startup name
#         name = startup.find('h3').text.strip()
        
#         # Extract startup description
#         description = startup.find('p').text.strip()
        
#         # Extract startup website link
#         website = startup.find('a')['href']
        
#         print("Name:", name)
#         print("Description:", description)
#         print("Website:", website)
#         print("\n")
# else:
#     print("Failed to retrieve the webpage.")

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup

# # Initialize the Selenium webdriver
# driver = webdriver.Firefox()  # You need to have Chrome webdriver installed and in your PATH

# # Send a GET request to the website
# url = 'https://levillagebyca.com/les-start-up/'
# driver.get(url)

# # Wait for the page to load
# wait = WebDriverWait(driver, 10)
# wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'village')))

# # Click on the desired option
# option = driver.find_element_by_class_name('village.alpes-provence')
# option.click()

# # Wait for the "OK" button to become clickable
# ok_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'OK')]")))

# # Click on the "OK" button
# ok_button.click()

# # Wait for the page to reload after filtering
# time.sleep(2)  # Add a delay to allow the page to reload (adjust as needed)

# # Parse the HTML content of the filtered page
# soup = BeautifulSoup(driver.page_source, 'html.parser')

# # Find the elements containing the startup information
# startup_elements = soup.find_all('div', class_='option alpes-provence')

# # Iterate over each startup element and extract relevant information
# for startup in startup_elements:
#     # Extract startup name
#     name = startup.find('h3').text.strip()
    
#     # Extract startup description
#     description = startup.find('p').text.strip()
    
#     # Extract startup website link
#     website = startup.find('a')['href']
    
#     print("Name:", name)
#     print("Description:", description)
#     print("Website:", website)
#     print("\n")

# # Close the webdriver
# driver.quit()


# import requests
# import json
# from bs4 import BeautifulSoup

# # Define the URL and payload
# url = 'https://levillagebyca.com/wp-admin/admin-ajax.php'
# payload = {
#     'action': 'cats_filter_startups',
#     'block_id': 'block_af444a9889b86470cc0667432dc93ddd',
#     'query_params': 'eyJwb3N0X3R5cGUiOiJzdGFydC11cCIsInBvc3Rfc3RhdHVzIjoicHVibGlzaCIsInBvc3RzX3Blcl9wYWdlIjoiMTgiLCJvcmRlcmJ5IjoidGl0bGUiLCJvcmRlciI6IkFTQyJ9',
#     'display_type': 'grid',
#     'display_navigation': '',
#     'display_pagination': '',
#     'nonce': '9e2fb12d30',
#     's': '',
#     'activity_domain': '',
#     'village': 'provence-cote-dazur'
# }

# # Send a POST request with the payload
# response = requests.post(url, data=payload)

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the JSON response
#     data = response.json()
#     print(data)
    
#     # Extract startup information from the response
#     startup_html = data['result']
#     soup = BeautifulSoup(startup_html, 'html.parser')
    
#     # Find the elements containing the startup information
#     startup_elements = soup.find_all('div', class_='option alpes-provence')
    
#     # Iterate over each startup element and extract relevant information
#     for startup in startup_elements:
#         print("**** STARTUP ==> ", startup)
#         # Extract startup name
#         name = startup.find('h3').text.strip()
        
#         # Extract startup description
#         description = startup.find('p').text.strip()
        
#         # Extract startup website link
#         website = startup.find('a')['href']
        
#         print("Name:", name)
#         print("Description:", description)
#         print("Website:", website)
#         print("\n")
# else:
#     print("Failed to retrieve the data.")
import requests
import json
from bs4 import BeautifulSoup

# Define the URL
url = 'https://levillagebyca.com/les-start-up/'

# Define the base payload with common parameters
base_payload = {
    'action': 'cats_filter_startups',
    'block_id': 'block_af444a9889b86470cc0667432dc93ddd',
    'query_params': 'eyJwb3N0X3R5cGUiOiJzdGFydC11cCIsInBvc3Rfc3RhdHVzIjoicHVibGlzaCIsInBvc3RzX3Blcl9wYWdlIjoiMTgiLCJvcmRlcmJ5IjoidGl0bGUiLCJvcmRlciI6IkFTQyIsInRheF9xdWVyeSI6eyJyZWxhdGlvbiI6IkFORCIsIjAiOnsidGF4b25vbXkiOiJ2aWxsYWdlIiwiZmllbGQiOiJzbHVnIiwidGVybXMiOlsicHJvdmVuY2UtY290ZS1kYXp1ciJdfX19',
    'display_type': 'grid',
    'display_navigation': '',
    'display_pagination': '',
    'nonce': '9e2fb12d30',
    's': '',
    'activity_domain': '',
    'village': 'provence-cote-dazur'
}

# Iterate over 4 pages
for page_num in range(0, 5):
    # Update the payload with the page number
    payload = base_payload.copy()  # Make a copy to avoid modifying the base payload
    payload['query_params'] = f'{{"page":{page_num},"post_type":"startup","posts_per_page":18}}'

    # Send a POST request with the updated payload
    response = requests.post(url, data=payload)
    print("RESPONSE : ", response.status_code)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        print("******* PAGE : ", page_num)
        print("DATA : ", data)
        # Extract startup information from the response
        # startup_html = data['html']
        # soup = BeautifulSoup(startup_html, 'html.parser')
        
        # # Find the elements containing the startup information
        # startup_elements = soup.find_all('div', class_='option alpes-provence')
        
        # # Iterate over each startup element and extract relevant information
        # for startup in startup_elements:
        #     # Extract startup name
        #     name = startup.find('h3').text.strip()
            
        #     # Extract startup description
        #     description = startup.find('p').text.strip()
            
        #     # Extract startup website link
        #     website = startup.find('a')['href']
            
        #     print("Name:", name)
        #     print("Description:", description)
        #     print("Website:", website)
        #     print("\n")
    else:
        print(f"Failed to retrieve data for page {page_num}.")
