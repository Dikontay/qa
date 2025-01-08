from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import logging

def set_implicit_wait(driver, timeout=10):
    """Set implicit wait."""
    driver.implicitly_wait(timeout)
    logging.info(f"Set implicit wait to {timeout} seconds.")

def wait_for_search_button(driver):
    wait =  WebDriverWait(driver, 10)
    """Wait explicitly for the search button to be clickable."""
    try:
        search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "header-search-button")))
        
        logging.info("Search button is clickable.")
        search_button.click()
        search_query = "selenium"
        logging.info(f"Searching for repositories with query: {search_query}")
        search_bar = wait.until(EC.presence_of_element_located((By.NAME, "query-builder-test")))
        search_bar.send_keys(search_query)
        search_bar.send_keys(Keys.RETURN)

    except Exception as e:
        logging.error(f"Error during explicit wait for the search button: {e}")
        raise

class FluentWaitCondition:
    """Fluent wait condition for dynamic elements."""
    def __call__(self, driver):
        try:
            element = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/main/react-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div[1]/div/span")
            return element if element.is_displayed() else False
        except Exception:
            return False  # Return False if the element is not found

def fluent_wait_for_results(driver):
    """Fluent wait for search results header."""
    try:
        results_header = WebDriverWait(driver, timeout=15, poll_frequency=1).until(FluentWaitCondition())
        logging.info(f"Found element with fluent wait: {results_header.text}")
        return results_header
    except Exception as e:
        logging.error(f"Error during fluent wait: {e}")
        raise