from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

def perform_search(input_file):
    # Load the data from the JSON file
    with open(input_file, 'r') as file:
        data = json.load(file)

    # Initialize the WebDriver
    driver = webdriver.Firefox()

    for item in data:
        # Open Google
        driver.get('https://www.google.com')

        try:
            print(f"Searching for: {item['name']}")

            # Wait until the "I agree" button is available and click it
            agree_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[text()="I agree"]')))
            agree_button.click()

            # Wait until the search box is available
            search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))

            # Use JavaScript to set the value of the search box
            driver.execute_script("arguments[0].value = arguments[1];", search_box, item['name'])

            # Submit the form
            search_box.send_keys(Keys.CONTROL + Keys.RETURN)  # Open search in a new tab
        except Exception as e:
            print(f"An error occurred: {e}")

        # Wait for the page to load
        time.sleep(2)

    # Close the WebDriver
    driver.quit()

# Usage example
input_file = 'output_nice.json'
perform_search(input_file)