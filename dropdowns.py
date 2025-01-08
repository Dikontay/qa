from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# Logging setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# WebDriver initialization
driver = webdriver.Chrome()
#driver.set_page_load_timeout(30)

try:
    logging.info("Navigating to W3Schools TryIt Editor")
    driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select")

    # Wait for the iframe to load
    logging.info("Switching to iframe")
    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "iframeResult"))
    )

    # Wait for dropdown to be present
    logging.info("Waiting for dropdown")
    dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "select"))
    )

    # Select an option from dropdown
    logging.info("Interacting with dropdown")
    select = Select(dropdown)
    select.select_by_visible_text("Volvo")

except Exception as e:
    logging.error(f"An error occurred: {e}")

finally:
    logging.info("Closing the browser")
    driver.quit()
