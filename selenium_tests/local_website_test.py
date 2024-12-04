from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import json

# Initialize the driver
driver = webdriver.Chrome()

wait=WebDriverWait(driver,10)

try:
    executor_object = {
    'action': 'setSessionName',
    'arguments': {
        'name': "Testing Local Website"
        }
    }
    browserstack_executor = 'browserstack_executor: {}'.format(json.dumps(executor_object))
    driver.execute_script(browserstack_executor)

    driver.maximize_window()
    driver.get("http://localhost:3030/")

    wait.until(EC.visibility_of_element_located((By.XPATH,"//flutter-view[@flt-view-id='0']")))

    # Explicit wait for the login button to be clickable and click it
    login_button = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "//flt-semantics[text()='Sign In with Google']")))
    login_button.click()

    # Wait for dashboard to load
    wait.until(EC.visibility_of_element_located((By.ID, 'flt-semantic-node-25')))

    # Wait for the 'create new category' button to be clickable and click it
    create_category_button = wait.until(EC.element_to_be_clickable((By.ID, 'flt-semantic-node-13')))
    create_category_button.click()

    # Wait for the text input field to be visible, then input text
    # text_input = wait.until(EC.visibility_of_element_located((By.ID, 'flt-semantic-node-34')))
    # input_field = text_input.find_element(By.TAG_NAME, 'input')
    # input_field.click()
    # input_field.send_keys('New Category')

    # Another way to do the above code
    text_input = wait.until(EC.visibility_of_element_located((By.XPATH,"//flt-semantics/input")))
    text_input.click()
    text_input.send_keys('New Category')

     # Wait for the 'OK' button to be clickable and click it
    ok_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//flt-semantics[text()='OK']")))
    ok_button.click()

    # Wait for dashboard to load
    wait.until(EC.visibility_of_element_located((By.ID, 'flt-semantic-node-25')))

    # Wait for the 'entries' page button to be clickable and click it
    # entries_page_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//flt-semantics/span[text()='Entries']")))
    # entries_page_button.click()

    # Using flt-semantics-identifer attribute that was added by Semantics Widget (used as a wrapper)
    entries_page_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//flt-semantics[@flt-semantics-identifier="Entries"]')))
    entries_page_button.click()

    # Wait for elements to load
    wait.until(EC.visibility_of_element_located((By.ID, 'flt-semantic-node-45')))

    # Wait for the dropdown button to be clickable and click it
    dropdown_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//flt-semantics[text()='Coffee (oz)']")))
    dropdown_button.click()

    # Wait for the specific dropdown option to be clickable and select it
    dropdown_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//flt-semantics[text()='Git Commits']")))
    dropdown_option.click()    

    time.sleep(5)

finally:
    # Close the browser
    driver.quit()
